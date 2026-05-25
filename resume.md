# Ming Jia

**34500 Bentley Ct., Fremont, CA 94555**  
**(626) 354-7866** · **mailming@gmail.com**

---

## Summary

Staff-scope platform engineer and AI builder with 20+ years across CI/CD, artifact management, and high-availability infrastructure on AWS, Azure, and Kubernetes. Staff Engineer on GEICO's Artifact Management Platform — drove Artifactory from ~1 major incident/month to **four-nines (99.99%) availability SLO**, and **practice every platform change as AI-augmented engineering** (every May 2026 platform PR authored with Claude Code / Cursor; surgical, packet-level RCAs co-written with AI agents). Delivering a portfolio of AI initiatives entered into **GEICO's DE AI Showcase 2026** (org-wide, 282 DE associates, "real work accelerated through AI"): a Claude Agent triage prototype for the team's Slack help channel, an **AI-powered CI/CD pipeline migration engine** for the JFrog SaaS cutover (target: 100% of inventoried pipelines), a **Claude Code plugin** that lets engineers manage Artifactory in plain English, and **AI-consumable runbooks / ADR** for artifact authentication. Invited to GEICO's Claude Code pilot; authored the *"Cursor MCP × Slack"* business requirement and built the Cursor-cached-token bridge that lets Claude Code reuse Cursor's encrypted Slack MCP credentials; active contributor in `#sig-ai-assisted-development`. Previously Staff Release Engineer at Navan (SOC 2 Type II, IPO readiness); $600K+/yr savings through HA Jenkins/Nexus migrations at Turn/Amobee. **Led** the **OpenClaw cost-aware runtime plugin** (originated the approach; primary implementer) — Purdue ECE 50874/59500 final project. Pursuing MS in Artificial Intelligence at Purdue; founder of [SmartTuna](https://smarttuna.ai/) (LangGraph multi-agent stock-analysis platform).

---

## Work Experience

### Staff Engineer — GEICO, Artifact Management Platform (Developer Engineering)
**Insurance · 06/2025 – Present**

*Technical lead and primary architect for AMP's largest cross-org initiatives — Identity, SRE, Network, Database Platform, and Developer Engineering. Selected for GEICO's DE AI Showcase track.*

*AI initiatives — entered into GEICO's DE AI Showcase 2026 (282 DE associates org-wide)*

