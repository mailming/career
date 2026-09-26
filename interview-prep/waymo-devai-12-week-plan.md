# Waymo DevAI (Req 4857) — 12-Week Prep Plan

**Role:** Staff Software Engineer, DevAI · Req **4857** · Mountain View (not SF).

**Start:** 2026-07-14 · **End:** 2026-10-05

**Budget:** 12–14 hrs/week (vacation weeks 2–3: 4–6 hrs). Interviews **replace** study — never double-book.

**Companion docs:**
- [waymo-devai-referral-plan.md](waymo-devai-referral-plan.md) — Gate 1 + referral timing
- [waymo-devai-surge.md](waymo-devai-surge.md) — 2-week intensive once screens are booked
- [company-briefs.md § Waymo](study-materials/company-briefs.md)
- [phone-screen-playbook.md](phone-screen-playbook.md)

**Frame every answer:** *"I accelerate the humans building the Driver."*

---

## Phase map

| Phase | Weeks | Dates | Goal |
|-------|-------|-------|------|
| **0 — Referral ready** | 1 | Jul 14–20 | Gate 1, apply 4857, send referral |
| **1 — Vacation vocab** | 2–3 | Jul 21 – Aug 3 | LC + eval/RAG vocabulary; no live screens |
| **2 — Screens + core designs** | 4–5 | Aug 4–17 | Recruiter/HM; Inner + Outer Loop designs cold |
| **3 — Technical depth** | 6–7 | Aug 18–31 | Perception debug design; coding ramp; mocks |
| **4 — Onsite readiness** | 8–9 | Sep 1–14 | Full loop simulation; portfolio artifact |
| **5 — Polish + buffer** | 10–12 | Sep 15 – Oct 5 | Behavioral Staff bar; gap-fill; rest before onsite |

**LC target (12 weeks):** 36–40 problems total (~3/week). Log every one in [coding-log.md](coding-log.md).

**System designs to own (Waymo-specific):**
1. Inner Loop — spec → code → test → iterate ([03-agent-orchestration.md](system-design/03-agent-orchestration.md))
2. Outer Loop — RCA agent OR eval pipeline ([04-eval-pipelines.md](system-design/04-eval-pipelines.md))
3. Perception debugging agent (surge Week B Day 3 — unique to Waymo)

**Do not study:** docs 05, 06 (training/GPU); AV sensor fusion / SLAM.

---

## Standard week template (non-vacation, non-onsite)

| Day | Block (45–60 min) | Exercise |
|-----|-------------------|----------|
| **Mon** | This week's theme reading OR recruiter follow-up | Walk |
| **Tue** | 1 LC problem (Python-friendly) | Gym |
| **Wed** | System design rehearse (out loud, timed) | Walk |
| **Thu** | 1 LC problem | Gym |
| **Fri** | STAR story out loud (1–2) | Walk |
| **Sat** | **Deep work 2 hr** — build, mock, or design deliverable | Family AM |
| **Sun** | 45 min review; set next week's ONE priority | Family |

**If a live interview lands that week:** drop Wed design OR Sat deep work — keep Tue/Thu LC and Fri STAR.

---

## Week-by-week plan

### Week 1 — Gate 1: Referral ready (Jul 14–20) · ~10 hrs

**Milestone:** Referral sent Jul 20–21. Req 4857 applied.

| Deliverable | Resource | Done |
|-------------|----------|------|
| Read JD + company brief + waymo.com "How it works" | [company-briefs § Waymo](study-materials/company-briefs.md) | [ ] |
| Write + record: spec-driven 90 sec, Why DevAI 90 sec, inner/outer 30 sec each | [referral-plan Gate 1](waymo-devai-referral-plan.md) | [ ] |
| Perception-debug paragraph (replay @ T → diff ground truth) | surge Week A Day 3 | [ ] |
| Map 4 STARs with Waymo frame | surge Week B Day 4 table | [ ] |
| Tailor resume; **apply Req 4857 (MV)** | [resume-ai-infra.md](../resume-ai-infra.md) | [ ] |
| **Send referral** Jul 20–21 | referrer packet in referral-plan | [ ] |
| 2 LC (warm-up) | arrays, hash map | [ ] |
| LinkedIn locations updated | [linkedin-rewrite.md](../linkedin-rewrite.md) | [ ] |

