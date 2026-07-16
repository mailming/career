# Waymo DevAI — Referral-Ready Plan

**Role:** Staff Software Engineer, DevAI — Req **4857** · **Mountain View only** (not SF).

**Why 4857 over 4858:** Same team, same JD responsibilities — Staff bar (8+ yrs, $251K–$310K base) vs Senior Staff (10+ yrs, $298K–$368K). Better match for referral conversion; title aligns with GEICO Staff scope; still clears ~$220K TC floor with bonus/equity.

**Rule:** Do **not** activate the referral until **Gate 1** is checked off. A warm intro that lands a weak HM screen is harder to recover from than waiting one week.

**Target:** Activate referral **Jul 20–21** (after Gate 1) with *"available to screen week of Aug 6"* — uses vacation for Week A prep, not live interviews.

**Surge doc (post-recruiter):** [waymo-devai-surge.md](waymo-devai-surge.md)

**Full 12-week plan:** [waymo-devai-12-week-plan.md](waymo-devai-12-week-plan.md)

---

## What you're interviewing for

You build **developer tools for Waymo's 1,000+ AV engineers** — not the perception/planning stack itself.

| Loop | DevAI mission | Your GEICO anchor |
|------|---------------|-------------------|
| **Inner loop** | Spec → code → test → iterate faster | AI CI/CD migration engine; Claude Code AMP plugin; JFrog SaaS POC workflows |
| **Outer loop** | Automate triage, RCA, eng workflows | Claude Agent SDK `#help-pkg-mgmt` triage bot; MCP + agent skills in prod |
| **Perception debug** | Help engineers root-cause sim failures | OpenClaw eval + cost governance; design agent that queries replay @ timestamp T |

**Frame every answer:** *"I accelerate the humans building the Driver."*

---

## Gate 1 — Referral-ready (complete before asking referrer)

~8–10 hrs total. **Deadline: Jul 20.**

