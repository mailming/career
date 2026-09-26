# TODAY — Sun Aug 9, 2026 · Week B Day 1 + Sunday Review

**Where you are:** Week 4 of [waymo-devai-12-week-plan.md](../waymo-devai-12-week-plan.md) (Aug 4–10). Post-vacation. Recruiter-screen window (Aug 6–12). Today starts **Week B system designs** per [waymo-devai-referral-plan.md](../waymo-devai-referral-plan.md).

**Today's ONE priority:** Read agent orchestration patterns → draft **Inner Loop** design outline → 45 min Sunday review.

**Frame (say once before any rehearsal):**  
*"I accelerate the humans building the Driver — I build tools for Waymo's engineers, not the Driver itself."*

**Total time:** ~90 min career (family day — keep it light; no 2-hr Sat block today).

---

## Block 0 — Sunday review (15 min)

Copy into [weekly-log.md](../../weekly-log.md) or a note:

```markdown
## Week of 2026-08-04

**One priority for next week:** Inner Loop design cold in 10 min (Sat Aug 16 deep work)
**Interviews this week:** Recruiter screen? (Y/N) ___  HM scheduled? (Y/N) ___
**LC count (cumulative):** ___
**Designs rehearsed:** Inner ___ / Outer ___ / Perception ___
**STARs practiced:** ___
**Weakest area:** ___
**Vacation / life override?** ___
```

**Set next week's ONE priority:** *"Deliver Inner Loop design out loud in 10 min by Sat Aug 16."*

---

## Block 1 — Read: How agents communicate (30 min)

**File:** [agentic-workflows-how-agents-communicate.md](agentic-workflows-how-agents-communicate.md)

Read in this order (do not binge the whole doc):

| Section | Time | Why today |
|---------|------|-----------|
| §1 The one idea (orchestration / state / tools) | 5 min | Mental model for any design |
| §2 Pattern A Supervisor + Workers | 5 min | Triage bot, adoption story |
| §2 **Pattern C Pipeline** | 10 min | **Inner Loop = fixed spec → code → test → review** |
| §3 What gets passed (typed artifacts) | 5 min | Production rule for Waymo |
| §5 Map to YOUR projects (Inner Loop row) | 5 min | Interview bridge |

**Optional external (10 min if energy):** Anthropic [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) — workflows vs agents section only.

**Done when:** You can say without notes: *"Inner Loop is mostly **Pattern C pipeline** with a **supervisor** on iteration — spec agent → codegen → test → review, loop until spec satisfied or budget hit."*

---

## Block 2 — Read: Platform layer (20 min)

**File:** [03-agent-orchestration.md](../system-design/03-agent-orchestration.md)

Skim — do not memorize scale numbers today:

| Section | Focus |
|---------|--------|
| §3 Run model | State snapshot after every step; resume = load + continue |
| §4 Budgets | OpenClaw hook — max steps, cost, policy at step boundaries |
| §6 Sub-agents | Parent/child budget; depth limit |
| §7 Versioning + evals | Eval harness + trace-replay for regressions |
| §13 Lines that land | Pick 2 to steal for Inner Loop |

**Rule for interviews:** Cite this as *infrastructure* ("durable state, budgets, traces — same shape as OpenClaw"). Spend your 10 min on the **SDLC-specific** layer below.

---

## Block 3 — Write: Inner Loop outline (25 min)

**Prompt (from [waymo-devai-surge.md](../waymo-devai-surge.md) Week B Day 1):**

> *"Design a multi-agent system that helps Waymo engineers write and test code faster. Engineers write a spec in natural language; the system generates candidate implementations, runs tests, and iterates until the spec is satisfied."*

Fill this outline (bullets only — no essay):

```
1. SPEC INGESTION
   - NL spec → structured spec (JSON schema / ADR-like)
   - Your GEICO anchor: ___

2. TEST-GEN AGENT (TDD before code)
   - Derive test cases from spec first
   - ___

3. CODE-GEN AGENT
   - Candidate implementation + codebase RAG context
   - Your GEICO anchor: AI CI/CD migration / Claude Code plugin

4. EXECUTION SANDBOX
   - Isolated, resource limits, reproducible
   - ___

5. ITERATION CONTROLLER
   - On test fail → re-prompt with failure context
   - Max N iterations; budget halt (OpenClaw pattern)
   - Pattern: pipeline + supervisor on the loop edge

6. EVAL HARNESS
   - Tests pass AND spec satisfied (LLM-as-judge + pass rate)
   - PR regression: new agent version must beat baseline
   - ___

7. OBSERVABILITY
   - Langfuse-style trace per spec run
   - ___

8. SAFETY / FAILURE MODES (Waymo signal)
   - Code passes tests but violates safety invariant → ___
   - Ambiguous spec → human gate
   - Agent loops → step budget server-side
```

**GEICO anchors to weave in:**
- JFrog SaaS POC = spec → automated validation → pass/fail
- AI CI/CD migration = pipeline opening per-team PRs
- Claude Code BRD = spec contract that drove implementation

---

## Block 4 — Speak: 5-min cold run (10 min)

Close all tabs. Set timer **5 min** (not 10 — Sunday lite).

Deliver aloud:
1. Problem (30 sec) — DevAI inner loop for 1,000+ AV engineers
2. Architecture (3 min) — walk your 8-section outline
3. One GEICO proof (1 min)
4. One safety/failure mode (30 sec)

| Attempt | Time | Gap |
|---------|------|-----|
| 1 | ___ min | |

**Do not** record full 10 min today — that's **Sat Aug 16** deep work per 12-week plan.

---

## What NOT to read today

| Skip | When |
|------|------|
| Outer Loop / RCA design | Mon Aug 10 (Week B Day 2) |
| Perception debug design | Tue Aug 11 (Week B Day 3) |
| Docs 05, 06 (training/GPU) | Not DevAI surface |
| AV sensor fusion / SLAM | Wrong lane |
| Full 04-eval-pipelines.md | Read Thu if doing Outer Loop alt |

---

## Optional — if you have 30 extra min

- **LC:** 1 medium (heap or graph) → [coding-log.md](../coding-log.md)
- **STAR #7** MCP bridge — 2 min out loud with Waymo adoption frame
- Re-read [company-briefs.md § Waymo](company-briefs.md) — 15 min skim

---

## Week ahead (preview)

| Day | Focus |
|-----|--------|
| **Mon Aug 10** | Outer Loop RCA design — read surge Week B Day 2 + [04-eval-pipelines.md](../system-design/04-eval-pipelines.md) |
| **Tue Aug 11** | Perception debug design — surge Week B Day 3 + Gate 1 perception paragraph |
| **Wed Aug 12** | Rehearse all 3 designs; recruiter follow-up |
| **Sat Aug 16** | **2 hr:** Inner Loop 10 min cold + safety section written |

---

## Done-when checklist (tonight)

- [ ] Sunday review filled (15 min)
- [ ] Can explain Pattern C pipeline + supervisor loop for Inner Loop
- [ ] Inner Loop 8-section outline written with ≥2 GEICO anchors
- [ ] One 5-min cold delivery attempted
- [ ] Next week's ONE priority set
