# A Cost-Aware Runtime for Browser Agents

*Draft — for Month 2 publish on personal blog / Medium / dev.to, cross-posted to Hacker News and r/LocalLLaMA. Based on Purdue ECE 50874 final project, Team 17.*

---

> Author note: ~1,800-2,500 words target. Diagrams: 1 architecture, 1 cost-over-time chart, 1 latency comparison chart. Inline code blocks for the policy decision example.
>
> Headline candidates:
> - "A Cost-Aware Runtime for Browser Agents"
> - "What happens when you put a budget around your agent loop"
> - "Token / cost / step budgets as a side-car for OpenClaw"
>
> Use the first one for HN; it's the most concrete.

---

## TL;DR

Browser agents (Claude Operator, OpenAI's Operator, OpenClaw, etc.) are usually shipped without runtime budgets. We took the open-source [OpenClaw](https://github.com/openclaw-ai/openclaw) project and built a thin governance layer that gives each task per-run budgets on tokens, cost, wallclock, and steps; a post-action policy decision point; rolling cost / latency aggregates; and manual pricing overrides for models whose SKUs your billing system hasn't seen yet. The agent core didn't change. The agent got measurably more useful in production-shaped scenarios. We're open-sourcing the runtime — repo and IEEE-style report linked at the bottom.

## The shape of the problem

You let an autonomous agent loose against a real browser. Three failure modes will dominate your operational pain:

1. **Token / cost blow-up.** A loop hits a slow tool or repeats itself; the agent burns through hundreds of dollars of context-padded LLM calls before anyone notices.
2. **Latency tail.** Most runs complete in 30 seconds, but the long tail goes to 30 minutes — agent steps stack while the user waits.
3. **Step-count explosion.** The agent gets into a "self-correction" loop: scroll, retry, re-read, scroll, retry. Each step costs tokens and time and produces no progress.

The standard reactions are wrong:

- **Hard kill at a token cap.** Brittle. You sacrifice good runs to protect against bad ones.
- **Rewrite the agent.** Expensive, and the agent is improving every month upstream.
- **Wrap in a retry-with-backoff.** Doesn't help; you needed cost-aware *halting*, not cost-aware *retry*.

What you actually want is a control plane *around* the agent that doesn't have an opinion on what the agent does step-to-step but does have a strong opinion on whether the run can keep going.

## Design goals

When we started the project (Purdue ECE 50874 final project, Team 17), we set four hard constraints:

1. **Don't touch the agent core.** OpenClaw is a living codebase upstream. Anything that requires forking it loses.
2. **Decisions happen at step boundaries.** Mid-step interruption is fragile; post-step policy decisions are robust.
3. **Cost is a first-class signal.** Not a billing afterthought. Cost goes into routing decisions in real time, the same way you'd treat queue depth.
4. **Pricing tables must be editable by a human at 2 AM.** Vendors invent SKUs faster than your billing rollups can model them; this needed to be a config field, not a database migration.

## Architecture

```
+--------------+        +--------------------+        +----------------+
|  OpenClaw    |  step  |   LLM Insights     |  call  |   AgentOps     |
|  agent core  +------->+   Gateway plugin   +------->+   (routing,    |
|              |        |                    |        |    budgets)    |
+--------------+        +--------+-----------+        +-------+--------+
                                 |                            |
                                 v                            v
                          +------+-----+               +------+-----+
                          | Langfuse   |               | Manual     |
                          | (traces)   |               | pricing    |
                          +------------+               | overrides  |
                                                       +------------+
```

(Replace with a proper diagram on publish — Excalidraw or Mermaid.)

The key components:

- **LLM Insights Gateway plugin** — sits between the agent and any LLM call. Tags every call with `(run_id, step_id, tenant_id)`. Returns the response, plus emits a cost event.
- **AgentOps integration** — routes between providers based on budget state; returns "halt" / "throttle" / "allow" at policy decision points.
- **Langfuse integration** — trace telemetry; every step is a span with cost + token annotations.
- **Manual pricing overrides** — a JSON table of `model_id -> {prompt_per_1k, completion_per_1k}`. Defaults from each vendor's published prices; humans can override per model + per tenant.

## What a step boundary looks like in code

```python
# Pseudocode; see repo for actual implementation.

def step(run_state):
    action = agent.next_action(run_state)        # Agent decides what to do.
    if action.kind == "llm_call":
        out, usage = llm_gateway.call(action.request, run_state)   # gateway annotates.
        run_state.apply_llm_result(out, usage)
    elif action.kind == "tool_call":
        out, side_effects = tool_runner.call(action.tool, action.args)
        run_state.apply_tool_result(out, side_effects)

    # Cost event always emitted.
    cost_events.publish(run_state.delta())

    # Policy decision after the step, never during.
    decision = policy.decide(run_state)
    if decision == "halt":
        return Halt(reason=decision.reason)
    elif decision == "throttle":
        sleep_then_continue(decision.delay)

    return Continue
```

Two important things this gets right:

- Cost is computed inside the gateway from the LLM provider's response, using the **resolved pricing table** (manual override > vendor default), so the run_state.delta() emission has the correct cost.
- Policy decisions happen *after* the step. If the agent has just produced a useful side-effect, we don't abort mid-side-effect.

## The benchmark

We ran two configurations against the same set of OpenClaw scenarios (web-search → form-fill → submit):

- **Baseline:** OpenClaw, no runtime, no budgets.
- **Cost-aware:** same OpenClaw, plus the runtime, with budgets of 4,000 tokens / $0.20 / 60s / 12 steps.

Across N runs (results in the IEEE report; I'll insert real numbers when re-running for blog):

| Metric                 | Baseline | Cost-aware | Δ |
|------------------------|----------|------------|---|
| p50 cost per task      | (fill)   | (fill)     | (fill) |
| p95 cost per task      | (fill)   | (fill)     | (fill) — the long tail compresses dramatically |
| p50 latency            | (fill)   | (fill)     | (fill) |
| p95 latency            | (fill)   | (fill)     | (fill) |
| % runs successfully halted in cost overrun | (fill) | (fill) | n/a — baseline has no halt |
| Task success rate       | (fill)   | (fill)     | (fill) — should be ≈ flat |

(Re-run benchmarks before publishing. The point of this section is: cost-aware doesn't cost task success — it caps the tail.)

> Action item before publishing: re-run benchmarks on a refreshed OpenClaw HEAD, capture cost / latency per task, generate two charts (cost over time, latency CDF). Tag them in this draft.

## What we got wrong the first time

A few lessons that I'd skip if I were building this again:

- **First version put policy decisions inside the gateway.** That mixed concerns. The gateway should observe and report; policy should be a separate object with its own state. We split it.
- **First pricing table was a Python dict in code.** Useful until you need to deploy at 2 AM for a model SKU that just shipped. Moved to YAML with a hot reload.
- **First budgets were per-tenant.** Per-task is the right granularity; per-tenant rolls up cleanly from per-task. Per-tenant-only didn't catch a single-task runaway.
- **First policy halted hard.** Adding `throttle` (sleep-then-continue) and `escalate_to_human` (pause-resume) drastically improved usability without losing safety.

## What this maps to in production

The same shape applies to any agent platform, not just OpenClaw:

- A LangGraph agent — wrap the model nodes with the gateway; policy decisions at edges.
- A Claude Agent SDK app — middleware on `client.messages.create`.
- A multi-agent system — propagate budget down to sub-agents; cost rolls up.

It also matches the runtime needs I see daily at GEICO Developer Engineering, where we're rolling out Claude Code, Cursor, and MCP servers to a 282-person organization. Cost governance is the question hiring managers ask after "does it actually work."

## What's next

- Move from JSON pricing overrides to a small admin UI; price discovery from vendor APIs where they expose them.
- Multi-provider routing on cost-quality curves (route 70% of work to cheaper models that hit the quality bar; reserve premium models for hard cases).
- A regression suite that proves cost-aware doesn't degrade quality, not just by anecdote.

If you're building agents in production, the most useful thing this work might give you is a vocabulary: **token budget, cost budget, wallclock budget, step budget, policy decision point, manual pricing override**. The vocabulary lets you talk about a class of failures that's currently named "the agent did something weird and now we're getting paged."

---

**Links**

- Code: https://github.com/mailming/openclaw/tree/feature/llm-insights-manual-pricing
- Report (IEEE-style): (link to PDF when published)
- About me: [linkedin.com/in/mailming](https://www.linkedin.com/in/mailming) — currently Staff platform engineer at GEICO, leading our Claude Code / Cursor / MCP rollout, MS-AI in progress at Purdue.

---

## Publishing checklist (do not include in published post)

- [ ] Re-run benchmarks, fill (fill) cells with real numbers
- [ ] Replace ASCII architecture with Mermaid or Excalidraw PNG
- [ ] Cost-over-time line chart (matplotlib)
- [ ] Latency CDF (matplotlib)
- [ ] One real code snippet from `openclaw` repo (not pseudocode) — license check
- [ ] Cross-post: Hacker News (Show HN, link to blog), r/LocalLLaMA (text post), LinkedIn (4-6 sentence summary + link), X (thread of 5-7 tweets)
- [ ] Update LinkedIn Featured with this post
- [ ] Add one bullet to `resume-ai-infra.md` under OpenClaw section: "Published blog post + benchmark report at [link], cross-posted to Hacker News / r/LocalLLaMA"
- [ ] Forward to all open recruiter conversations and the 3+ active referral contacts from `referrals.md`