**Gate 1 pass test:** 4 min cold — spec-driven + why DevAI + inner + outer, no notes.

---

### Week 2 — Vacation A: Eval + spec vocabulary (Jul 21–27) · ~5 hrs

**Milestone:** Referral in flight. Recruiter may email async — reply with Aug 6+ for live calls.

| Deliverable | Resource | Done |
|-------------|----------|------|
| Braintrust "What is an eval?" (30 min) | braintrust.dev/docs | [ ] |
| Promptfoo quickstart (20 min) | promptfoo.dev | [ ] |
| Re-read [04-eval-pipelines.md](system-design/04-eval-pipelines.md) | highlight golden-set + PR regression | [ ] |
| Write 2 eval scenarios for GEICO triage bot | surge Week A Day 6–7 | [ ] |
| Re-record spec-driven + Why DevAI (cut filler) | phone voice memo | [ ] |
| 2 LC | medium | [ ] |
| **Optional Sat:** start RAG mini-hack (ChromaDB + ADR corpus or SmartTuna) | 2 hr if energy | [ ] |

---

### Week 3 — Vacation B: Waymo context + STARs (Jul 28 – Aug 3) · ~5 hrs

**Milestone:** Can explain perception-debug agent in 60 sec. 6 STARs skimmed.

| Deliverable | Resource | Done |
|-------------|----------|------|
| Skim [Waymo Research blog](https://waymo.com/research/) — simulation / ML pipeline posts (45 min) | 2 posts max | [ ] |
| Read Copilot Workspace spec approach (30 min) | githubnext.com/projects/copilot-workspace | [ ] |
| Polish perception-debug design paragraph | surge Week B Day 3 frame | [ ] |
| Read aloud STARs **6, 7, 8** (JFrog POC, MCP bridge, OpenClaw) | [star-stories.md](star-stories.md) | [ ] |
| 2 LC | BFS or topological sort | [ ] |
| Finish RAG mini-hack if started | 1 STAR bullet ready | [ ] |

---

### Week 4 — Recruiter screens + Inner Loop design (Aug 4–10) · ~12 hrs

**Milestone:** Recruiter screen done. Inner Loop design deliverable in 10 min cold.

| Deliverable | Resource | Done |
|-------------|----------|------|
| Recruiter screen(s) — scripts from [phone-screen-playbook](phone-screen-playbook.md) | log in target-companies | [ ] |
| Study [03-agent-orchestration.md](system-design/03-agent-orchestration.md) | full read | [ ] |
| **Sat 2 hr:** rehearse Inner Loop design out loud (timed 10 min) | surge Week B Day 1 prompt | [ ] |
| Components checklist: spec ingestion, test-gen agent, sandbox, iteration controller, codebase RAG, eval harness, traces | written outline | [ ] |
| Add **safety / failure-mode** section to Inner Loop outline | Waymo culture signal | [ ] |
| 3 LC | heap, two pointers, graph | [ ] |
| STAR **#7 MCP bridge** — full 2 min with Waymo adoption frame | | [ ] |

**Inner Loop prompt:** *"Design a multi-agent system that helps Waymo engineers write and test code faster from a natural-language spec."*

---

### Week 5 — HM screen + Outer Loop design (Aug 11–17) · ~12 hrs

**Milestone:** HM screen done. Outer Loop OR eval pipeline in 10 min cold.

| Deliverable | Resource | Done |
|-------------|----------|------|
| HM screen prep — "vision for AI-assisted SDLC?" | GEICO 4-initiative STAR + Why DevAI | [ ] |
| **Sat 2 hr:** rehearse Outer Loop RCA design | surge Week B Day 2 prompt | [ ] |
| Alt Sat session: deliver [04-eval-pipelines.md](system-design/04-eval-pipelines.md) as 10-min talk | per-PR regression focus | [ ] |
| RAG story — 2 sentences ready (built or planned) | Week 2–3 hack | [ ] |
| 3 LC | trees, dynamic programming (1 easy) | [ ] |
| STAR **#1 Artifactory four-nines** + Waymo reliability frame | 1,000+ engineers blocked if DevAI is down | [ ] |
| Read 2 Waymo engineering blog posts | recent only | [ ] |

**Outer Loop prompt:** *"Design an RCA agent for simulation regressions — triage, hypothesize, verify, output diagnosis or fix PR."*

---

### Week 6 — Perception debug + technical prep (Aug 18–24) · ~14 hrs

**Milestone:** All 3 Waymo-specific designs outlined. First self-mock recorded.

| Deliverable | Resource | Done |
|-------------|----------|------|
| **Sat 2 hr:** Perception debugging agent design cold | surge Week B Day 3 | [ ] |
| Technical screen likely — confirm format with recruiter | coding vs design | [ ] |
| Python agent patterns review | Claude Agent SDK tool-use, state, error handling | [ ] |
| 4 LC | emphasis Python: dict/graph, queue, binary search | [ ] |
| Self-record: Inner Loop 10 min → watch back → note 3 fixes | [mock-interviews.md](mock-interviews.md) | [ ] |
| STAR **#6 JFrog SaaS POC** — spec-driven live example | | [ ] |
| Write "Why Waymo DevAI" final script — 90 sec memorized | surge Week B Day 5 | [ ] |

**Perception prompt:** *"Design an agent to debug a missed pedestrian at T=12.3s in simulation."*

---

### Week 7 — Coding ramp + hostile mock (Aug 25–31) · ~14 hrs

**Milestone:** Answer 4 hostile design questions fluently. 20+ LC total logged.

| Deliverable | Resource | Done |
|-------------|----------|------|
| Hostile mock questions (self-ask or partner) | surge Week B Day 6 list | [ ] |
| — "Code passes tests but violates safety invariant?" | | [ ] |
| — "Spec is ambiguous?" | | [ ] |
| — "How measure if Inner Loop actually makes engineers faster?" | | [ ] |
| — "LLM judge is wrong?" | | [ ] |
| 4 LC | medium; 1 timed 45 min | [ ] |
| Rehearse all 3 designs back-to-back (30 min each) | Sat | [ ] |
| STAR **#8 OpenClaw** — eval + cost governance → DevAI eval strategy | | [ ] |
| Technical screen(s) if scheduled | | [ ] |

---

### Week 8 — Portfolio + onsite block 1 (Sep 1–7) · ~14 hrs

**Milestone:** One public artifact live (blog OR RAG demo). Simulated 3-round day.

| Deliverable | Resource | Done |
|-------------|----------|------|
| **Publish** OpenClaw blog OR RAG demo video/GIF | [portfolio/blog-openclaw-cost-aware-runtime.md](../portfolio/blog-openclaw-cost-aware-runtime.md) | [ ] |
| Pin to LinkedIn Featured | | [ ] |
| **Sat 3 hr onsite sim:** 45 min coding + 45 min Inner Loop + 45 min behavioral | log gaps | [ ] |
| 3 LC | maintenance | [ ] |
| Re-read full [company-briefs § Waymo](study-materials/company-briefs.md) | | [ ] |
| Staff-scope language pass on all STARs | "across interdependent teams" | [ ] |

---

### Week 9 — Mock week (Sep 8–14) · ~14 hrs

**Milestone:** Partner mock OR 2 self-recorded full loops. Gap list written.

| Deliverable | Resource | Done |
|-------------|----------|------|
| Mock #1: HM + "vision for AI-assisted SDLC" | [mock-interviews.md](mock-interviews.md) | [ ] |
| Mock #2: System design — Outer Loop or eval pipeline | | [ ] |
| Fix top 3 gaps from mocks | update outlines | [ ] |
| 3 LC | | [ ] |
| STAR **#10 disagreement / mistake** — Staff ownership | | [ ] |
| Onsite scheduling / travel plan for MV | Fremont → MV hybrid | [ ] |

---

### Week 10 — Behavioral depth (Sep 15–21) · ~12 hrs

**Milestone:** 6 STARs at 2 min each without notes. Adoption story sharp.

| Deliverable | Resource | Done |
|-------------|----------|------|
| Daily Fri-style: 2 STARs out loud | rotate 1–8 | [ ] |
| **Cross-team adoption** deep prep | STAR #7 + GEICO 282-person rollout | [ ] |
| "Biggest failure" / "disagreement with senior stakeholder" | STAR #10, #2 NOCIM | [ ] |
| 3 LC | | [ ] |
| **Sat:** Perception design + safety section — final polish | | [ ] |
| Questions to ask HM/interviewers (5 prepared) | team roadmap, adoption metrics, eval strategy | [ ] |

---

### Week 11 — Full onsite simulation (Sep 22–28) · ~14 hrs

**Milestone:** Full 5–6 round day simulated. Night-before checklist done once.

| Deliverable | Resource | Done |
|-------------|----------|------|
| **Sat 4–5 hr full loop sim:** | surge Week B Day 7 checklist | [ ] |
| Round 1: Coding (Python, agent-adjacent) | | [ ] |
| Round 2: Inner Loop design | | [ ] |
| Round 3: Outer Loop or eval pipeline | | [ ] |
| Round 4: Perception debug design | | [ ] |
| Round 5: Behavioral ×2 (adoption + reliability) | | [ ] |
| Run surge **night-before checklist** as dry run | | [ ] |
| 2 LC | light — don't burn out | [ ] |
| Onsite date confirmed OR virtual loop scheduled | | [ ] |

---

### Week 12 — Buffer + polish (Sep 29 – Oct 5) · ~8–10 hrs

**Milestone:** Rested, sharp, no new material. Adjust from real interview feedback.

| Deliverable | Resource | Done |
|-------------|----------|------|
| Re-read JD — pull 3 phrases verbatim for "why this role" | | [ ] |
| 4 polished STARs only (don't cram new ones) | #1, #6, #7, #8 | [ ] |
| 3 designs — 5 min skim each (outline only) | | [ ] |
| 2 LC | confidence maintenance | [ ] |
| **If onsite this week:** Mon–Wed light; sleep ≥7 hr; no new LC Thu–Fri | | [ ] |
| **If no onsite yet:** use week for gap-fill from recruiter feedback | | [ ] |
| Log conversion metrics | screen→tech→onsite | [ ] |

---

## LC focus by topic (Waymo-relevant)

Prioritize **Python**, practical patterns over competitive programming tricks.

| Weeks | Topics | Why |
|-------|--------|-----|
| 1–3 | Arrays, hash map, two pointers, BFS | Warm-up; parsing logs / graphs |
| 4–6 | Heap, trees, topological sort, binary search | Scheduling, dependencies |
| 7–9 | Graph (shortest path), DP (1D), intervals | RCA / timeline reasoning |
| 10–12 | Mixed medium timed sets | Maintenance |

**Agent-adjacent coding prep:** practice implementing a simple tool-calling loop, retry with backoff, and parsing JSON tool outputs in Python — 1 hr in Week 6 Sat.

---

## Behavioral — core 6 for Waymo DevAI

| Priority | STAR | Waymo angle |
|----------|------|-------------|
| P0 | #7 Cursor × MCP bridge | Cross-team adoption of novel AI tooling |
| P0 | #1 Artifactory four-nines | DevAI tools are critical path for 1,000+ engineers |
| P0 | #6 JFrog SaaS POC | Spec-driven development in production |
| P0 | #8 OpenClaw cost-aware runtime | Eval + governance for agent systems |
| P1 | GEICO 4 AI initiatives (combine #6,#7 + showcase) | Inner loop + outer loop — already shipped |
| P1 | #10 disagreement / mistake | Staff scope, safety culture |

---

## When interviews start — priority rules

1. **Recruiter/HM booked** → run [surge Week A](waymo-devai-surge.md) compressed into 3 days before that screen.
2. **Technical booked** → surge Week B + drop LC to 1/week that week.
3. **Onsite booked** → Week 11 simulation moves up; Week 12 becomes rest-only.
4. **Rejected** → log gap in [mock-interviews.md](mock-interviews.md); one week targeted fix; resume parallel Bay Area apps.

---

## Weekly checkpoint (Sundays, 15 min)

```markdown
## Week N — Waymo prep

**One priority for next week:**
**Interviews this week:**
**LC count (cumulative):**
**Designs rehearsed (1/2/3):**
**STARs practiced:**
**Weakest area:**
**Vacation / life override?**
```

---

## Success timeline (adjust when recruiter confirms)

| Milestone | Target | Actual |
|-----------|--------|--------|
| Gate 1 + referral | Jul 20–21 | |
| Recruiter screen | Aug 6–12 | |
| HM screen | Aug 13–20 | |
| Technical round 1 | Aug 20 – Sep 5 | |
| Technical round 2 / onsite | Sep 5 – Oct 5 | |
| Offer | Oct+ | |

Log everything in [target-companies.md](../target-companies.md).
