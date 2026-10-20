# Ming Jia

**34500 Bentley Ct., Fremont, CA 94555**  
**(626) 354-7866** · **mailming@gmail.com**  
**LinkedIn:** [linkedin.com/in/mailming](https://www.linkedin.com/in/mailming) · **GitHub:** [github.com/mailming](https://github.com/mailming) · **Jiadroid:** [github.com/mailming/jiadroid](https://github.com/mailming/jiadroid)

---

## Summary

Staff-scope platform engineer and AI builder with 20+ years across CI/CD, artifact management, and high-availability infrastructure on AWS, Azure, and Kubernetes. At GEICO Artifact Management Platform: drove Artifactory to **four-nines (99.99%) SLO**, shipped **Load Healer Reactive** (OUTAGE → HTTP 429 on NP/PD2), and lead **Martech → JFrog SaaS cutover** (Jan 30 hard date) across MAP, CDP, Billing, and Payments with `amp-migrate` for OIDC/repo-settings. Invited to GEICO's Claude Code pilot; built the **Cursor × Claude Code MCP bridge** and production MCP/agent skills. Founder of **[Jiadroid](https://github.com/mailming/jiadroid)** (phone-as-robot-brain); led **OpenClaw cost-aware runtime** (Purdue ECE 50874). Previously Staff Release Engineer at Navan (SOC 2 / IPO); $600K+/yr savings via Jenkins/Nexus HA at Turn/Amobee. MS AI @ Purdue; founder of [SmartTuna](https://smarttuna.ai/). U.S. Citizen.

---

## Work Experience

### Senior Engineer — GEICO, Artifact Management Platform (Developer Engineering)
**Insurance · 06/2025 – Present** · Staff-IC tech lead for AMP cross-org initiatives (Identity, SRE, Network, DE)

*AI initiatives — GEICO DE AI Showcase 2026*

- **Claude Agent SDK / MCP portfolio**: Slack triage prototype; AI-powered CI/CD / **`amp-migrate`** cutover path; Claude Code AMP/JFrog plugin; AI-consumable artifact-auth ADR
- **Cursor × Claude Code MCP bridge** — Claude Code pilot; enterprise Slack MCP credential reuse; JFrog/Slack/ADO/GitHub MCP servers + agent skills (`solve-case`, `close-case`, `build-kb`); Slack maintenance-announcement skill
- **AI-augmented engineering practice** — production PRs and packet-level RCAs co-authored with Claude Code / Cursor

*Platform engineering*

- **Artifactory reliability**: ~1 major incident/month → **99.99% SLO**; upgraded to **7.161.15**; AMP on-call lead
- **Load Healer Reactive** (PR #109/#111) — NP validated + **PD2** deployed; noisy-neighbor OUTAGE → HTTP 429 instead of node failure
- **Martech-off / JFrog SaaS cutover** (Jan 30) — migration channels + kickoffs for MAP, CDP, Billing, Payments, Bolt·Athena; SaaS POC lead (11 package types; 5,000×5,000 load test)
- **Entra ID auth for `amp-control-plane`** (Go JWT + APIM); ACS production deploy
- **CoE author**: NOCIM-11695, NOCIM-12455, **NOCIM-13154** (MarTech PD upgrade), **NOCIM-13213** (router OOM); PD Phase 1 stability; TLS renewals **&lt;1 min** outage

### Staff Release Engineer / DevOps — Navan (formerly TripActions)
**E-Commerce · 01/2022 – 04/2025**

- Led **SOC 2 Type II** remediation; Vault + SonarCloud for **IPO readiness**
- Owned SCM/release engineering; AWS CD; Bitrise mobile CI/CD

### Lead Release Engineer — Turn / Amobee
**Ad Technology · 12/2015 – 11/2021**

- Led 2 REs + 5 offshore NOC; ~500-engineer org; thousands of servers worldwide
- **Jenkins HA** + **Nexus HA** — unplanned outages eliminated; **$600K+/yr** vs enterprise licensing

### Sr. Software Engineer — Skytree
**Machine Learning · 04/2014 – 11/2015** — CI/CD; AWS EMR dynamic clusters; on-demand PaaS

### Sr. Software Engineer — Walmart Labs
**E-Commerce · 03/2013 – 04/2014** — Build/release Dev→Prod

### Software Engineer — Macrovision / Rovi
**Digital Media · 11/2009 – 02/2013** — CM across 20+ projects; Hadoop/MongoDB; company Git

### SCM Manager — Helio / Virgin Mobile USA / Sprint
**Telecommunications · 02/2007 – 10/2009** — CI/CD; VM + JBoss automation

### Software Developer — XLDynamics
**01/2005 – 02/2007** — Build/release; C++ XML/SOAP; Shell tooling

---

## Selected Projects

### Jiadroid — Founder ([github.com/mailming/jiadroid](https://github.com/mailming/jiadroid))
Phone-as-robot-brain protocol · ESP32-S3 2WD firmware (Wi-Fi / USB-C / OTA) · Follow Me on Android+iOS · duck + rover sims (MuJoCo)

### OpenClaw Cost-Aware Runtime — Purdue ECE 50874/59500 (2026)
***Project lead & primary implementer*** · [github.com/mailming/openclaw](https://github.com/mailming/openclaw/tree/feature/llm-insights-manual-pricing)

- Token/cost/step budgets + policy at step boundaries; AgentOps + Langfuse; LLM Insights gateway

### SmartTuna — Founder ([smarttuna.ai](https://smarttuna.ai/))
LangGraph multi-agent stock analysis · Python + Astro UI

---

## Key Competencies

- **AI engineering for platform ops:** Claude Agent SDK / Claude Code plugins, migration agents (`amp-migrate`), AI-consumable runbooks & ADRs, agent triage/RCA, LangGraph
- **MCP & coding-agent integration:** MCP servers; Cursor / Claude skills; enterprise credential bridging
- **Embodied / Physical AI:** Jiadroid protocol, ESP32 firmware, vision Follow Me, multi-body sims
- **Platform & DevOps:** CI/CD, Artifactory HA / X-Ray / SaaS, Load Healer, Kubernetes/AKS, Terraform, Helm
- **Cloud & security:** AWS, Azure (Entra ID, Firewall, AKS, ACS), SOC 2, Vault, OIDC
- **Leadership:** Staff-IC tech lead, cross-org cutover programs, on-call/incident ownership

---

## Technical Skills

| Category | Technologies |
|----------|--------------|
| **Cloud & Platform** | AWS, Azure (AKS, ACR, Entra ID, Azure Firewall), Kubernetes, Helm, Terraform, Docker |
| **CI/CD & Artifacts** | Jenkins, GitHub Actions, Azure DevOps, ArgoCD, JFrog Artifactory/X-Ray/SaaS, Nexus, ACR |
| **Languages & Build** | Python, Go, Java, Shell, TypeScript, Kotlin, Swift, Groovy, Maven, Gradle, C/C++ |
| **Security** | SOC 2 Type II, HashiCorp Vault, Azure Key Vault, SonarCloud, OIDC, Entra ID |
| **AI / LLM / Embodied** | Claude Agent SDK, Claude Code, Cursor MCP, LangGraph, AgentOps, Langfuse, OpenClaw, Jiadroid, ESP32, Ollama, vLLM |

---

## Education

**Purdue University** — MS, Artificial Intelligence *(In Progress)* · ECE 50874/59500 OpenClaw; CNIT 57500 Data Analysis (Fall 2026)

**UCLA** — BS, Computer Science *(Minor: Mathematics & Economics)*

---

## Additional

**Work Authorization:** U.S. Citizen
