# Ming Jia

**Fremont, CA** · **(626) 354-7866** · **mailming@gmail.com**  
**LinkedIn:** [linkedin.com/in/mailming](https://www.linkedin.com/in/mailming) · **GitHub:** [github.com/mailming](https://github.com/mailming)

---

## Summary

AI infrastructure and platform engineer who builds production agent systems and the reliability platforms underneath them. At GEICO, Staff-scope owner of the enterprise artifact registry: drove **99.99% availability**, shipped overload protection that returns HTTP 429 under node saturation, and lead org-wide **migration to JFrog SaaS**. Invited to the Claude Code pilot; integrated Cursor/Claude tooling and MCP into platform workflows. Side projects: **Jiadroid** (phone-as-robot-brain), **OpenClaw** cost-aware agent runtime (Purdue), **SmartTuna**. 20+ years HA platform (Navan SOC 2/IPO; Turn/Amobee Jenkins+Nexus HA, $600K+/yr savings). MS AI @ Purdue. U.S. Citizen.

---

## Selected projects

**Jiadroid** — [github.com/mailming/jiadroid](https://github.com/mailming/jiadroid) · Open phone-to-robot protocol, ESP32 firmware, and Follow Me apps so a phone can act as brain/eyes for robot bodies.

**OpenClaw cost-aware runtime** — Purdue ECE 50874 · Token/cost/step budgets and policy around browser agents without rewriting agent core.

**SmartTuna** — [smarttuna.ai](https://smarttuna.ai) · LangGraph multi-agent stock analysis.

---

## Work Experience

### Senior Engineer — GEICO, Artifact Management (Developer Engineering)
**06/2025 – Present** · Staff-IC tech lead for the enterprise package registry and related developer platforms

- Drove Artifactory from ~1 major incident/month to a **99.99% availability SLO**; on-call lead and primary author of post-incident write-ups
- Shipped **concurrency overload protection** so a saturated node throttles the noisy client with HTTP 429 instead of failing for everyone; validated in non-prod and rolled out to production
- Leading **registry consolidation to JFrog SaaS** — partner with consumer teams, run migration tooling (OIDC + repo provisioning), and previously led the SaaS POC (11 package types end-to-end; large-scale load test)
- Built **Entra ID auth** for the registry control-plane service (Go + API gateway) and deployed it to production on Azure
- Productionized **Claude Code / Cursor / MCP** for support and ops (Slack triage, agent skills, credential bridge for the Claude Code pilot)

### Staff Release Engineer / DevOps — Navan
**01/2022 – 04/2025**

- Led **SOC 2 Type II** remediation and secrets/quality gates for **IPO readiness** (Vault, SonarCloud)
- Owned release engineering and AWS CD; Bitrise mobile CI/CD

### Lead Release Engineer — Turn / Amobee
**12/2015 – 11/2021**

- Led release ops for a ~500-engineer org on thousands of servers worldwide
- **Jenkins HA** and **Nexus HA** migrations — eliminated unplanned outages; **$600K+/yr** vs enterprise licensing

### Earlier roles
**Skytree** (ML startup) · **Walmart Labs** · **Macrovision/Rovi** · **Helio/Virgin/Sprint** · **XLDynamics** — CI/CD, build/release, and platform engineering (2005–2015)

---

## Skills

| Category | Technologies |
|----------|--------------|
| **AI / Agents** | Claude Agent SDK, Claude Code, Cursor, MCP, LangGraph, agent evals & cost governance |
| **Physical AI** | Phone–robot protocols, ESP32, computer-vision Follow Me, multi-body simulation |
| **Platform** | Kubernetes, Helm, Terraform, AWS, Azure, GitHub Actions, Azure DevOps, JFrog Artifactory |
| **Languages** | Python, Go, TypeScript, Java, Shell |
| **Security** | SOC 2, Vault, OIDC, Entra ID |

---

## Education

**Purdue University** — MS, Artificial Intelligence *(In Progress)*  
**UCLA** — BS, Computer Science *(Minors: Mathematics & Economics)*

**Work Authorization:** U.S. Citizen