| # | Task | Time | Done |
|---|------|------|------|
| 1 | Read JD + [company-briefs.md § Waymo](study-materials/company-briefs.md) | 45 min | [ ] |
| 2 | Skim [waymo.com](https://waymo.com) "How it works" — sensors, perception outputs, simulation | 30 min | [ ] |
| 3 | Write **spec-driven development** 90-sec answer (ADRs, JFrog POC spec→validation, Claude Code BRD) | 1 hr | [ ] |
| 4 | Write **Why Waymo DevAI** 90-sec answer — record on phone; cut filler | 1 hr | [ ] |
| 5 | Write **inner loop** + **outer loop** 30-sec definitions from memory | 30 min | [ ] |
| 6 | One paragraph: perception debugging agent (scenario ID + timestamp → replay → diff vs ground truth) | 30 min | [ ] |
| 7 | Map 4 STARs with Waymo frame (see surge doc Week B Day 4 table) | 1 hr | [ ] |
| 8 | Tailor resume bullet order: lead with agent platform + reliability, not generic SRE | 30 min | [ ] |
| 9 | Submit **cold application** Req **4857** (MV) yourself first — referral stacks on existing req | 45 min | [ ] |
| 10 | Draft **referrer packet** (below) — send only after rows 1–9 | 30 min | [ ] |

**Gate 1 pass test:** Can you deliver spec-driven + why DevAI + inner/outer loop **without notes** in under 4 minutes total? If not, one more practice round before the referral.

---

## Referrer packet (send Jul 20–21)

**Subject:** DevAI Staff referral — Ming Jia — Req 4857 (MV)

**Message to referrer:**

> Thanks for offering to refer me. Target role: **Staff Software Engineer, DevAI (Req 4857), Mountain View**.
>
> **One-liner:** Staff platform engineer at GEICO — four-nines Artifactory, production Claude Code + MCP rollout for 282-person DE org, OpenClaw cost-aware agent runtime (Purdue).
>
> **Why DevAI:** I've already shipped the inner loop (AI CI/CD migration PRs, Claude Code plugin) and outer loop (Slack triage agent, MCP skills) that this team builds — for AV engineers instead of package-mgmt engineers.
>
> **Logistics:** I'm traveling **07/22–08/05**. Happy to do async steps now; **live screens best week of Aug 6+**. Based in Fremont — **MV on-site works; not a daily SF commute.**
>
> Resume attached. I also applied on the careers site [date] so there's a req in Greenhouse/Lever.

Attach: `resume-ai-infra.md` PDF + [portfolio/one-pager.md](../portfolio/one-pager.md) PDF.

---

## Calendar (Jul 14 → Aug 12)

### Pre-vacation — Gate 1 sprint

| Date | Focus | Career time |
|------|-------|-------------|
| **Jul 14 (Tue)** | Tasks 1–2: JD, brief, Waymo vocabulary | 90 min |
| **Jul 15 (Wed)** | Tasks 3–5: spec-driven + why DevAI + inner/outer (record) | 90 min |
| **Jul 16 (Thu)** | Task 6–7: perception paragraph + STAR Waymo frames | 90 min |
| **Jul 17 (Fri)** | Task 8–9: resume + **apply Req 4857 (MV)** | 90 min |
| **Jul 18 (Sat)** | Task 10 prep; 1 LC problem | 2 hr |
| **Jul 19 (Sun)** | Gate 1 pass test; fix weak answers | 45 min |
| **Jul 20–21** | **Activate referral** if Gate 1 passes | 30 min |

**Parallel (lower priority):** Figure Agentic Systems submit — does not block Waymo referral.

**Pause:** New applications to other companies until referral is out (avoid split attention).

### Vacation — Week A lite (no live screens)

| Week | Allowed | Skip |
|------|---------|------|
| Jul 22 – Aug 5 | 2–3 LC/week; re-record 90-sec answers; read Braintrust evals + Promptfoo quickstart (1 hr total); optional 2-hr RAG mini-hack on SmartTuna or AMP ADR corpus | Live recruiter/HM calls; Isaac Lab; other company apps |

**Week A lite checklist:**

- [ ] Re-read [04-eval-pipelines.md](system-design/04-eval-pipelines.md) + Braintrust "What is an eval?" (30 min)
- [ ] 2 GEICO triage-bot eval scenarios written (golden set + PR regression) — surge Week A Day 6–7
- [ ] Optional: minimal RAG (ChromaDB + 50 lines) — strong HM differentiator if done

### Post-vacation — Recruiter week + Week B

| Date | Focus |
|------|-------|
| **Aug 6–8** | Recruiter screens; rehearse [phone-screen-playbook.md](phone-screen-playbook.md) Waymo lines |
| **Aug 9–12** | Week B Days 1–3: Inner Loop design, Outer Loop RCA design, Perception debug design (45 min each, out loud) |
| **Before HM** | Full [waymo-devai-surge.md](waymo-devai-surge.md) Week B |

---

## Interview surface map (study in this order)

| Priority | Round | Prep asset |
|----------|-------|------------|
| P0 | HM: "vision for AI-assisted SDLC?" | Why DevAI + GEICO 4 AI initiatives STAR |
| P0 | Behavioral: cross-team adoption | Cursor × Claude Code MCP bridge STAR |
| P0 | Behavioral: reliability at scale | Artifactory four-nines STAR |
| P1 | System design: inner loop (spec → code → test) | [03-agent-orchestration.md](system-design/03-agent-orchestration.md) + surge Week B Day 1 |
| P1 | System design: outer loop RCA OR eval pipeline | [04-eval-pipelines.md](system-design/04-eval-pipelines.md) + surge Week B Day 2 |
| P2 | Domain: perception debugging agent | surge Week B Day 3 |
| P2 | Coding: Python agent/tool scenario | LC medium + Claude Agent SDK patterns |

**Do not study:** GPU autoscaling (doc 06), distributed training (doc 05), AV sensor fusion / SLAM.

---

## Recruiter / HM scripts

**Why Waymo DevAI (90 sec skeleton):**

1. Mission: DevAI lets AV engineers ship faster — same problem I've been solving for GEICO's 282-person DE org.
2. Angle: Simulation + perception debugging is a massive, safety-critical surface; tooling here has direct downstream impact on the Driver.
3. Proof: Shipped Claude triage bot (outer loop), AI CI/CD migration engine (inner loop), MCP bridge (adoption) — production, not demos.
4. Vision: Spec-driven dev + multi-agent outer loops can compress weeks to hours; AV is the hardest place to prove it.

**Location:**

> Fremont-based. MV hybrid works. Remote US works. I can't do a regular SF office commute.

**Availability:**

> Traveling 07/22–08/05. Async now; live screens week of Aug 6 onward.

---

## What "wasting a referral" looks like — avoid these

| Mistake | Fix |
|---------|-----|
| Referral before you can explain inner/outer loop | Complete Gate 1 first |
| Referral to wrong req or SF-primary listing | Req **4857**, MV explicitly |
| Referrer has no talking points | Send one-liner + why DevAI in referral packet |
| Accept recruiter screen mid-vacation unprepared | Defer to Aug 6+ in referral message |
| Pitch yourself as AV/perception engineer | DevTools-for-engineers frame only |
| No cold app in system | Apply yourself before referral (stacks cleanly) |

---

## Success metrics

| Milestone | Target date |
|-----------|-------------|
| Gate 1 complete | Jul 20 |
| Referral sent | Jul 21 |
| Recruiter screen | Aug 6–12 |
| HM screen | Aug 13–20 |
| Technical screens | Aug 20+ |

Log all activity in [target-companies.md](../target-companies.md) application table.
