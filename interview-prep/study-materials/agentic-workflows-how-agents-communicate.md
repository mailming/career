# Agentic Workflows — How Agents Communicate (Mastery Path)

**Goal:** Be able to draw and explain (in 10 minutes) how agents talk to each other, and build a tiny multi-agent demo you can show in interviews.

**You already have pieces of this:** SmartTuna (LangGraph), GEICO Claude Agent SDK triage, MCP tools, OpenClaw (tool + budget loop). This doc connects those into a clean mental model.

---

## 1. The one idea that unlocks everything

**Agents do not “telepathically chat.”**  
They communicate through **shared state** and **control transfer** (who runs next).

Every multi-agent system is three layers:

```
┌─────────────────────────────────────────┐
│  1. ORCHESTRATION  (who goes next?)     │  supervisor / handoff / pipeline
├─────────────────────────────────────────┤
│  2. STATE          (what do they share?) │  messages, scratchpads, artifacts
├─────────────────────────────────────────┤
│  3. TOOLS          (how they act?)       │  MCP, APIs, browser, other agents
└─────────────────────────────────────────┘
```

If you can explain those three for any product (SmartTuna, Waymo Inner Loop, Slack triage), you “master” agentic workflows for interviews.

---

## 2. How agents communicate — 4 patterns (memorize these)

### Pattern A — Supervisor + Workers (most common in 2026)

```
User → Supervisor → Worker A → Supervisor → Worker B → Supervisor → User
```

- **Supervisor** is an LLM that *only* decides: call which worker, or finish.
- **Workers** are specialist agents (research, code, triage, reviewer).
- Communication = supervisor writes into **shared state** (“task for coder”), worker writes **result** back, supervisor reads it.

**Your GEICO map:** Slack triage bot is often a mini-supervisor: classify → pick skill (`solve-case` / `close-case`) → tool calls → reply.

**Interview one-liner:**  
*"Hub-and-spoke. All routing through one controller. Easy to audit and budget; extra LLM hops."*

---

### Pattern B — Handoff / Swarm (peer-to-peer)

```
User ↔ Agent A ──handoff──→ Agent B ──handoff──→ Agent C
```

- Agent A decides “this is B’s job” and **transfers control** (and usually a summary of context).
- No permanent manager. Like a relay race.

**Interview one-liner:**  
*"Peer handoff. Fewer hops, harder to debug loops — need max-steps and clear ownership."*

---

### Pattern C — Pipeline (fixed order)

```
Spec agent → Code agent → Test agent → Review agent → Done
```

- Edges are **fixed** (not LLM-chosen each time).
- Best when the workflow is known (CI migration PRs, ADR → validation).

**Your GEICO map:** AI CI/CD migration engine ≈ pipeline: inventory → classify → generate PR → human review.

---

### Pattern D — Fan-out / map-reduce

```
Supervisor → [Worker1, Worker2, Worker3] in parallel → Merge → Continue
```

- Independent subtasks run at once; results merge into shared state.
- LangGraph: `Send` API / parallel nodes.

---

## 3. What actually gets passed between agents

| Channel | What it is | When to use |
|---------|------------|-------------|
| **Shared message list** | Full chat history all agents see | Small systems; simple |
| **Final-result only** | Worker keeps private scratchpad; publishes summary | Many agents; context explosion |
| **Typed artifacts** | Structured objects: `{ticket_id, diagnosis, pr_url}` | Production (your AMP/triage style) |
| **Tool call to sub-agent** | Parent calls `run_agent(name, input)` like a tool | Nested agents (Claude subagents, LangGraph subgraph) |
| **MCP / external tools** | Agents don’t talk to each other — both call same tools (JFrog, Slack) | Shared systems of record |

**Production rule (remember for Waymo / GEICO):**  
Prefer **typed artifacts + short summaries** over dumping full chain-of-thought between agents. Cheaper, safer, easier to eval.

---

## 4. The agent loop (single agent — build this first)

Every agent, before multi-agent:

```
1. Read state (messages / task)
2. LLM decides: tool call OR final answer
3. If tool: execute → append result to state → go to 1
4. If done: return
5. Always: check budgets (tokens / steps / cost) — OpenClaw lesson
```

Multi-agent = **same loop**, plus a routing decision: *which agent node runs next?*

---

## 5. Map to YOUR projects (say this in interviews)

| Your work | Pattern | How “agents” communicate |
|-----------|---------|---------------------------|
| **SmartTuna** | Supervisor or pipeline of LangGraph nodes | Shared graph state between analysis agents; model-pluggable providers |
| **Slack triage bot** | Supervisor + tools/skills | Classify → skill → MCP tools (JFrog/Slack) → reply in channel |
| **MCP servers** | Tools, not agents | Agents call tools; tools don’t call agents (usually) |
| **OpenClaw cost-aware runtime** | Policy around the loop | Observes each step; Allow/Halt — communication with *runtime*, not peer agents |
| **Waymo Inner Loop (target)** | Pipeline + supervisor | Spec → codegen → test → iterate; shared run state + eval harness |

