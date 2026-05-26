# Ming Jia

**Fremont, CA** · **(626) 354-7866** · **mailming@gmail.com**  
**LinkedIn:** [linkedin.com/in/mailming](https://www.linkedin.com/in/mailming) · **GitHub:** [github.com/mailming](https://github.com/mailming) · **SmartTuna:** [smarttuna.ai](https://smarttuna.ai)

---

## Summary

AI infrastructure / platform engineer building production agentic systems and the platforms that run them. Architect and primary implementer of the **OpenClaw cost-aware runtime plugin** (Purdue ECE 50874) — a governance layer giving browser agents token/cost/step budgets, AgentOps routing, and Langfuse telemetry without rewriting agent core. Founder of **[SmartTuna](https://smarttuna.ai)** (LangGraph multi-agent stock-analysis platform). At GEICO Developer Engineering, **invited to the Claude Code pilot** and shipping a portfolio of four AI initiatives into the **DE AI Showcase 2026** (282-associate org): a Claude Agent SDK Slack triage, an **AI-powered CI/CD migration engine** for the JFrog SaaS cutover, a plain-English **Claude Code plugin** for Artifactory, and AI-consumable runbooks/ADRs. Authored the **Cursor MCP × Slack** BRD and built the Cursor-cached-token bridge that lets Claude Code reuse Cursor's encrypted Slack MCP credentials. Underneath the AI work: 20+ years of high-availability platform engineering — drove GEICO's Artifactory from ~1 major incident/month to **four-nines (99.99%) availability**, led HA Jenkins / HA Nexus migrations at Turn/Amobee ($600K+/yr savings), and led Navan's SOC 2 Type II remediation for IPO readiness. MS in Artificial Intelligence at Purdue (in progress). U.S. Citizen.

---

## Selected AI Work

### OpenClaw Cost-Aware Runtime Plugin — *Project lead & primary implementer*
*Purdue ECE 50874/59500 Team 17 · IEEE-style report: "Design and Evaluation of a Cost-Aware Runtime for OpenClaw Browser Agents" · [github.com/mailming/openclaw](https://github.com/mailming/openclaw/tree/feature/llm-insights-manual-pricing) (2026)*

- **Originated the cost-aware runtime concept** — a governance layer wrapping [OpenClaw](https://github.com/openclaw-ai/openclaw) browser agents with per-task token/cost/step budgets and post-action policy enforcement, leaving agent core untouched
- **Designed and built the LLM Insights gateway plugin**: rolling cost/latency aggregates, manual pricing overrides for non-standard model SKUs, and a usage-to-cost pipeline that works across multi-model agent traffic
- Integrated **AgentOps** (routing + budget state) and **Langfuse** (trace telemetry); deployed the gateway with Playwright automation and a Telegram control surface for live demos

### SmartTuna — *Founder · [smarttuna.ai](https://smarttuna.ai)*
*LangGraph multi-agent stock analysis · Python backend [`smarttuna`](https://github.com/mailming/smarttuna) + Astro UI [`zzsheepTrader`](https://github.com/mailming/zzsheepTrader)*

- Multi-agent LangGraph orchestration with model-pluggable providers (Claude / GPT / Gemini), trade-rationale generation, and a public UI

### Claude Code / Cursor / MCP at GEICO Enterprise Scale (2025–2026)
*GEICO DE AI Showcase 2026 — org-wide AI-augmented-work program (282 DE associates)*

- **Portfolio of four AI initiatives in flight**:
  - (a) **Claude Agent SDK triage** for the `#help-pkg-mgmt` Slack channel — auto-classifies and runs first-pass response on incoming support
  - (b) **AI-powered CI/CD migration engine** that opens per-team PRs for the JFrog SaaS cutover (target: 100% of inventoried pipelines)
  - (c) **Claude Code plugin for AMP/JFrog** — plain-English Artifactory operations, targeting publication to GEICO's `developer-agent-hub` marketplace
  - (d) **AI-consumable artifact-auth ADR** — designed so any AI agent can onboard external teams without AMP hand-holding
- **Cursor × Claude Code MCP bridge** — invited to GEICO's Claude Code pilot; authored the *"Cursor MCP × Slack"* BRD and built the Cursor-cached-token bridge that lets Claude Code reuse Cursor's encrypted Slack MCP credentials; active in `#sig-ai-assisted-development`
- **MCP servers and agent skills in production** — shipped Club MCP server config into `amp-control-plane`; introduced JFrog, Slack, ADO, GitHub MCP servers and Claude / Cursor agent skills (`solve-case`, `close-case`, `build-kb`) across support, RCA, and runbook workflows; follow-on skills + Cursor agent hooks landing via `club-developer-agent-plugins`
- **AI-augmented engineering as practice** — every May 2026 AMP / pkg-mgmt PR authored with Claude Code or Cursor (Entra ID auth plan, JFrog SaaS POC workflows, ACS prod deployment); surgical Slack RCAs are AI-augmented end-to-end

---

## Work Experience

### Senior Engineer — GEICO, Artifact Management Platform (Developer Engineering)
**06/2025 – Present** · Staff-IC tech lead for AMP's cross-org initiatives (Identity, SRE, Network, Database Platform, DE)

*Platform reliability for ML/AI developer workflows at GEICO scale*

- **Artifactory reliability turnaround:** **~1 major incident/month → four-nines (99.99%) availability SLO** — the backbone for every model-artifact, container image, and ML pipeline binary the engineering org consumes
- **Technical lead, JFrog SaaS POC** — three GitHub Actions workflows validating **all 11 supported JFrog package types** end-to-end on `geicoeast.jfrog.io`; **SaaS load test at 5,000 repos / 5,000 parallel artifacts**
- **Architected Entra ID auth for `amp-control-plane`** via cross-team plan (Go JWT middleware + APIM defense-in-depth); deployed `amp-control-plane` to ACS production
- **Production incident leadership** — packet-level Azure Firewall TLS DPI RCA on S3-backed repos; JFrog Go-module cache RCAs; **CoE author for NOCIM-11695** (April 2026 Entra-ID-driven Artifactory outage); AMP on-call lead
- See **Selected AI Work** above for the Claude Agent SDK / MCP / Cursor portfolio shipped in parallel

### Staff Release Engineer / DevOps — Navan (formerly TripActions)
**01/2022 – 04/2025**

- Led **SOC 2 Type II** audit remediation; deployed **HashiCorp Vault** and **SonarCloud** across CI/CD to support **IPO readiness**
- Owned SCM and release engineering for the engineering org; built and maintained continuous delivery for core web and data systems on AWS
- Built mobile CI/CD with Bitrise for App Store and Google Play; drove rapid RCA on pipeline and production incidents

### Lead Release Engineer — Turn / Amobee
**12/2015 – 11/2021**

- Led 2 release engineers + 5 offshore NOC engineers; scaled release ops for a ~500-person engineering org deploying to **thousands of production servers worldwide**
- **Jenkins HA migration** — cut unplanned outages from hours/week to <5 min planned downtime/month; UI 12s → 0.5s/page; **saved $500K+/year** vs. CloudBees enterprise licensing
- **Nexus HA migration** — eliminated unplanned outages post-migration; **saved $100K+/year** vs. Sonatype enterprise licensing
- Built deployment automation and enforced release process; hands-on Technical Operations in production

### Sr. Software Engineer — Skytree *(Machine Learning startup)*
**04/2014 – 11/2015**

- Built end-to-end CI/CD for an ML product, **AWS dynamic cluster provisioning (EC2, S3, EMR)**, and a PaaS tool for on-demand ML environments; led agile adoption

### Sr. Software Engineer — Walmart Labs
**03/2013 – 04/2014**

- Automated build/release across Dev, QA, and production; operated and supported multiple production systems for engineering teams

### Software Engineer — Macrovision / Rovi
**11/2009 – 02/2013**

- CM/build/release/change management across **20+ projects** and four international teams; **Hadoop / MapReduce / MongoDB** operations
- Automated builds and CI (Maven, Ant, TeamCity, Jenkins); built a CM portal with automated release notes; established company-wide Git repos

### SCM Manager — Helio / Virgin Mobile USA / Sprint
**02/2007 – 10/2009**

- Server layout, deployment procedures, and CI/CD (CruiseControl, Hudson/Jenkins); VM automation, JBoss deployment automation, defect-tracking rollout

### Software Developer — XLDynamics
**01/2005 – 02/2007**

- Core dev systems on Linux/Unix/Windows; build/release automation, C++ XML/SOAP apps, Shell-based server tooling

---

## Skills

| Category | Technologies |
|----------|--------------|
| **AI / Agents / LLM** | Claude Agent SDK, Claude Code & plugins, Cursor agents & MCP, **Model Context Protocol (MCP) servers** (JFrog, Slack, ADO, GitHub, Club, Gemini, browser), LangGraph, AgentOps, Langfuse, OpenClaw, Playwright agents, Anthropic Claude / OpenAI GPT / Google Gemini, Ollama, vLLM |
| **AI Infra concepts** | LLM cost governance, agent runtimes, evals & traces, multi-model routing, prompt/agent skill packaging, MCP server publishing |
| **Cloud & Platform** | AWS, Azure (AKS, ACR, Entra ID, Azure Firewall), Kubernetes, Helm, Terraform, Docker, OpenStack |
| **CI/CD & Artifacts** | Jenkins, GitHub Actions, Azure DevOps, ArgoCD, Bitrise, JFrog Artifactory / X-Ray / SaaS, Nexus, ACR |
| **Languages & Build** | Python, Go, Java, TypeScript, Shell, Groovy, Maven, Gradle, C/C++ |
| **Security & Compliance** | SOC 2 Type II, HashiCorp Vault, Azure Key Vault, SonarCloud, OIDC, Entra ID |
| **Leadership** | Staff-IC tech lead, cross-org RFCs and architecture, on-call/incident ownership, global team coordination, AI-tooling advocacy |

---

## Education

**Purdue University** — MS, Artificial Intelligence *(In Progress)* — ECE 50874/59500: led OpenClaw cost-aware runtime plugin (final project), LLM-augmented software engineering

**UCLA** — BS, Computer Science *(Minors: Mathematics & Economics)*

---

**Work Authorization:** U.S. Citizen
