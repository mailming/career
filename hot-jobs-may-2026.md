# Hot AI-Infra Jobs Matching Your Background — May 2026

Live snapshot from company careers pages on 2026-05-26. Roles ranked by how directly your specific work at GEICO + OpenClaw + SmartTuna lines up.

For each role: the URL, why it's a fit, what to lead with in the cover note / first conversation, and any caveats.

---

## Tier S — Apply this week (perfect thesis match)

### 1. Anthropic — Staff+ Software Engineer, Developer Productivity

- **URL:** https://job-boards.greenhouse.io/anthropic/jobs/5110511008
- **Location:** San Francisco · New York City · Seattle
- **Why this is the single best fit on the list:** The team owns "build and CI infrastructure that keeps thousands of daily builds running reliably across multiple cloud providers" and "developer acceleration tooling that deeply integrates Claude into engineering workflows." That is literally what you are doing at GEICO today: JFrog SaaS POC (multi-cloud CI/CD), AMP reliability turnaround (thousands of daily builds), and the Claude Code / Cursor / MCP rollout (Claude integrated into engineering workflows). The JD even names Jenkins and GitHub Actions explicitly.
- **Lead with:** the Cursor × Claude Code MCP bridge BRD; the AI-powered CI/CD migration engine for the JFrog SaaS cutover; AI-augmented PRs as your engineering practice.
- **Bar:** 10+ years engineering + 3+ years tech-lead. You're well past both.
- **Stretch nice-to-haves to mention if you can:** Bazel remote execution / BuildBarn / BuildBuddy exposure (mention indirectly via the JFrog SaaS POC's build-cache work); Nix is rare and you can skip.
- **Resume to send:** [resume-ai-infra.md](resume-ai-infra.md) → `Mingresume.docx`.

### 2. Cursor — Software Engineer, Agent Harness

- **URL:** https://cursor.com/careers/software-engineer-agent-harness
- **Location:** San Francisco · New York City
- **Why it's a fit:** The role builds "the core agent behavior and capabilities that power agent experiences across Cursor products" — agent orchestration, tools, guardrails, model behavior tuning — including the **Auto model setting** (smart model choices based on cost appetite). Your OpenClaw cost-aware runtime is literally that thesis, applied to a different agent. You also use Cursor daily and author Cursor agent skills at GEICO.
- **Lead with:** OpenClaw cost-aware runtime; Cursor agent skills in production (`solve-case`, `close-case`, `build-kb`); Cursor × Claude Code MCP bridge.
- **Process note:** 2-3 short technicals + an in-person project day at SF or NY office. Plan for travel.
- **Caveat:** Cursor's culture is "flat, ~50 people, talent-dense, ship code." Cite shipping examples, not org-charts.

### 3. Cursor — Software Engineer, Agent Evaluation and Quality

- **URL:** https://jobs.ashbyhq.com/cursor (search "Agent Evaluation") or the Bebee mirror at https://bebee.com/us/jobs/software-engineer-agent-evaluation-and-quality-anysphere-san-francisco--lensa-2365_96d8c0eb98ee028e48a3899efe94551e4fdb0c098cd7769a2c65790c982eadd6
- **Location:** San Francisco · New York City
- **Why it's a fit:** "Curated datasets, offline replay, scorers/judges, regression alerts, dashboards" — your Month-1 eval-pipeline design doc ([interview-prep/system-design/04-eval-pipelines.md](interview-prep/system-design/04-eval-pipelines.md)) is a one-to-one match. OpenClaw's Langfuse + AgentOps integration gives you the production angle.
- **Lead with:** OpenClaw benchmark methodology; the eval-pipeline design write-up if interviewers want depth.

### 4. Anthropic — Staff + Sr. Software Engineer, AI Reliability

- **URL:** Apply via https://www.anthropic.com/careers/jobs?team=4019632008 (Infrastructure)
- **Location:** San Francisco · New York City · Seattle
- **Why it's a fit:** Reliability for AI systems at scale — your Artifactory monthly-incident → four-nines turnaround is the foundational story you have on this; pair with the NOCIM-11695 CoE narrative.
- **Lead with:** the deep-dive at [interview-prep/onsite-deep-dives.md](interview-prep/onsite-deep-dives.md#deep-dive-1--artifactory-9999-turnaround).

---

## Tier 1 — Strong fit, apply next week

### 5. Anthropic — Staff Software Engineer, Kubernetes Platform

- **URL:** https://www.anthropic.com/careers/jobs?team=4019632008 (filter "Kubernetes Platform")
- **Why:** AKS + Helm + Kubernetes operations is part of your GEICO AMP work; pair with ACS production deploy of `amp-control-plane`.
- **Caveat:** Bar is hyperscale K8s; you'll want to honestly position this as "experienced K8s operator, not core K8s internals contributor." Still credible.

### 6. Anthropic — Staff Infrastructure Engineer, Cluster Infrastructure

- **URL:** https://www.anthropic.com/careers/jobs?team=4019632008
- **Why:** Agent-driven automation for cluster provisioning. Your AI-augmented CI/CD migration engine is one example of agent-driven automation, applied to a different surface.
- **Caveat:** GPU / accelerator hyperscale (10K+ nodes) — be honest if asked, frame your scale story as JFrog SaaS POC (5,000 repos / 5,000 parallel artifacts).

### 7. Modal — Member of Technical Staff, Platform Engineering / Reliability Engineering

- **URL:** https://modal.com/company (Ashby board at https://jobs.ashbyhq.com/modal)
- **Location:** New York · San Francisco · Stockholm
- **Why:** Modal is hiring its first reliability-focused MTS. "Define the company's reliability systems and practices." That's exactly the playbook you ran at GEICO. NY-only or NYC + SF preferred (Stockholm option exists).
- **Lead with:** Artifactory four-nines + NOCIM-11695 CoE; Jenkins/Nexus HA migrations as the older but still relevant track record.
- **Caveat:** Modal hires at "MTS" levels (no formal IC ladder); positioning is by scope of impact, not title.

### 8. Databricks — Staff Backend Software Engineer (AI Platform)

- **URL:** https://www.databricks.com/company/careers/engineering/staff-backend-software-engineer--ai-platform-8367019002
- **Why:** The team builds MLflow, AI Gateway, Agent Framework, Agent Bricks, Foundation Model APIs. Your SmartTuna + OpenClaw work and the GEICO MCP rollout map onto Agent Framework + AI Gateway directly.
- **Lead with:** SmartTuna (multi-agent LangGraph); OpenClaw cost-aware runtime; MCP servers + Claude/Cursor agent skills.
- **Languages:** Scala / Go / Python. Lean on Go (you have it at GEICO) and Python.

### 9. Databricks — Staff Software Engineer, Agent Quality

- **URL:** https://www.databricks.com/company/careers/open-positions (filter "Agent Quality")
- **Location:** New York City
- **Why:** Same eval/quality thesis as Cursor's Agent Evaluation role.
- **Caveat:** NYC only as of this listing — confirm SF/remote acceptable before investing.

### 10. OpenAI — Software Engineer, Enterprise AI Platform

- **URL:** https://openai.com/careers/software-engineer-enterprise-ai-platform-san-francisco/
- **Location:** San Francisco (hybrid 3 days)
- **Why:** "Infrastructure and networking systems that connect structured and unstructured data to LLMs in a performant and reliable manner" — and "secure and compliant systems to process sensitive and valuable data." That is GEICO's AMP team's job description. You also wrote the Entra ID + APIM defense-in-depth plan, which is exactly the security-compliance angle.
- **Comp range:** $230K – $385K + equity (public posting).

### 11. Browserbase — Software Engineer (Agent Platform / Stagehand / Core Infrastructure)

- **URL:** https://www.browserbase.com/careers/
- **Location:** San Francisco (5 days/week in office)
- **Why:** OpenClaw is *the* browser-agent project — Browserbase's Stagehand is the closest commercial analogue. Your cost-aware runtime is a paper they would read. Their open roles include Agent Platform, Stagehand, Core Infrastructure, and Distributed Systems — all are on-thesis.
- **Lead with:** OpenClaw IEEE-style report + repo link; mention Playwright automation and Telegram control surface (their stack).
- **Caveat:** 5-day in-office requirement; Fremont commute to SF, decide if that's acceptable.

### 12. Sierra — Software Engineer, Agent Architecture (or Platform / Infrastructure)

- **URL:** https://sierra.ai/careers
- **Location:** Mostly SF + global offices
- **Why:** Agent SDK, orchestration engine, runtime — your LangGraph + Claude Agent SDK fluency is the language they speak. Also evals.
- **Caveat:** Bret Taylor + Clay Bavor's culture is "primarily in-person, San Francisco." Plan for hybrid+.

### 13. Perplexity — Member of Technical Staff (AI Infrastructure / AI Platform / API Platform)

- **URL:** https://jobs.ashbyhq.com/perplexity (or https://www.perplexity.ai/hub/careers)
- **Location:** San Francisco · Palo Alto · New York City
- **Why:** ~500 employees now, 43+ SF roles; multiple Member of Technical Staff (AI Infrastructure / AI Platform / API Platform) positions open. RAG architecture, search infrastructure, and LLM serving are their interview surfaces.
- **Lead with:** Inference cost-attribution design (you have a write-up); multi-model routing (SmartTuna provider plug-ins).

### 14. LangChain — Python OSS Engineer / Fullstack Applied AI Engineer

- **URL:** https://www.langchain.com/careers (Simplify mirror: https://simplify.jobs/p/5cf4f9eb-e137-4d3b-bfb8-ab77febabfed)
- **Location:** SF preferred · also Boston (Cambridge) · NYC
- **Why:** You built SmartTuna *on* LangGraph. The Python OSS role maintains LangChain/LangGraph; the Fullstack role builds internal AI agents on LangChain at LangChain. Both align.
- **Lead with:** SmartTuna.ai demo + GitHub; OpenClaw as bonus.
- **Caveat:** In-person 5 days/week, SF or Boston only. Decide commute tolerance.

---

## Tier 2 — Worth applying if Tier S/1 don't convert

| # | Company | Role | URL | Why |
|---|---------|------|-----|-----|
| 15 | OpenAI | Software Engineer, Data Infrastructure | https://openai.com/careers/software-engineer-data-infrastructure-san-francisco/ | Spark / Iceberg / Kafka / Airflow at exabyte scale — your Hadoop / Macrovision past + JFrog SaaS POC are credible angles. Stretch but real. |
| 16 | OpenAI | Capacity Systems Software Engineer | https://openai.com/careers/search/ (search "Capacity Systems") | Capacity planning at hyperscale — JFrog 5,000-repos load test maps. |
| 17 | OpenAI | Software Engineer, Infrastructure - Analytics Platform | https://openai.com/careers/software-engineer-infrastructure-analytics-platform-san-francisco/ | Rust / C++ required — softer fit; only if you want to lean Rust. |
| 18 | Anthropic | Staff Software Engineer, Continuous Integration | https://www.anthropic.com/careers/jobs?team=4019632008 (London) | Strong fit, but London-only. Pass unless you'd consider London. |
| 19 | Anthropic | Senior+ Software Engineer, Research Tools | https://www.anthropic.com/careers/jobs?team=4019632008 | Dev tooling for ML researchers; similar to Databricks AI Research Infra below. |
| 20 | Databricks | Staff Software Engineer, AI Research Infrastructure | https://www.databricks.com/company/careers/executive-engineering---pipeline/staff-software-engineer---ai-research-infrastructure-8532682002 | GPU fleet orchestration for thousands of GPUs — the JD names Kubernetes / Slurm / Ray. Mostly NYC/SF. Stretch but worth applying. |
| 21 | Sierra | Software Engineer, Site Reliability | https://sierra.ai/careers | Your 99.99% playbook |
| 22 | Sierra | Software Engineer, Agent Data Platform | https://agentic-engineering-jobs.com/jobs/sierra-software-engineer-agent-data-platform-bH6Jyp | Iceberg / Flink / Kafka / Trino — stretch but your old Hadoop work + current platform scope are angles |
| 23 | LangChain | Software Engineer (Storage Engine, Rust) | https://underprompt.com/jobs/software-engineer-langchain | Rust-required; storage-engine work; only if you want to lean Rust |
| 24 | Browserbase | Software Engineer (Distributed Systems) | https://jobs.ashbyhq.com/Browserbase | Same thesis as #11; pick whichever you fit most cleanly |
| 25 | Perplexity | Member of Technical Staff (AI Inference Engineer) | https://jobs.ashbyhq.com/perplexity | Inference-side specialty |

---

## Already in flight (continue)

- **Figure** — Staff Site Reliability Engineer **submitted** + Senior/Staff Software Engineer, Developer Tools and Productivity **submitted**. Three Helix AI Engineer roles still need resubmit (script ready at [figure-applications/apply_figure.py](figure-applications/apply_figure.py)).

---

## Suggested apply order this week

1. **Mon:** Anthropic Developer Productivity (#1) + Cursor Agent Harness (#2). Both are top-of-mind matches; do them while the rest of the week's energy is still available.
2. **Tue:** Cursor Agent Eval (#3) + Anthropic AI Reliability (#4).
3. **Wed:** Modal MTS (#7) + Databricks AI Platform (#8).
4. **Thu:** OpenAI Enterprise AI Platform (#10) + Browserbase (#11).
5. **Fri:** Sierra Agent Architecture (#12) + Perplexity AI Infrastructure (#13) + LangChain Python OSS (#14).

That puts you at **11 Tier-S/1 applications by Friday**, matching the Month-1 plan target of ~15 Tier-1 by end of week 4 (with Figure already submitted).

## What to use for each

- Resume: [resume-ai-infra.md](resume-ai-infra.md) → `Mingresume.docx`
- Cold note: use the templates in [applications-tier1.md](applications-tier1.md); for Anthropic Developer Productivity, lead with "I'm leading our Claude Code / Cursor / MCP rollout at GEICO and just built the Cursor × Claude Code MCP bridge — that's the JD."
- Form values: see [figure-applications/FINISH-REMAINING.md](figure-applications/FINISH-REMAINING.md) bottom section (same for all Greenhouse-hosted boards).
- Track every submission in [target-companies.md](target-companies.md) "Application logging" table.

## Notes on Greenhouse automation

Several of these are Greenhouse-hosted (Anthropic, Sierra, Databricks, OpenAI applied roles, LangChain). The `apply_figure.py` script in [figure-applications/](figure-applications/) is adaptable — copy it, swap the board URL and `JOBS` list, and reuse. The 8-char Gmail verification flow Greenhouse uses is identical across boards.

## What I deliberately left off

- **Anthropic Staff+ Backend / Full-stack / Billing Platform / Mobile** — all real and open, but less thesis-fit than Developer Productivity / AI Reliability / Kubernetes Platform.
- **Big-tech AI orgs (Meta GenAI, Google DeepMind, MS, AWS Bedrock)** — they hire constantly; not a "hot" signal worth highlighting at this snapshot. Apply if Month 1 conversion is slow.
- **NVIDIA NeMo, Snowflake Cortex, Tesla AI** — open roles exist but cold-application conversion is much lower than the AI-native shops above; warm referral required to be efficient.
- **Robotics-adjacent (1X, Apptronik, Skild, Physical Intelligence)** — Figure is already in flight; expand only if Figure converts and you want more humanoid-robotics surface.
