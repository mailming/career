# Ming Jia

**Fremont, CA** · **(626) 354-7866** · **mailming@gmail.com**  
**LinkedIn:** [linkedin.com/in/mailming](https://www.linkedin.com/in/mailming) · **GitHub:** [github.com/mailming](https://github.com/mailming)

---

## Summary

Staff-scope Release Platform / DevOps engineer with **20+ years building internal developer platforms** that serve hundreds-to-thousands of engineers. Currently Senior Engineer (Staff-IC scope) on **GEICO's Artifact Management Platform** — the package-registry control plane every one of GEICO's 3000+ engineers depends on — where I drove Artifactory from **~1 major incident/month to four-nines (99.99%) availability SLO**, architected the **Entra ID auth boundary for `amp-control-plane`** (Go JWT middleware + APIM defense-in-depth), and am **technical lead for the JFrog SaaS POC** (GitHub Actions workflows validating all 11 supported package types end-to-end; load test at 5,000 repos / 5,000 parallel artifacts). Previously **Lead Release Engineer at Turn/Amobee**: led HA Jenkins + HA Nexus migrations for a ~500-engineer org deploying to thousands of production servers, **saving $600K+/yr in enterprise license costs**. **Staff Release Engineer at Navan** through SOC 2 Type II remediation and IPO readiness (HashiCorp Vault + SonarCloud across CI/CD). Comfortable across the full DevOps stack: **Go**, Python, TypeScript, Shell; **Kubernetes / AKS / Helm**, ArgoCD, **Azure DevOps Pipelines and GitHub Actions**; deep packet-level network debugging (Azure Firewall TLS DPI RCA, JFrog Go-module cache RCAs). MS in AI at Purdue (in progress) and shipping an **AI-powered CI/CD migration engine** for GEICO's JFrog SaaS cutover so the Release Platform itself benefits from agentic automation. U.S. Citizen.

---

## Work Experience

### Senior Engineer (Staff-IC scope) — GEICO, Artifact Management Platform (Developer Engineering)
**06/2025 – Present** · Tech lead for cross-org platform initiatives across Identity, SRE, Network, Database Platform, and DE

*Internal developer platform for 3000+ GEICO engineers — the package-registry / artifact control plane underneath every CI/CD pipeline.*

- **Artifactory reliability turnaround** — drove the package registry from **~1 major incident/month to a four-nines (99.99%) availability SLO**; AMP on-call lead, CoE author for **NOCIM-11695** (April 2026 Entra-ID-driven Artifactory outage)
- **Technical lead, JFrog SaaS POC** — three **GitHub Actions** workflows validating **all 11 supported JFrog package types** end-to-end on `geicoeast.jfrog.io`; SaaS load test at **5,000 repos / 5,000 parallel artifacts** to characterize the cutover envelope
- **Architected the Entra ID auth boundary for `amp-control-plane`** — cross-team plan with **Go JWT middleware** at the service edge and **Azure APIM** defense-in-depth; deployed `amp-control-plane` to Azure Container Service production
- **Self-service developer experience for artifact onboarding** — designed an **AI-consumable artifact-auth ADR** so any team (or AI agent) can onboard external repos without AMP hand-holding; introduced JFrog/Slack/ADO/GitHub **MCP servers** and Claude/Cursor agent skills (`solve-case`, `close-case`, `build-kb`) that automate AMP's support, RCA, and runbook workflows
- **AI-powered CI/CD migration engine** for the JFrog SaaS cutover that opens per-team PRs across the inventoried pipeline fleet (target: 100% coverage) — Release Platform itself benefiting from agentic automation
- **Production incident leadership** — packet-level **Azure Firewall TLS DPI** RCA on S3-backed Artifactory repos; multiple JFrog Go-module cache RCAs; lead on cross-org Identity/Network/SRE bridge calls

### Staff Release Engineer / DevOps — Navan (formerly TripActions)
**01/2022 – 04/2025** · Release engineering and CI/CD for a high-growth fintech/travel platform

- **SOC 2 Type II audit remediation** lead and **IPO-readiness** track — deployed **HashiCorp Vault** for secrets governance and **SonarCloud** quality gates across the CI/CD fleet
- Owned **SCM strategy and release engineering for the engineering organization**; built and maintained continuous delivery for core web and data systems on AWS
- Built **mobile CI/CD on Bitrise** for App Store and Google Play; drove rapid RCA on pipeline and production incidents

### Lead Release Engineer — Turn / Amobee
**12/2015 – 11/2021** · Release platform and global deployment for a ~500-engineer ad-tech org

- Led **2 release engineers + 5 offshore NOC engineers** across time zones; scaled release operations for an engineering org deploying to **thousands of production servers worldwide**
- **Jenkins HA migration** — cut unplanned outages from hours/week to <5 min planned downtime/month; UI latency 12s → 0.5s/page; **saved $500K+/year** vs. CloudBees enterprise licensing
- **Nexus HA migration** — eliminated unplanned outages post-migration; **saved $100K+/year** vs. Sonatype enterprise licensing
- Built deployment automation, enforced release process, and ran hands-on Technical Operations in production; mentored release engineers through Jenkins HA and Nexus HA cutovers

### Sr. Software Engineer — Skytree
**04/2014 – 11/2015** · Build/release for an ML platform startup

- Built end-to-end CI/CD systems, **AWS dynamic cluster provisioning** (EC2, S3, EMR), and a **PaaS tool for on-demand engineering environments**; led agile adoption and initiated Scrum process

### Sr. Software Engineer — Walmart Labs
**03/2013 – 04/2014**

- Automated build / release across Dev, QA, and production; operated and supported multiple production systems for engineering teams

### Software Engineer — Macrovision / Rovi
**11/2009 – 02/2013**

- CM / build / release / change management across **20+ projects** and four international teams; **Hadoop / MapReduce / MongoDB** operations
- Automated builds and CI (**Maven, Ant, TeamCity, Jenkins**); built an internal CM portal with automated release notes; established company-wide Git repositories

### SCM Manager — Helio / Virgin Mobile USA / Sprint
**02/2007 – 10/2009**

- Server layout, deployment procedures, and CI/CD (**CruiseControl, Hudson/Jenkins**); VM automation, JBoss deployment automation, defect-tracking rollout (Jira / Bugzilla)

### Software Developer — XLDynamics
**01/2005 – 02/2007**

- Core dev systems on Linux / Unix / Windows; build/release automation, C++ XML/SOAP apps, Shell-based server tooling

---

## Key Competencies — Release Platform & DevOps Tooling

- **Internal developer platform engineering** — building artifact, CI/CD, and release control planes that scale from hundreds to thousands of engineers; self-service developer experiences; standardized deployment workflows
- **CI/CD and GitOps** — **Azure DevOps Pipelines, GitHub Actions, Jenkins** (HA migration, scale ops), Bitrise; ArgoCD GitOps; **Helm**-based Kubernetes rollouts
- **Kubernetes / AKS / ACS** — namespace and workload management, ingress / egress, Helm release lifecycle, container image supply chain (ACR, Artifactory Docker, X-Ray)
- **Deployment patterns** — zero-downtime HA migrations (Jenkins, Nexus, Artifactory), rolling and blue/green-style cutovers, rollback automation, package-level cutover playbooks for JFrog SaaS POC
- **Governance, policy, and compliance** — **SOC 2 Type II** audit remediation, **HashiCorp Vault**, OIDC and Entra ID auth boundaries, SonarCloud quality gates, change-gate / CRQ workflows, AI-consumable ADRs for cross-team policy alignment *(policy-as-code adjacent; ready to adopt OPA/Rego)*
- **Observability** — 99.99% availability SLO instrumentation, AMP on-call lead, packet-level network RCAs, JFrog Go-module cache RCAs, CoE / post-incident review authorship
- **Cloud & networking** — **Azure** (AKS, ACS, ACR, Entra ID, Azure Firewall, APIM), **AWS** (EC2, S3, EMR, IAM), light GCP; TCP/IP, TLS, DNS, ingress controllers, load balancing, **packet-level debugging** (Azure Firewall TLS DPI on S3-backed repos)
- **AI-augmented platform engineering** — Claude Code / Cursor / MCP shipped into AMP production; AI-powered CI/CD migration engine for the JFrog SaaS cutover; AI-co-authored RCAs and runbooks
- **Leadership** — Staff-IC tech lead at GEICO; led 2 release engineers + 5 offshore NOC at Turn/Amobee; mentor through HA migrations and AI-tooling rollout; active in `#sig-ai-assisted-development`

---

## Technical Skills

| Category | Technologies |
|----------|--------------|
| **Languages** | **Go**, Python, TypeScript, Java, Shell / Bash, Groovy, C / C++ |
| **CI/CD & Release** | **Azure DevOps Pipelines, GitHub Actions, Jenkins** (HA), ArgoCD (GitOps), Bitrise, Maven, Gradle, TeamCity |
| **Containers & Orchestration** | **Kubernetes, AKS, ACS**, Helm, Docker, container image supply chain |
| **Artifact & Registry** | JFrog Artifactory (HA + SaaS), JFrog X-Ray, JFrog Catalog, Nexus, ACR |
| **Cloud** | **Azure** (AKS, ACS, ACR, Entra ID, Azure Firewall, APIM), AWS (EC2, S3, EMR, IAM), GCP (light), OpenStack |
| **IaC & Config** | Terraform, Helm, ARM/Bicep (light), Ansible (light) |
| **Security & Governance** | SOC 2 Type II, **HashiCorp Vault**, Azure Key Vault, SonarCloud, **OIDC, Entra ID JWT auth, APIM**, policy-as-code (OPA/Rego — adopting), audit and change-gate workflows |
| **Networking & Observability** | TCP/IP, TLS, DNS, ingress controllers, load balancing; Grafana, packet-level Azure Firewall debugging, 99.99% SLO instrumentation |
| **AI / Agents (value-add)** | Claude Agent SDK, Claude Code & plugins, Cursor agents, **Model Context Protocol (MCP) servers** (JFrog, Slack, ADO, GitHub, Club), LangGraph, AgentOps, Langfuse |

---

## Education

**Purdue University** — MS, Artificial Intelligence *(In Progress)* · ECE 50874/59500: led OpenClaw cost-aware runtime plugin (final project), LLM-augmented software engineering

**UCLA** — BS, Computer Science *(Minors: Mathematics & Economics)*

---

**Work Authorization:** U.S. Citizen
