# Ming Jia

**34500 Bentley Ct., Fremont, CA 94555**  
**(626) 354-7866** · **mailming@gmail.com**

---

## Summary

Staff-scope DevOps and platform engineer with 20+ years building CI/CD, artifact management, and high-availability infrastructure across AWS, Azure, and Kubernetes. Currently Staff Engineer on GEICO's Artifact Management Platform — improved Artifactory from ~1 major incident/month to **four-nines (99.99%) Artifactory availability SLO**, technical lead for enterprise JFrog strategy, Entra ID platform auth, and SOC-grade platform operations. Previously Staff Release Engineer at Navan (SOC 2 Type II / IPO readiness). Track record of multi-million-dollar savings through HA Jenkins/Nexus migrations, global release operations at scale, and cross-org incident leadership. **Led** the **OpenClaw cost-aware runtime plugin** (originated the approach; primary implementer) for production browser-agent governance. Pursuing MS in Artificial Intelligence at Purdue; founder of [SmartTuna](https://smarttuna.ai/).

---

## Work Experience

### Staff Engineer — GEICO, Artifact Management Platform (Developer Engineering)
**Insurance · 06/2025 – Present**

*Technical lead and primary architect for the team's largest cross-org initiatives — Identity, SRE, Network, Database Platform, and Developer Engineering.*

- **Artifactory reliability turnaround** — investigated recurring production failures and drove remediation across platform, config, and operations; improved from **~1 major incident/month to four-nines (99.99%) Artifactory availability SLO** completion
- **Technical lead, JFrog SaaS POC (Phase 4)** — validated Python/Java/Go publishing at 5,000 repos / 5,000 parallel artifacts; outcomes drive GEICO's enterprise artifact-management roadmap
- **Architected Entra ID auth** for `amp-control-plane` via cross-team RFC — separated NP/PD access and aligned with corporate SSO / service-to-service standards
- **Zero-downtime platform upgrades** — built automation pipeline for rolling Artifactory (7.111.12 → 7.146.8) and X-Ray (3.131.20 → 3.143.12) upgrades across Package Registry and Martech tenants on AKS with **zero customer impact**
- **Production incident leadership** — packet-level RCA and cross-team fix for Azure Firewall TLS DPI against S3-backed repos; owned CoE for April 2026 Azure East US outage (NOCIM-11695); AMP on-call lead
- **AI-assisted platform ops** — introduced MCP-based tooling (JFrog, Slack) and agent skills for support triage, RCA, and runbook workflows

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

- **Platform & DevOps:** CI/CD, build/release engineering, artifact management (JFrog, Nexus, ACR), Kubernetes/AKS, Terraform, Helm
- **Cloud:** AWS, Azure (Entra ID, Azure Firewall, AKS), multi-region HA, Docker
- **Security & compliance:** SOC 2 Type II, Vault, Azure Key Vault, SonarCloud, OIDC/RBAC, audit remediation
- **Leadership:** Staff-IC technical lead, cross-org RFCs, on-call/incident ownership, global team coordination
- **AI (supplemental):** OpenClaw plugin/runtime integration, AgentOps/Langfuse observability, MCP integrations, multi-agent systems

---

## Technical Skills

| Category | Technologies |
|----------|--------------|
| **Cloud & Platform** | AWS, Azure (AKS, ACR, Entra ID, Azure Firewall), Kubernetes, Helm, Terraform, Docker, OpenStack |
| **CI/CD & Artifacts** | Jenkins, GitHub Actions, Azure DevOps, ArgoCD, Bitrise, JFrog Artifactory/X-Ray/SaaS, Nexus, ACR |
| **Languages & Build** | Python, Go, Java, Shell, Groovy, Maven, Gradle, TypeScript, C/C++ |
| **Security** | SOC 2 Type II, HashiCorp Vault, Azure Key Vault, SonarCloud, OIDC, Entra ID |
| **AI / LLM** | OpenClaw, AgentOps, Langfuse, MCP servers, LangGraph, Playwright agents, Claude/GPT/Gemini, Ollama, vLLM |

---

## Education

**Purdue University** — MS, Artificial Intelligence *(In Progress)* · ECE 50874/59500: led OpenClaw cost-aware runtime plugin (final project), LLM-augmented software engineering

**UCLA** — BS, Computer Science *(Minor: Mathematics & Economics)*

---

## Additional

**Work Authorization:** U.S. Citizen
