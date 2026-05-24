# Ming Jia

**34500 Bentley Ct., Fremont, CA 94555**  
**(626) 354-7866** · **mailming@gmail.com**

---

## Summary

Senior platform engineer and AI builder pursuing a Master of Science in Artificial Intelligence at Purdue University, with 20+ years designing CI/CD, package management, and high-availability infrastructure across AWS, Azure, and Kubernetes. Currently Senior Engineer on GEICO's Artifact Management Platform team, where I'm driving the JFrog SaaS POC, Entra ID authentication design for the internal control plane, and the team's adoption of AI-assisted operations through Model Context Protocol (MCP) servers for JFrog, Slack, and the internal support runbook stack. In parallel, I research and prototype LLM agent systems — including a cost/latency/reliability-aware agent runtime ("AgentOne") and LLM-powered N-version programming — turning DevOps experience into agentic-workflow engineering. Previously Staff Release Engineer at Navan, where I led SOC 2 Type II remediation and platform hardening for IPO readiness.

---

## Key Competencies

- **LLM & AI agent engineering:** agent runtime design (planning loop, budget enforcement, model routing, graceful degradation), prompt engineering, RAG, multi-LLM evaluation, LLM observability and cost tracking
- **Model Context Protocol (MCP):** authoring and integrating MCP servers (JFrog, Slack, Gemini, browser, internal-support) to give coding agents safe access to enterprise systems
- **Cloud & platform engineering:** AWS, Azure (AKS, ACR, Azure Firewall, Entra ID), Kubernetes/Helm, Terraform, OpenStack, Docker — multi-region high availability
- **Artifact and package management at scale:** JFrog Artifactory HA, X-Ray, JFrog Catalog, JFrog SaaS, Azure Container Registry, Nexus
- **CI/CD & developer experience:** GitHub Actions, Azure DevOps Pipelines, Jenkins, ArgoCD, Bitrise, OIDC pipeline auth, paved-road developer platforms
- **Security & compliance:** SOC 2 Type II remediation, secrets management (HashiCorp Vault, Azure Key Vault), static analysis (SonarCloud, X-Ray), Entra ID / OIDC, audit readiness
- **Leadership:** cross-functional collaboration with security, identity, SRE, and data-platform teams; on-call rotation ownership; mentoring and technical writing (RFCs, runbooks, CoEs)

---

## Technical Skills

| Category | Technologies |
|----------|--------------|
| **AI / LLMs** | OpenAI GPT, Anthropic Claude, Google Gemini, Ollama, vLLM, local & remote model routing |
| **AI Tooling & Frameworks** | Model Context Protocol (MCP) servers, LangChain, LangGraph, AutoGen, CrewAI, Anthropic Agent Skills, Cursor agents, Langfuse, AgentOps, Playwright agent bridges |
| **AI Engineering Patterns** | Agent planning/execution loops, budget-aware prompting, N-version LLM programming, RAG, prompt engineering, structured telemetry, deterministic replay |
| **Build & Scripting** | Maven, Gradle, Ant, Python, Shell (Bash), Groovy, Ruby, Xcodebuild, MSBuild |
| **Programming** | Python, Go, TypeScript, JavaScript, Java, C/C++, SQL, Objective-C, J2EE |
| **Cloud & Infrastructure** | AWS (EC2, S3, EMR, EKS), Azure (AKS, ACR, Azure Firewall, Entra ID), Kubernetes, Helm, Terraform, OpenStack, Docker, Vagrant, Chef |
| **CI/CD & DevOps Tools** | GitHub Actions, Azure DevOps Pipelines, Jenkins, ArgoCD, Bitrise, TeamCity, CruiseControl, Git, Subversion |
| **Artifact & Package Management** | JFrog Artifactory HA, JFrog X-Ray, JFrog Catalog, JFrog SaaS, JFrog CLI, JFrog Workers, Nexus, Azure Container Registry |
| **Security & Compliance** | SOC 2 Type II, HashiCorp Vault, Azure Key Vault, SonarCloud, OIDC, Entra ID/Azure AD, RBAC, secrets rotation, pipeline security scanning |
| **Observability & Data** | Grafana, PostgreSQL, Valkey/Redis, MongoDB, Hadoop, Oracle, MySQL |
| **Application Servers** | Tomcat, Apache, Jetty, JBoss, WebLogic, IIS, NGINX |
| **Operating Systems** | Linux (Ubuntu, Red Hat, CentOS), macOS, Solaris, Windows Server |

---

## Work Experience

### Senior Engineer — GEICO, Artifact Management Platform (Developer Engineering)
**Insurance · 06/2025 – Present**

