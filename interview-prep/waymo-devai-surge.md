# Waymo DevAI — Pre-Interview Surge Plan

**Use when:** recruiter screen is booked or imminent. Slot this on top of your existing 5-month plan — it replaces (not adds to) the "system design" and "behavioral" blocks for those 2 weeks.

**Audience reminder:** you're interviewing to build *developer tools for Waymo's engineers*, not to build the autonomous vehicle. Keep every answer in that frame.

---

## Week A — Before Recruiter / HM Screen

**Goal:** be fluent in Waymo's vocabulary, your hook, and the three known gaps.

### Day 1–2: Close the Spec-Driven Development gap
- Read: [Copilot Workspace spec approach](https://githubnext.com/projects/copilot-workspace) — how GitHub Next uses a natural-language spec to drive code generation. Understand the loop: spec → plan → implementation → verification.
- Read: one of [TLA+ intro](https://lamport.azurewebsites.net/tla/tla.html) (skim for concepts, not formalism) OR the "spec-first API design" section from any modern API design guide.
- **Map to your work:** write 3 bullets connecting your existing work to spec-driven development:
  - Your AI-consumable ADRs = machine-readable specs for artifact auth
  - JFrog SaaS POC workflows = spec (package type matrix) → automated validation → pass/fail signal
  - Claude Code plugin BRD = the spec contract that drove implementation
- Practice the 90-second answer out loud. Record it.

### Day 3: Perception debugging context (30-min read, not deep study)
- Read "How Waymo's self-driving technology works" on waymo.com — skim for: what sensors (lidar, camera, radar), what the perception pipeline outputs (bounding boxes, object classifications, predicted trajectories), what simulation replay is.
- Write 1 paragraph in your own words: "If an engineer notices the Waymo Driver missed a pedestrian in a specific simulation run, what would a debugging agent need to do?" Answer: query the replay at that timestamp → extract perception outputs → compare to ground truth labels → surface the delta. That's your "perception debugging agent" design in 3 steps.

### Day 4–5: Strengthen RAG story
- Spend 2 hrs adding a minimal RAG component to SmartTuna or the Claude Code AMP plugin:
  - Option A (SmartTuna): add a codebase/earnings-doc search tool using ChromaDB + text-embedding. Even 50 lines of Python counts.
  - Option B (AMP plugin): add a RAG lookup against the JFrog docs or your AI-consumable ADR corpus.
- After building it, write one STAR bullet: "Built a RAG layer for [X] using [embedding model] + [vector store]; [result]."

### Day 6–7: LLM eval vocabulary
- Read [Braintrust "What is an eval?" docs](https://www.braintrust.dev/docs/guides/evals) (30 min) — covers LLM-as-judge, golden datasets, scoring functions.
- Read [Promptfoo quickstart](https://www.promptfoo.dev/docs/getting-started/) (20 min) — practitioner angle on prompt regression testing.
- Review your existing [system-design/04-eval-pipelines.md](system-design/04-eval-pipelines.md) — you already have the system design; now you have the vocabulary to go deeper.
- Write 2 concrete eval scenarios you'd run for the GEICO Claude Agent triage bot:
  - Golden dataset eval: 50 sample help-channel tickets with expected routing decisions → LLM-as-judge scores routing accuracy.
  - Regression eval on PR: any prompt change triggers the eval suite; alert if accuracy drops > 2%.

---

## Week B — Before Technical Screens / Onsite

**Goal:** deliver two system designs cold, polish 4 STAR stories, build the "why Waymo DevAI" answer.

### Day 1: System design — Inner Loop (developer code acceleration)
**Design prompt to practice:** *"Design a multi-agent system that helps Waymo engineers write and test code faster. Engineers write a spec in natural language; the system generates candidate implementations, runs tests, and iterates until the spec is satisfied."*

Key components to cover:
- Spec ingestion (natural language → structured spec → code generation agent)
- Test-generation agent (derive test cases from the spec before writing code — TDD loop)
- Execution sandbox (safe, reproducible code execution with resource limits)
- Iteration controller (re-prompt on test failure; budget: max N iterations)
- Codebase RAG (retrieve relevant existing code as context for generation)
- Eval harness (did the final output actually satisfy the spec? LLM-as-judge + test pass rate)
- Observability (Langfuse-style traces per spec run)

Practice delivering this in 10 min cold. Use your [system-design/03-agent-orchestration.md](system-design/03-agent-orchestration.md) as the infrastructure layer — don't re-explain the plumbing, cite it and go deeper on the SDLC-specific layer.

### Day 2: System design — Outer Loop (root cause analysis agent)
**Design prompt to practice:** *"Design an automated root cause analysis agent for Waymo's CI/CD pipeline. When a regression is detected in simulation, the agent should automatically triage, identify the likely cause, and open a PR with a fix or diagnosis report."*

Key components:
- Trigger: regression alert from eval pipeline → RCA agent invoked
- Context retrieval: pull recent commits, diff, simulation logs, failing scenario metadata (RAG over logs)
- Hypothesis generation: LLM generates 3–5 candidate root causes ranked by likelihood
- Verification loop: per hypothesis, agent runs targeted sub-simulation or log query to validate
- Output: structured diagnosis report + optional fix PR
- Human-in-the-loop gate: high-confidence auto-PR vs. needs-human-review routing
- Reliability: idempotent, auditable, no silent failures (Waymo safety culture)

### Day 3: Perception debugging agent design
**Design prompt:** *"Design a specialized agent for debugging perception failures in the Waymo Driver."*

Frame (from your Day 3 Week A research):
- Input: scenario ID + timestamp + reported failure type (e.g., "missed pedestrian at T=12.3s")
- Agent tools: query simulation replay API, query ground-truth label store, diff perception output vs. ground truth, search similar historical failures (RAG over failure database)
- Output: ranked hypotheses (sensor occlusion? model edge case? data distribution shift?) + links to similar resolved incidents
- Eval: did the agent's top hypothesis match the human engineer's eventual diagnosis? Track precision@1.

This round is unique to Waymo — no other company will ask this. If you can design it fluently, it signals deep reading of the JD.

### Day 4: STAR story polish for Waymo specifically

For each story, add a Waymo-framing sentence — what would the equivalent situation look like at Waymo DevAI?

| Story | Waymo frame to add |
|-------|-------------------|
| GEICO AI Showcase portfolio (4 initiatives) | "At Waymo DevAI this would be exactly the inner loop + outer loop mission — I've already built and shipped the pattern" |
| Claude Agent SDK triage prototype | "This is the outer-loop triage automation Waymo's JD describes; I have production evidence, not a demo" |
| Cursor × Claude Code MCP bridge | "Cross-team adoption of novel AI tooling is a stated requirement for this role; here's how I've done it" |
| Artifactory four-nines | "Waymo DevAI tools will be critical path for 1,000+ engineers; reliability ownership is what I bring from the Artifactory turnaround" |

### Day 5: "Why Waymo DevAI" answer — write and record
Draft a 90-second answer. Required elements:
1. The mission resonance: "Waymo's DevAI team is building the internal platform that lets AV engineers ship faster — that's exactly the problem I've been attacking at GEICO."
2. The specific angle: "The perception-debugging and simulation-RCA use cases are uniquely hard because the debugging surface is massive and the failure modes are safety-critical — I want to work on problems where the tooling I build has direct downstream impact on the safety of the Driver."
3. The credibility anchor: name 1 concrete thing from your background that directly maps (the Claude Agent SDK triage bot, the AI-powered CI/CD migration engine, or the MCP bridge).
4. The vision: "I believe spec-driven development + multi-agent outer loops will compress weeks of engineering cycle time to hours — and the autonomous driving domain is the hardest, most impactful place to prove that."

Record it. Cut to 90 seconds. No filler words.

### Day 6: Mock — system design with a hostile interviewer
Ask a partner to run the Inner Loop design (Day 1 prompt). Partner role: push hard on:
- "What happens when the generated code passes tests but violates a safety invariant?"
- "How do you prevent the spec from being ambiguous?"
- "How do you measure whether the Inner Loop tool actually makes engineers faster?"
- "Your eval judge is an LLM — what if the judge itself is wrong?"

Log in [mock-interviews.md](mock-interviews.md).

### Day 7: Night-before-screen checklist
- Re-read [company-briefs.md § Waymo](study-materials/company-briefs.md) in full
- Re-read the JD one more time; pull 3 phrases verbatim for your "why this role" answer
- Review your 4 polished STAR stories with Waymo frames
- Confirm your RAG story (Week A Day 4–5) is 2 sentences ready
- Confirm your spec-driven development 90-second answer is memorized
- Sleep ≥ 7 hours

---

## Quick-reference: Waymo interview surface map

| Round | Most likely prompt | Your anchor story | Key design doc |
|-------|-------------------|------------------|----------------|
| HM screen | "What's your vision for AI-assisted SDLC?" | GEICO 4 AI initiatives | — |
| Coding | Python; practical agent/tool scenario | Live code, Claude Agent SDK patterns | — |
| System design #1 | Inner loop: spec-driven code gen | OpenClaw cost-aware runtime pattern | doc 03 (agent orch) |
| System design #2 | Outer loop: RCA agent OR eval pipeline | SmartTuna + GEICO triage bot | doc 04 (evals) |
| Domain design | Perception debugging agent | Week B Day 3 prep | — |
| Behavioral | Cross-team adoption, disagreement, biggest failure | Cursor × MCP bridge, NOCIM-11695, AMP turnaround | star-stories.md |

---

## What NOT to study for Waymo (save time)

- GPU autoscaling internals (doc 06) — not the DevAI surface
- Distributed training orchestration (doc 05) — not the DevAI surface
- AV sensor fusion / SLAM / planning algorithms — you're building *for* those engineers, not joining them
- TypeScript / Rust — Waymo DevAI is Python + Go