---

## 6. Learning path — 2 weeks to fluency

Do in order. Do not skip to frameworks before patterns.

### Days 1–2 — Mental model (2 hrs total)

**Read (pick one primary):**
1. Anthropic — [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) (workflows vs agents)
2. Your own: [03-agent-orchestration.md](../system-design/03-agent-orchestration.md) § Sub-agents + Run model
3. LangGraph concepts: [Multi-agent](https://langchain-ai.github.io/langgraph/concepts/multi_agent/) (supervisor vs network vs handoffs)

**Exercise (30 min):** On paper, draw SmartTuna OR Slack triage as boxes. Label: who decides next? what state is shared?

---

### Days 3–5 — Build one tiny multi-agent (the mastery drill)

**Project: “Ticket Triage Crew”** (mirrors GEICO help channel)

3 agents only:
1. **Classifier** — output JSON: `{category, priority}`
2. **Resolver** — given category, call 1 fake tool (`lookup_runbook(id)`)
3. **Responder** — write a short Slack-style reply

**Implement with ONE of:**
- **A (recommended for you):** LangGraph supervisor — you already use LangGraph in SmartTuna  
  Docs: [LangGraph multi-agent](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/agent_supervisor/)
- **B:** Claude Agent SDK with a subagent / tool that is another agent  
  Docs: Anthropic Agent SDK / Claude Code subagents

**Acceptance criteria:**
- [ ] Trace shows: Classifier → Resolver → Responder  
- [ ] Shared state has typed fields, not only free text  
- [ ] Max 8 steps; if exceeded → halt (OpenClaw habit)  
- [ ] One markdown README with the diagram  

**Time box:** 4–6 hours across 3 evenings. Ship ugly code that works.

---

### Days 6–7 — Communication deep dive (2 hrs)

Read + take 5 bullets of notes:
- Handoff vs Supervisor: [Medium — Handoff vs Supervisor](https://medium.com/@attia.atef92/handoff-vs-supervisor-why-your-multi-agent-architecture-choice-matters-%EF%B8%8F-40cadb0e0dc2) *or* LangGraph multi-agent concepts page
- Optional: [OpenAI Agents SDK — handoffs](https://openai.github.io/openai-agents-python/) (conceptual; you don’t need to switch stacks)

**Speak aloud (2 min):**  
*"I’d pick supervisor when I need auditability and one budget owner; handoff when latency and specialist UX matter; pipeline when the steps are fixed."*

---

### Week 2 — Production hardening (interview gold)

1. Re-read [04-eval-pipelines.md](../system-design/04-eval-pipelines.md) — how do you know multi-agent got better?  
2. Add to your Triage Crew:
   - 10 golden tickets with expected category  
   - Simple accuracy metric  
3. Rehearse design prompt cold (10 min):  
   *"Design a multi-agent system that helps engineers write and test code from a natural-language spec."*  
   Use [waymo-devai-surge.md](../waymo-devai-surge.md) Day 1 checklist.

---

## 7. Cheat sheet — answer any “how do agents talk?” question

Use this script:

> "Agents communicate through **shared state** and **routing**, not magic chat.  
> In the **supervisor** pattern, a controller LLM picks a specialist; the worker writes a **typed result** back into state; the supervisor decides again or finishes.  
> In **handoff**, the specialist transfers control and a summary to the next agent.  
> In **pipeline**, the graph edges are fixed.  
> Tools (MCP) are how agents touch the world; **sub-agents** are just tools that are themselves agent runs.  
> I enforce **budgets at step boundaries** — that’s what I built in OpenClaw — so agent-to-agent chatter can’t run forever."

---

## 8. Resources (ranked — don’t binge all)

| Priority | Resource | Why |
|----------|----------|-----|
| 1 | Anthropic [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) | Correct mental model: workflows vs agents |
| 2 | [LangGraph multi-agent concepts](https://langchain-ai.github.io/langgraph/concepts/multi_agent/) | Matches SmartTuna |
| 3 | Your [03-agent-orchestration.md](../system-design/03-agent-orchestration.md) | Interview design depth + OpenClaw/MCP |
| 4 | Build Triage Crew (above) | Only way to *master* |
| 5 | Claude Agent SDK docs (subagents / tools) | GEICO stack fluency |
| 6 | Optional: CrewAI / AutoGen tutorials | Skip until after Triage Crew ships |

**Skip for now:** academic multi-agent RL papers, AutoGPT nostalgia blogs, 10-framework comparison videos.

---

## 9. Tonight (30–45 min) — start here

1. Read Anthropic “Building Effective Agents” (or skim) — 20 min.  
2. Draw on one page: Classifier → Resolver → Responder with arrows labeled **state** and **who routes**.  
3. Open SmartTuna repo (or GEICO triage notes) and write 3 bullets: *where is the supervisor? what is shared state? what are the tools?*

Done when you can explain Pattern A and C without notes.