*AI-assisted platform operations*
- Integrated the JFrog MCP server into the team's developer environment and authored the AMP team's Slack MCP integration guidelines, giving coding agents safe, audited access to package-registry telemetry, runbooks, and support cases
- Adopted and contributed to internal Cursor / Claude "agent skills" for the team's support workflow (`solve-case`, `close-case`, `build-kb`), shortening incident triage and runbook hygiene cycles and demonstrating how AI agents can run production-adjacent operations under guardrails
- Used AI agents to drive deeper root-cause analyses (e.g., the Azure Firewall TLS deep-packet-inspection issue below) and to draft RFCs, runbooks, and Correction-of-Errors documents

*Platform engineering*
- Senior engineer on the Artifact Management Platform (AMP) / Package Management team, operating the JFrog Artifactory HA, X-Ray, and JFrog Catalog stacks that serve as GEICO's enterprise package registry across non-prod and production on Azure Kubernetes Service (AKS)
- Drove rolling upgrades of Artifactory (7.111.12 → 7.125.11 → 7.146.8) and X-Ray (3.131.20 → 3.143.12) across the Package Registry and Martech tenants with documented runbooks and minimal customer impact
- Co-led the JFrog SaaS Proof of Concept (Phases 1–4): authored reusable GitHub Actions workflows to publish Python, Java, and Go artifacts to JFrog SaaS, defined publish/promotion patterns, and validated scale (5,000 repos / 5,000 mixed artifacts in parallel)
- Designed and authored the Entra ID (Azure AD) authentication RFC for the `amp-control-plane` service, defining NP/PD access boundaries and bridging the platform with corporate SSO, ZTNA, and APISIX/APIM service-to-service auth standards
- Deployed `amp-control-plane` to ACS production with HashiCorp Vault integration, PostgreSQL provisioning via internal "Club" blueprints, and CRQ-managed change control
- Diagnosed and resolved an Azure Firewall TLS deep-packet-inspection issue that was breaking S3-backed remote JFrog repositories (Debian, GitHub proxies); produced a packet-level root cause and drove the SSL inspection bypass through the network team
- Authored the post-incident Correction of Errors for NOCIM-11695 (Azure East US outage, April 2026) and owned on-call rotation for the AMP team
- Built GitHub Actions reusable templates for JFrog CLI install/auth, generic file uploads, Docker pull testing, and OIDC migration patterns for the SDK Pipelines team
- Wrote runbooks for AKS PDB-aware upgrades, Grafana dashboards, X-Ray persistent-volume fixes, JFrog Workers / Circle of Trust setup, and Artifactory release management
- Partnered with Identity, Database Platform, and SRE teams to rotate `SRV-JFROG-NP/PD` service accounts, provision PostgreSQL roles, and drive the consolidation KPI across `packageregistry`, `artifactory-pd`, and Azure Container Registry

### Staff Release Engineer / DevOps — Navan (formerly TripActions)
**E-Commerce · 01/2022 – 04/2025**

- Led SOC 2 Type II audit remediation with security, compliance, and engineering teams; hardened build, release, and AWS infrastructure to support Navan's IPO and ongoing compliance
- Deployed and integrated HashiCorp Vault for centralized secrets management and SonarCloud for static code analysis and security scanning across CI/CD pipelines
- Built and maintained continuous delivery for the company's core web application and data systems on AWS
- Owned SCM and release engineering for the engineering organization; optimized release processes across AWS environments
- Built mobile CI/CD pipelines with Bitrise to automate App Store and Google Play deployments
- Responded rapidly to pipeline failures and production incidents; performed root-cause analysis and drove permanent fixes

### Lead Release Engineer — Turn / Amobee
**Ad Technology · 12/2015 – 11/2021**

- Led a team of 2 release engineers and 5 offshore NOC engineers, scaling release operations for a ~500-person engineering organization
- Redesigned and migrated Jenkins to a highly available, scalable architecture—reducing unplanned outages from hours per week to under 5 minutes of planned downtime per month, improving UI response from 12s to 0.5s per page, and saving $500K+/year vs. enterprise CloudBees licensing
- Redesigned and migrated Nexus with redundant HA architecture—eliminating unplanned outages post-migration and saving $100K+/year vs. enterprise Sonatype licensing
- Managed SCM and application deployments to thousands of production servers worldwide
- Built tools and automation to enable rapid, reliable deployment across production environments
- Enforced and improved release processes; served in a hands-on Technical Operations role for production systems

### Sr. Software Engineer — Skytree
**Machine Learning · 04/2014 – 11/2015**

- Designed and implemented end-to-end Continuous Integration and Continuous Delivery systems
- Built automation tools to accelerate the development lifecycle and dynamic cluster provisioning on AWS (EC2, S3, EMR)
- Designed and implemented a PaaS tool for on-demand environment provisioning
- Introduced Scrum and led the development team through agile adoption using Jira

### Sr. Software Engineer — Walmart Labs
**E-Commerce · 03/2013 – 04/2014**

- Built, released, and automated deployments into Dev, QA, and internal production environments
- Operated, monitored, and administered multiple production systems and internal tools
- Provided build, release, and infrastructure support across engineering teams in an agile environment

