# Ming Jia

**Fremont, CA** · **(626) 354-7866** · **mailming@gmail.com**  
**LinkedIn:** [linkedin.com/in/mailming](https://www.linkedin.com/in/mailming) · **GitHub:** [github.com/mailming](https://github.com/mailming) · **Jiadroid:** [github.com/mailming/jiadroid](https://github.com/mailming/jiadroid) · **SmartTuna:** [smarttuna.ai](https://smarttuna.ai)

---

## Summary

AI infrastructure / platform engineer building production agentic systems and the platforms that run them. At GEICO Developer Engineering (Staff-IC on Artifact Management), drove Artifactory to **four-nines availability**, shipped **Load Healer Reactive** (OUTAGE → HTTP 429 throttle on NP/PD2), and am leading **Martech → JFrog SaaS cutover** outreach (Jan 30 hard date) across MAP, CDP, Billing, and Payments while running `amp-migrate` for OIDC/repo-settings campaigns. Invited to GEICO's **Claude Code pilot**; built the **Cursor × Claude Code MCP bridge** and landed MCP servers + agent skills in AMP production. Outside work: founded **[Jiadroid](https://github.com/mailming/jiadroid)** (phone-as-robot-brain protocol + ESP32 2WD + Follow Me apps) and led the **OpenClaw cost-aware runtime** (Purdue ECE 50874). Founder of **[SmartTuna](https://smarttuna.ai)**. 20+ years HA platform (Navan SOC 2 / IPO; Turn/Amobee Jenkins+Nexus HA, $600K+/yr savings). MS AI @ Purdue (in progress). U.S. Citizen.

---

## Selected AI Work

### Jiadroid — *Founder · [github.com/mailming/jiadroid](https://github.com/mailming/jiadroid)*
*Phone-as-robot-brain · embodied agent platform (2026)*

- Open **phone↔robot protocol** (device discovery, `motion.velocity`, latched estop) so a phone supplies brain/eyes/ears/internet for any compatible body
- Shipped **ESP32-S3 firmware** for a 2WD chassis (L9110S + encoders); Wi-Fi + **USB-C serial / OTA** from Android; Save Wi-Fi to NVS
- **Follow Me** on Android + iOS (person/marker tracking, voice wake, emotion-driven eyes) driving duck + **rover** sims (kinematic + MuJoCo)

### OpenClaw Cost-Aware Runtime Plugin — *Project lead & primary implementer*
*Purdue ECE 50874/59500 · [github.com/mailming/openclaw](https://github.com/mailming/openclaw/tree/feature/llm-insights-manual-pricing) (2026)*

- Governance layer wrapping browser agents with per-task token/cost/step budgets and post-action policy — agent core untouched
- LLM Insights gateway: rolling cost/latency aggregates, manual pricing overrides; **AgentOps** + **Langfuse** telemetry

### Claude Code / Cursor / MCP at GEICO (2025–2026)
*DE AI Showcase 2026 · 282-associate org*

- Portfolio: Claude Agent SDK Slack triage; **AI-powered CI/CD / `amp-migrate` cutover** path; Claude Code AMP/JFrog plugin; AI-consumable artifact-auth ADR
- **Cursor × Claude Code MCP bridge** — enterprise Slack MCP credential reuse for Claude Code pilot
- Production MCP servers (JFrog, Slack, ADO, GitHub, Club) + agent skills (`solve-case`, `close-case`, `build-kb`); Slack **maintenance-announcement** skill

### SmartTuna — *Founder · [smarttuna.ai](https://smarttuna.ai)*
LangGraph multi-agent stock analysis · Python + Astro UI

---

## Work Experience

### Senior Engineer — GEICO, Artifact Management Platform (Developer Engineering)
**06/2025 – Present** · Staff-IC tech lead for AMP cross-org initiatives (Identity, SRE, Network, DE)

*Platform reliability + SaaS cutover for ML/AI developer workflows at GEICO scale*

- **Artifactory reliability:** ~1 major incident/month → **99.99% SLO**; upgraded to **7.161.15**; AMP on-call lead
- **Load Healer Reactive** (`pkg-jfrog-charts` PR #109/#111) — NP validated + **PD2** deployed; OUTAGE → per-account **HTTP 429** instead of node meltdown; data-driven concurrency threshold (~640)
- **Martech-off / JFrog SaaS cutover** (hard date Jan 30) — stood up `#amp-martech-migration` / `#amp-cdp-migration`; kicked off MAP, CDP Self Serve/Chameleon, Billing, Payments, Bolt·Athena; installed **`amp-migrate`** for OIDC + repo-settings campaigns
- **Technical lead, JFrog SaaS POC** — GitHub Actions validating **all 11 package types** end-to-end; load test **5,000 repos / 5,000 parallel artifacts**
- **Entra ID auth for `amp-control-plane`** (Go JWT + APIM); ACS production deploy
- **CoE author:** NOCIM-11695 (Entra-ID outage), NOCIM-12455 (npm EINTEGRITY), **NOCIM-13154** (MarTech PD upgrade), **NOCIM-13213** (router OOM); PD Phase 1 stability + TLS renewals with **&lt;1 min** outage

### Staff Release Engineer / DevOps — Navan (formerly TripActions)
**01/2022 – 04/2025**

- Led **SOC 2 Type II** audit remediation; Vault + SonarCloud for **IPO readiness**
- Owned SCM/release engineering and AWS continuous delivery; Bitrise mobile CI/CD

### Lead Release Engineer — Turn / Amobee
**12/2015 – 11/2021**

- Led 2 REs + 5 offshore NOC for ~500-engineer org, thousands of servers worldwide
- **Jenkins HA** + **Nexus HA** — eliminated unplanned outages; **$600K+/yr** license savings vs enterprise

### Sr. Software Engineer — Skytree *(Machine Learning startup)*
**04/2014 – 11/2015**

- CI/CD for ML product; AWS EC2/S3/EMR dynamic clusters; PaaS for on-demand environments

### Sr. Software Engineer — Walmart Labs
**03/2013 – 04/2014** — Build/release automation Dev→Prod

### Software Engineer — Macrovision / Rovi
**11/2009 – 02/2013** — CM across 20+ projects; Hadoop/MapReduce/MongoDB; company-wide Git

### SCM Manager — Helio / Virgin Mobile USA / Sprint
**02/2007 – 10/2009** — CI/CD (CruiseControl, Hudson/Jenkins); VM + JBoss automation

### Software Developer — XLDynamics
**01/2005 – 02/2007** — Build/release automation; C++ XML/SOAP; Shell tooling

---

## Skills

| Category | Technologies |
|----------|--------------|
| **AI / Agents / LLM** | Claude Agent SDK, Claude Code & plugins, Cursor agents & MCP, MCP servers (JFrog, Slack, ADO, GitHub, Club), LangGraph, AgentOps, Langfuse, OpenClaw, Playwright agents, Claude / GPT / Gemini, Ollama, vLLM |
| **Embodied / Physical AI** | Jiadroid protocol, ESP32-S3 firmware, USB-C serial/OTA, Follow Me vision, multi-body sims (rover, MuJoCo duck) |
| **AI Infra concepts** | LLM cost governance, agent runtimes, evals & traces, multi-model routing, MCP packaging |
| **Cloud & Platform** | AWS, Azure (AKS, ACR, Entra ID, Azure Firewall), Kubernetes, Helm, Terraform, Docker |
| **CI/CD & Artifacts** | Jenkins, GitHub Actions, Azure DevOps, ArgoCD, JFrog Artifactory / X-Ray / SaaS, Nexus, ACR |
| **Languages** | Python, Go, Java, TypeScript, Shell, Kotlin/Swift (mobile clients), C/C++ |
| **Security & Compliance** | SOC 2 Type II, Vault, Azure Key Vault, OIDC, Entra ID |
| **Leadership** | Staff-IC tech lead, cross-org cutover programs, on-call/incident ownership, AI-tooling advocacy |

---

## Education

**Purdue University** — MS, Artificial Intelligence *(In Progress)* — ECE 50874/59500 OpenClaw final project; CNIT 57500 Data Analysis (Fall 2026)

**UCLA** — BS, Computer Science *(Minors: Mathematics & Economics)*

---

**Work Authorization:** U.S. Citizen
