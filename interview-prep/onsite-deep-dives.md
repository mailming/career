# Onsite Deep-Dives — 3 Staff-Level Narratives

These are 30-45 min rehearsed talks you can deliver in the "deep dive" or "tech presentation" round at an onsite loop. Each has a one-slide outline you can sketch on a whiteboard, a 5-min compact version (for HM follow-ups), and the FAQ.

## Deep-Dive #1 — Artifactory 99.99% Turnaround

**Audience:** SRE / platform / infra interviewers. Bias them toward your reliability seniority.

### One-slide outline

```
Title: From monthly outages to 99.99% on Artifactory at GEICO

Y-axis: outage minutes / month
X-axis: months (12 prior + current)
  [Bars: starting tall, dropping over 4 quarters]

Below:
  - 5 dependency classes
  - 1 firewall TLS DPI class (40% of outage minutes) → fixed first
  - AI-consumable runbooks → on-call survivability
  - Entra ID + APIM defense in depth
  - NOCIM-11695 CoE → 2 latent issues fixed
```

### 30-min flow

1. **Frame (3 min):** what AMP is, what it serves (every container image, model artifact, ML binary), the SLO ask.
2. **Inventory the failure surface (5 min):** the 12-month spreadsheet of every incident, classified by root cause; show the Pareto.
3. **Pareto fix (8 min):** the firewall TLS DPI class, packet-level RCA, the cross-team plan with Network and Database Platform.
4. **AI-consumable runbooks + agent skills (5 min):** how `solve-case`, `close-case`, `build-kb` Claude / Cursor skills let any on-call engineer (and any agent) close pages without paging me.
5. **Entra ID + APIM (5 min):** the auth-side hardening; Go JWT middleware; ACS production deploy.
6. **NOCIM-11695 (3 min):** the highest-severity incident, the CoE structure, the two latent issues you exposed.
7. **Lessons (1 min):** sequencing matters more than scope; write runbooks before they're needed.

### 5-min compact version

> When I joined the AMP team Artifactory had monthly outages. The bulk of the outage minutes came from a single failure class — Azure Firewall TLS DPI inspecting S3-backed JFrog repos. I led the packet-level RCA across Network, Database Platform, and JFrog; we got the firewall reconfigured, mitigated client-side, and the outage minutes for that class went to near zero. In parallel I built AI-consumable runbooks and a set of Claude / Cursor agent skills that closed common pages without paging me — that's what got on-call survivable. We ended that year at 99.99% SLO. The highest-severity event after that was an Entra-driven outage I led the CoE for, which surfaced two latent issues we fixed before they re-tripped.

### FAQ

- **What was the hardest tradeoff?** Ignoring 3 noisy smaller incident classes for the first quarter; sequencing on impact, not noise.
- **Where did AI fit in?** AI-consumable runbooks were the highest-leverage piece — an artifact that any human or agent can use.
- **What's the next reliability lever?** JFrog SaaS POC results — SaaS removes a whole class of self-hosted failure surface.

---

## Deep-Dive #2 — OpenClaw Cost-Aware Runtime

**Audience:** Agent platform / AI infra interviewers. Bias them toward your AI/agentic-systems chops.

### One-slide outline

```
Title: A cost-aware runtime for browser agents (Purdue ECE 50874 Team 17)

[Box: OpenClaw agent core] -- step --> [Box: LLM Insights gateway] -- call -->
                                          | (cost event)         (LLM provider)
                                          v
                                       [AgentOps: routing + budget]
                                       [Langfuse: trace + cost]
                                       [Manual pricing overrides]

Below:
  4 design constraints
  Policy decisions at step boundaries
  Cost as a first-class signal
  Manual pricing overrides (vendor SKU race)
  Benchmark: p95 cost ↓↓, task success ≈ flat
```

### 30-min flow

1. **Problem framing (4 min):** three failure modes of unbudgeted agents — cost blow-up, latency tail, step explosion.
2. **Why the usual reactions are wrong (3 min):** hard cap is brittle; rewrite is expensive; retry doesn't help.
3. **Design constraints (3 min):** the four rules — no agent-core changes, policy at step boundaries, cost as first-class signal, hot-reloadable pricing tables.
4. **Architecture (8 min):** the gateway, AgentOps integration, Langfuse, pricing-override table; draw the diagram on the whiteboard.
5. **Walk a step at code level (5 min):** the step() pseudocode; explain what happens at each line and why.
6. **Benchmark (5 min):** scenarios, baselines, results — cost-tail compresses, success rate is flat, latency tail follows cost tail.
7. **Lessons (2 min):** policy ≠ observation (split the modules); pricing is hot-reloadable config not code; per-task is the right granularity.

### 5-min compact version