### Software Engineer — Macrovision / Rovi
**Digital Media · 11/2009 – 02/2013**

- Defined and maintained configuration management, build/release, and change management across 20+ projects with four domestic and international teams
- Led server layout design and deployment procedures for server, web, and mobile applications
- Supported Hadoop, MapReduce, and MongoDB system setup and operations
- Automated builds (Maven, Ant, xcodebuild, MSBuild) and CI pipelines (TeamCity, Jenkins)
- Built a configuration management portal with source archives, build metadata, and automated release notes
- Automated Tomcat deployments via Shell scripting; developed Python system tools and RPM-based installations
- Established and maintained company Git repositories

### SCM Manager — Helio / Virgin Mobile USA / Sprint
**Telecommunications · 02/2007 – 10/2009**

- Led server layout design and deployment procedures across multiple product lines
- Administered a 10+ server Linux dev lab; implemented VM automation via Kickstart
- Built CI pipelines with CruiseControl and Hudson/Jenkins; automated JBoss deployments with Shell, Perl, and Python
- Evaluated and deployed defect tracking systems (Jira, Trac, Bugzilla, Mantis); implemented Trac and Bugzilla for dev and QA
- Created a configuration management portal and continuous deployment workflows using ControlTier

### Software Developer — XLDynamics
**01/2005 – 02/2007**

- Built and configured core development systems across Linux, Unix, and Windows
- Created Shell scripts to monitor, test, and install software on Linux servers
- Developed C++ XML/SOAP applications and HTML/JavaScript web interfaces
- Resolved build and release issues and tracked software changes across multiple projects

---

## Selected AI / Agent Projects

### Cost-Aware Runtime for OpenClaw Browser Agents — Purdue ECE 50874/59500, Team Final Project (2026)
- Co-authored an IEEE-style final paper, *"Design and Evaluation of a Cost-Aware Runtime for OpenClaw Browser Agents"*, with three Purdue ECE teammates
- Contributed to the runtime design that treats token cost, dollar spend, tool-call count, and wall-clock latency as first-class budgets and applies explicit termination policies (stop-and-summarize, ask-human, best-effort degrade) when budgets are exhausted

### AgentOne — Cost / Latency / Reliability-Aware Agent Runtime (2026)
- Authored the requirements and architecture for an agent runtime that exposes a stable REST API and CLI, runs a planning/execution loop over repo / API / document tools, and continuously enforces budgets (max tokens, dollars, tool calls, retries, wall-clock)
- Designed model routing across local backends (Ollama, vLLM) and a remote gateway, with budget-aware prompting and graceful degradation; specified structured telemetry (per-run cost breakdown, token counts, retry paths, latency distribution) and a benchmark suite of realistic agent tasks (CI triage, dependency-bump, breaking-change summarization)
- Defined the system as a set of cooperating engines — API Engine, Management Engine, Extension Engine, LLM Calling Engine, Translator, Prediction Agent, Learning Agent, User Profile, and Credential Store — backed by PostgreSQL ([github.com/mailming/AgentOne](https://github.com/mailming/AgentOne))

### LLM-Powered N-Version Programming — Purdue ECE 50874 Lab 2 (2026)
- Used three different LLMs to generate three independent implementations of the Avalon tax-code engine in Python, Go, and C++, then ran 10,000 reserved test cases through each version and built a 2-out-of-3 agreement table
- Authored the diversity strategy and the analysis of cross-implementation divergence (floating-point representation, rounding rules, threshold handling, FIFO ordering), and wrote up reliability math (`P(failure) = p²(3 − 2p)`) for the 2oo3 voter ([github.com/mailming/purdueECE874-Lab2](https://github.com/mailming/purdueECE874-Lab2))

### Gemini Chat MCP / API Bridge (2025)
- Built a Flask + WebSocket + Tampermonkey bridge that exposes the Gemini chat web UI as a Gemini-API-compatible HTTP endpoint and an MCP server, with an example Playwright client and a Python SDK ([github.com/mailming/gemini-chat-userscript](https://github.com/mailming/gemini-chat-userscript))

### Applied AI / Agent Study
- Active study and contribution to LLM observability and agent tooling: forks and PRs against `langfuse`, `agentops`, Browser-MCP, `openclaw`, `minimind` (training a 26M-parameter GPT from scratch), Anthropic's prompt-engineering tutorial, and multi-agent finance projects (`TradingAgents`, `ai-hedge-fund`)

---

## Education

**Purdue University** — Master of Science, Artificial Intelligence *(In Progress)*  
*Coursework:* ECE 50874/59500 Software Reliability & LLM-Augmented Engineering (Redundant Designs in Software, LLM-Powered N-Version Programming, Cost-Aware Agent Runtimes)

**University of California, Los Angeles (UCLA)** — Bachelor of Science, Computer Science  
*Minor: Mathematics and Economics*

---

## Additional

**Work Authorization:** U.S. Citizen