- **Claude Agent triage prototype for `#help-pkg-mgmt`** — designing and building a Claude Agent SDK prototype that ingests the team's Slack help-channel history and surfaces recurring issues, unanswered threads, and trend signals — eliminating single-point-of-failure support and feeding the DE AI June showcase
- **AI-powered CI/CD migration engine for JFrog SaaS** — leading delivery of an AI agent that scans every GEICO CI/CD pipeline (GitHub Actions + Azure DevOps), determines the required auth / URL / repo-structure changes for the SaaS cutover, and opens a migration PR for each owning team — target: **100% of inventoried pipelines**
- **Claude Code plugin for AMP / JFrog** — building a plain-English Claude Code plugin so engineers can create repositories, configure OIDC identity mappings, and check migration status without filing tickets or using the JFrog UI; targeting publication to GEICO's central [`developer-agent-hub`](https://github.com/geico-private/developer-agent-hub) so any GEICO developer can install it from the marketplace; aimed at a measurable drop in support-ticket volume
- **AI-consumable artifact-auth ADR** — defining the GEICO standard for OIDC / service-principal / Artifactory integration as machine-readable runbooks any AI agent can consume to onboard external teams without AMP hand-holding
- **Cursor × Claude Code MCP bridge** — invited to GEICO's Claude Code pilot; authored the formal *"Cursor MCP × Slack"* business-requirement document and reverse-engineered the Cursor-cached-token bridge that lets Claude Code reuse Cursor's encrypted Slack MCP credentials; active advocate in `#sig-ai-assisted-development`
- **MCP servers & agent skills for AMP operations** — shipped Club MCP server configuration directly into the `amp-control-plane` deployment ([AMP #371](https://github.com/geico-private/artifact-management-platform/pull/371)) so Cursor can drive Club-blueprint actions on the team's production service; introduced JFrog, Slack, ADO, and GitHub MCP servers into the team's daily workflow; brought Claude/Cursor agent skills (`solve-case`, `close-case`, `build-kb`) into support, RCA, and runbook handling
- **Club MCP server skills & Cursor agent hooks for AMP** — designing dedicated Club MCP server skills and Cursor agent hooks (e.g., post-merge runbook regeneration, automated OIDC mapping audits, pre-deploy Vault-path validation) for distribution via [`club-developer-agent-plugins`](https://github.com/geico-private/club-developer-agent-plugins), turning AMP's repeatable operational toil into reusable AI-driven tasks
- **AI-augmented platform engineering as practice** — *every* `geico-private/artifact-management-platform` and `pkg-mgmt` PR in May 2026 is authored with Claude Code or Cursor (Entra ID auth plan, JFrog SaaS POC workflows for 11 package types, ACS prod deployment, runbooks); surgical Slack RCAs (JFrog Go-module cache; Debian `deb.architecture=64` indexer; Azure Firewall TLS DPI on S3) are AI-augmented end-to-end

*Platform engineering*

- **Artifactory reliability turnaround** — drove remediation across platform, config, and operations; **~1 major incident/month → four-nines (99.99%) availability SLO**
- **Technical lead, JFrog SaaS POC (Phase 4)** — delivered three GitHub Actions workflows validating **all 11 supported JFrog package types** (Maven, Gradle, npm, PyPI, Go, NuGet, Docker, Helm, Debian, RPM, Generic) end-to-end on `geicoeast.jfrog.io`; outcomes feed GEICO's enterprise artifact-management roadmap; ran SaaS load test at 5,000 repos / 5,000 parallel artifacts
- **Architected Entra ID auth for `amp-control-plane`** via cross-team implementation plan — Go JWT middleware as the authoritative check + APIM `custom-jwt-ws` as defense-in-depth, single app registration in the GEICO tenant, separate NP/PD access boundaries, `AUTH_ENABLED` gradual rollout, audit-log enrichment with `caller_oid` / `caller_upn`
- **Zero-downtime platform upgrades** — scripted, pipeline-driven rolling upgrades for Artifactory and X-Ray across Package Registry and Martech tenants on AKS with **zero customer impact** and a runbook any teammate can execute
- **Production incident leadership** — packet-level RCA and cross-team fix for Azure Firewall TLS DPI on S3-backed remote repos; JFrog Go-module cache RCA (`workflowengine` v1.7.9 / `voltage-go` v0.0.1 / `@latest` pseudo-version caching); Debian `deb.architecture` indexer fix; Martech JVM/OOM investigation; **CoE author for NOCIM-11695** (April 2026 Entra ID-driven Artifactory outage); AMP team on-call lead

### Staff Release Engineer / DevOps — Navan (formerly TripActions)
**E-Commerce · 01/2022 – 04/2025**

- Led **SOC 2 Type II** audit remediation; deployed **HashiCorp Vault** and **SonarCloud** across CI/CD to support **IPO readiness**
- Owned SCM and release engineering for the engineering org; built and maintained continuous delivery for core web and data systems on AWS
- Built mobile CI/CD with Bitrise for App Store and Google Play; drove rapid RCA on pipeline and production incidents

### Lead Release Engineer — Turn / Amobee
**Ad Technology · 12/2015 – 11/2021**

- Led 2 release engineers + 5 offshore NOC engineers; scaled release ops for ~500-person engineering org deploying to **thousands of production servers worldwide**
- **Jenkins HA migration** — cut unplanned outages from hours/week to <5 min planned downtime/month; UI 12s → 0.5s/page; **saved $500K+/year** vs. CloudBees enterprise licensing
- **Nexus HA migration** — eliminated unplanned outages post-migration; **saved $100K+/year** vs. Sonatype enterprise licensing
- Built deployment automation and enforced release process; hands-on Technical Operations in production

### Sr. Software Engineer — Skytree
**Machine Learning · 04/2014 – 11/2015**

- Built end-to-end CI/CD systems, AWS dynamic cluster provisioning (EC2, S3, EMR), and a PaaS tool for on-demand environments; led agile adoption

### Sr. Software Engineer — Walmart Labs
**E-Commerce · 03/2013 – 04/2014**

- Automated build/release across Dev, QA, and production; operated and supported multiple production systems for engineering teams

### Software Engineer — Macrovision / Rovi
**Digital Media · 11/2009 – 02/2013**

- CM/build/release/change management across **20+ projects** and four international teams; Hadoop/MapReduce/MongoDB ops
- Automated builds and CI (Maven, Ant, TeamCity, Jenkins); built CM portal with automated release notes; established company Git repos

### SCM Manager — Helio / Virgin Mobile USA / Sprint
**Telecommunications · 02/2007 – 10/2009**

- Server layout, deployment procedures, and CI/CD (CruiseControl, Hudson/Jenkins); VM automation, JBoss deployment automation, defect-tracking rollout

### Software Developer — XLDynamics
**01/2005 – 02/2007**

- Core dev systems on Linux/Unix/Windows; build/release automation, C++ XML/SOAP apps, Shell-based server tooling

---

## Selected Projects

### OpenClaw Cost-Aware Runtime Plugin — Purdue ECE 50874/59500 Final Project (2026)
***Project lead & primary implementer** · Team 17 · IEEE-style report: "Design and Evaluation of a Cost-Aware Runtime for OpenClaw Browser Agents" · [github.com/mailming/openclaw](https://github.com/mailming/openclaw/tree/feature/llm-insights-manual-pricing)*

- **Originated the cost-aware runtime concept** and led end-to-end implementation — a governance layer around [OpenClaw](https://github.com/openclaw-ai/openclaw) browser agents with token/cost/step budgets and post-action policy enforcement, without rewriting core agent logic
- **Designed and built the LLM Insights gateway plugin** (primary implementation): rolling cost/latency aggregates, manual model pricing overrides, and usage-to-cost pipeline for multi-model agent operations
- Integrated **AgentOps** (LLM routing, budget state) + **Langfuse** (trace telemetry); deployed gateway, Playwright automation, and Telegram control for live demos

### SmartTuna — Founder ([smarttuna.ai](https://smarttuna.ai/))
LangGraph multi-agent stock analysis · Python backend ([smarttuna](https://github.com/mailming/smarttuna)) + Astro UI ([zzsheepTrader](https://github.com/mailming/zzsheepTrader))

---

## Key Competencies

- **AI engineering for platform ops:** Claude Agent SDK / Claude Code plugins, AI-powered CI/CD migration agents, AI-consumable runbooks & ADRs, agent-driven triage and RCA, multi-agent LangGraph systems
- **MCP & coding-agent integration:** building and integrating MCP servers (JFrog, Slack, ADO, GitHub, Club, Gemini, browser); authoring Cursor / Claude agent skills; safe enterprise credential bridging
- **AI-augmented engineering practice:** Claude Code- / Cursor-authored production PRs, AI-co-authored packet-level RCAs, AI-driven runbook generation, AI-pair-programmed Go / Helm / GitHub-Actions / CRQ-deployment work
- **Platform & DevOps:** CI/CD, build/release engineering, artifact management at scale (JFrog Artifactory HA, X-Ray, Catalog, SaaS, Nexus, ACR), Kubernetes/AKS, Terraform, Helm
- **Cloud:** AWS, Azure (Entra ID, Azure Firewall, AKS, ACS), multi-region HA, Docker
- **Security & compliance:** SOC 2 Type II, Vault, Azure Key Vault, SonarCloud, OIDC/RBAC, audit remediation
- **Leadership:** Staff-IC technical lead, cross-org RFCs and architecture, on-call/incident ownership, global team coordination, AI-tooling advocacy

---

## Technical Skills

| Category | Technologies |
|----------|--------------|
| **Cloud & Platform** | AWS, Azure (AKS, ACR, Entra ID, Azure Firewall), Kubernetes, Helm, Terraform, Docker, OpenStack |
| **CI/CD & Artifacts** | Jenkins, GitHub Actions, Azure DevOps, ArgoCD, Bitrise, JFrog Artifactory/X-Ray/SaaS, Nexus, ACR |
| **Languages & Build** | Python, Go, Java, Shell, Groovy, Maven, Gradle, TypeScript, C/C++ |
| **Security** | SOC 2 Type II, HashiCorp Vault, Azure Key Vault, SonarCloud, OIDC, Entra ID |
| **AI / LLM** | Claude Agent SDK, Claude Code & plugins, Cursor agents & MCP, Model Context Protocol (MCP) servers (JFrog, Slack, ADO, GitHub, Club), LangGraph, AgentOps, Langfuse, OpenClaw, Playwright agents, Anthropic Claude / OpenAI GPT / Google Gemini, Ollama, vLLM |

---

## Education

**Purdue University** — MS, Artificial Intelligence *(In Progress)* · ECE 50874/59500: led OpenClaw cost-aware runtime plugin (final project), LLM-augmented software engineering

**UCLA** — BS, Computer Science *(Minor: Mathematics & Economics)*

---

## Additional

**Work Authorization:** U.S. Citizen