> OpenClaw is an open-source browser-agent. We took it as-is and built a thin governance layer around it. The trick is that the runtime never decides what the agent does — it only decides whether the agent can keep going. At each step boundary the gateway emits a cost event, the policy module looks at the run's remaining budget and decides to allow, throttle, halt, or escalate to a human. The pricing table is hot-reloadable JSON because vendors invent SKUs faster than billing systems can model them. Benchmarks: with the runtime on, the cost tail compresses dramatically while task success rate is flat. The vocabulary it gives you — token budget, cost budget, step budget, policy decision point — turns "the agent did something weird" into a class of failures you can talk about.

### FAQ

- **Where do you draw the agent / runtime line?** Runtime observes the agent's state; decides whether to halt. Never decides the next action.
- **Why manual pricing overrides?** Vendor SKUs change faster than billing rollups. Config beats code for things that change at 2 AM.
- **What's next?** Multi-provider cost-quality routing; a regression suite that proves cost-aware doesn't degrade quality.

---

## Deep-Dive #3 — Claude Code / Cursor / MCP at GEICO Enterprise

**Audience:** AI tooling / dev-platform / Cursor / Anthropic interviewers. Bias them toward your enterprise rollout sense.

### One-slide outline

```
Title: Bringing Claude Code, Cursor, and MCP to a 282-person dev-engineering org

  [Claude Code pilot]  --(BRD)-->  [Cursor MCP × Slack bridge]
       |                                       |
       v                                       v
  Claude Agent SDK Slack triage      Cursor cached-token bridge
  AI-powered CI/CD migration engine  -> Claude Code reuses Cursor Slack creds
  Plain-English Claude Code plugin
  AI-consumable artifact-auth ADR

Cross-cutting:
  - MCP server portfolio (JFrog / Slack / ADO / GitHub / Club)
  - Agent skills (solve-case / close-case / build-kb)
  - Security model: derived short-lived tokens, never raw creds
```

### 30-min flow

1. **The org context (3 min):** 282 associates in DE, GEICO's 2026 AI Showcase as the org-wide AI-augmented-work program.
2. **The four AI initiatives (5 min):** Slack triage, CI/CD migration engine, Claude Code plugin, AI-consumable ADR — what each is, who it serves, where each is on the dial.
3. **The MCP bridge BRD (5 min):** the auth-state-collision problem between Cursor and Claude Code, the BRD format you wrote, what the security model is.
4. **The bridge implementation (5 min):** OS-level read with user consent prompt, derived short-lived token, revocation hook. Diagram the data flow.
5. **MCP server portfolio + agent skills (5 min):** which servers, which skills, which workflows they replaced (support, RCA, runbook).
6. **AI-augmented engineering as practice (5 min):** every May 2026 AMP / pkg-mgmt PR authored with Claude Code or Cursor; surgical Slack RCAs end-to-end AI-augmented.
7. **What's next (2 min):** Club skills + Cursor agent hooks; bridge pattern extended to other MCP servers.

### 5-min compact version

> GEICO ran a Claude Code pilot alongside Cursor adoption. The two products had separate enterprise auth state for Slack MCP — that meant double sign-ins and a security review headache. I authored the BRD for a Cursor × Claude Code MCP bridge: Cursor's cached token store is read at the OS level with an explicit user-consent prompt; Claude Code receives a derived short-lived token, never the raw store contents. Around that, we shipped a Claude Agent SDK Slack triage prototype, an AI-powered CI/CD migration engine for the JFrog SaaS cutover, a plain-English Claude Code plugin for Artifactory, and a portfolio of MCP servers + Claude / Cursor agent skills. The pattern — derived tokens with a consent dialog — generalizes to ADO, GitHub, and other MCP server integrations.

### FAQ

- **What was security's objection?** Initially read it as "let Anthropic see your Slack." Walking through the actual data flow (derived token, never the raw store, revocation hooks) turned them into champions.
- **What's been the developer impact?** Single sign-in across both products in the pilot; agent skills automate the highest-friction parts of on-call.
- **What does the marketplace publication look like?** Targeting publication to GEICO's `developer-agent-hub`.

---

## Rehearsal schedule (Month 3 week 1)

- **Day 1:** read all three outlines; speak each one out loud once at full length.
- **Day 2:** record yourself doing each at 30 min. Listen back at 1.5x.
- **Day 3:** do each in 5 min (compact version). This is what HMs ask for.
- **Day 4:** do each on a whiteboard with no notes, in front of a peer. The peer asks 3 FAQ-style questions per deep-dive.
- **Day 5:** rest. Don't rehearse the night before an onsite.

## Onsite-day routine

- Sleep > 7 h two nights before.
- Eat breakfast.
- Open the one-pager, the corresponding deep-dive outline, and `star-stories.md` in tabs.
- Glass of water.
- 15 min before each round, glance at the doc relevant to that round.
- After every round, write 2 bullets — what they asked, what you'd change. Don't re-debate during the day.
- After the last round, send the thank-you note that same evening (template below).

## Thank-you note template

> Hi [Name] — thanks for the time today. The conversation about [one specific topic] was the highlight; I enjoyed sketching the [thing] on the whiteboard and would love to continue the thread on [open question they raised]. I'm at [contact]; happy to follow up however is most useful.
