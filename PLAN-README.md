# AI Infra Job Plan — Workspace Index

Implementation of the plan at `c:\Users\USER\.cursor\plans\ai_infra_job_plan_2a48b049.plan.md`. Everything below is ready-to-use; nothing requires me to be in the loop to execute.

## Top-level docs

| File | Purpose | When to use |
|------|---------|-------------|
| [resume-ai-infra.md](resume-ai-infra.md) | AI-infra variant of the resume; lead with Claude/MCP/OpenClaw | Every AI-infra application |
| [resume.md](resume.md) | Original (platform-engineer) resume — keep for traditional platform roles | Non-AI-native platform/SRE roles |
| [linkedin-rewrite.md](linkedin-rewrite.md) | Copy-paste-ready LinkedIn headline + About + Featured | Update LinkedIn this week |
| [target-companies.md](target-companies.md) | 60-company target list (Tier 1-4) + application logging table | Weekly review; log every send |
| [applications-tier1.md](applications-tier1.md) | 15 ready-to-send Tier-1 applications with tailored 3-sentence notes | Send 2/week, weeks 2-4 |
| [hot-jobs-may-2026.md](hot-jobs-may-2026.md) | Live-scraped ranked shortlist of 14 best-fit openings as of 2026-05-26 | This week's apply queue |
| [referrals.md](referrals.md) | 3 warm referral paths + ask templates + tracking | Weeks 2-4 outreach |
| [portfolio/README.md](portfolio/README.md) | Pick 1 of 3 Month-2 artifacts | Pick in week 1; finish in weeks 5-8 |
| [portfolio/blog-openclaw-cost-aware-runtime.md](portfolio/blog-openclaw-cost-aware-runtime.md) | Draft blog post + publish checklist | If you pick Option A |
| [portfolio/one-pager.md](portfolio/one-pager.md) | 3-artifact 1-page summary; attach to referrals + thank-yous | Reuse heavily |

## Interview prep

| File | Purpose |
|------|---------|
| [interview-prep/STUDY-PLAN-5MONTHS.md](interview-prep/STUDY-PLAN-5MONTHS.md) | **Master 20-week study schedule** — read this every Monday |
| [interview-prep/coding-log.md](interview-prep/coding-log.md) | Daily LC log + Month 1/2 curated picks + pattern tracker |
| [interview-prep/system-design/01-llm-inference-serving.md](interview-prep/system-design/01-llm-inference-serving.md) | LLM inference serving (multi-tenant) |
| [interview-prep/system-design/02-vector-db-at-scale.md](interview-prep/system-design/02-vector-db-at-scale.md) | Vector DB at scale (HNSW / IVF-PQ / DiskANN) |
| [interview-prep/system-design/03-agent-orchestration.md](interview-prep/system-design/03-agent-orchestration.md) | Agent orchestration platform (LangGraph / Claude Agent SDK shape) |
| [interview-prep/system-design/04-eval-pipelines.md](interview-prep/system-design/04-eval-pipelines.md) | LLM / agent eval pipelines |
| [interview-prep/system-design/05-distributed-training-orchestration.md](interview-prep/system-design/05-distributed-training-orchestration.md) | Distributed training (Slurm vs K8s, gang sched, checkpoints) |
| [interview-prep/system-design/06-gpu-autoscaling.md](interview-prep/system-design/06-gpu-autoscaling.md) | GPU autoscaling for inference (signals, weight cache, lifecycle) |
| [interview-prep/system-design/07-multi-tenant-inference-cost.md](interview-prep/system-design/07-multi-tenant-inference-cost.md) | Cost attribution + chargeback at scale |
| [interview-prep/system-design/08-prompt-eval-registry.md](interview-prep/system-design/08-prompt-eval-registry.md) | Prompt + eval registry control plane |
| [interview-prep/star-stories.md](interview-prep/star-stories.md) | 10 STAR stories + cheat sheet of question→story |
| [interview-prep/mock-interviews.md](interview-prep/mock-interviews.md) | Month 2 mock cadence + protocol + log template |
| [interview-prep/phone-screen-playbook.md](interview-prep/phone-screen-playbook.md) | Recruiter + HM screen flow, elevator pitch, conversion dashboard |
| [interview-prep/onsite-deep-dives.md](interview-prep/onsite-deep-dives.md) | 3 staff-level deep-dive narratives + rehearsal schedule |
| [interview-prep/negotiation-and-offers.md](interview-prep/negotiation-and-offers.md) | Comp data sources, ask script, decision matrix |

## Figure applications (in-flight)

- [figure-applications/FINISH-REMAINING.md](figure-applications/FINISH-REMAINING.md) — runbook for the remaining 4 submissions.
- [figure-applications/apply_figure.py](figure-applications/apply_figure.py) — Playwright script with security-code polling.
- Status: 1/5 confirmed (Staff SRE). 4 remain; blocker is the 8-character Gmail verification code that I cannot read.

## Suggested weekly cadence (12 hrs/week)

| Day | Block | Activity |
|-----|-------|----------|
| Mon | 1 h | Apply to 2 new roles; update `target-companies.md`. |
| Mon | 1 h | LC problem; log it. |
| Tue | 1 h | LC problem. |
| Tue | 1 h | System-design read-and-rehearse (alternate doc weekly). |
| Wed | 1 h | LC problem. |
| Wed | 1 h | Portfolio artifact (M2 weeks). |
| Thu | 1 h | LC problem. |
| Thu | 1 h | Referral chases / recruiter calls. |
| Fri | 1 h | LC problem. |
| Fri | 1 h | STAR rehearsal (out loud). |
| Sat | 2 h | Portfolio artifact OR mock interview (M2-M3). |
| Sun | 1 h | Weekly retrospective: update conversion dashboard; replan for next week. |

If a phone screen lands on a weekday, replace that day's LC with screen prep + screen. Don't double-book yourself.

## Open questions to revisit at end of Month 1

- Is the resume conversion rate at or above the apply → recruiter benchmark (30-50%)? If not, iterate `resume-ai-infra.md`.
- Are the 3 referrals real and engaged? If only 1, add Path 4 (LangChain) and a second cohort of LinkedIn search.
- Is the artifact pick still right? If the blog re-benchmark is blocked, fall back to a polished MCP server (Option B).

## Open questions to revisit at end of Month 2

- Onsite count tracking to 3+? If only 1, increase Tier-2 applications.
- Coding self-score consistently ≥ 3.5 / 5 on mocks? If not, add 2 more mocks in Month 3 week 1.
- Cost/quality of phone-screen prep — is the elevator pitch landing? Listen back to one recorded screen.
