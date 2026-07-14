# Work Evidence Catalog — Ming Jia

*Last updated: 2026-07-14. Sourced from Slack (U08V0N1LMU2), GitHub (`jiaming_geico` / `mailming`), and ADO (Developer Engineering). Use this as the source-of-truth when tailoring resumes, one-pagers, and interview STAR stories.*

---

## Summary stats (GEICO, Jun 2025 – Jul 2026)

| Metric | Value |
|--------|-------|
| **geico-private PRs authored** | 65 total · 29 merged |
| **Primary repos** | `artifact-management-platform`, `pkg-mgmt`, `pkg-jfrog-charts`, `repo-manager-worker`, `hut8-workspaces` |
| **ADO work items (assigned / activity)** | 50+ in Developer Engineering |
| **CoE documents authored** | NOCIM-11695 (Apr 2026 Entra-ID outage), NOCIM-12455 (npm EINTEGRITY) |
| **On-call / incident leadership** | AMP on-call lead; packet-level RCAs; ZTNA troubleshooting |

---

## 1. Platform engineering — Artifact Management Platform (AMP)

### 1.1 Reliability & availability

- Drove Artifactory from **~1 major incident/month → four-nines (99.99%) availability SLO** (ongoing; AMP on-call lead).
- **PD Phase 1 stability** (Jul 2026): cluster investigation on PD1 East + PD2 West; identified undersized resource requests, broken Xray HPA, system-pool pressure. Shipped PR with sizing/HPA/priority-class fixes. **ADO AB#12711221** · `pkg-jfrog-charts` PR #88.
- **Artifactory 7.111.12 → 7.146.8** + X-Ray 3.131.20 → 3.143.12 upgrade for packageregistry. **ADO AB#12104170** · `pkg-jfrog-charts` PR #81.
- **Stdout JSON logging** rollout for Artifactory + Xray (NP, PD1, PD2). **ADO AB#12289049** · PRs #82, #85.
- **TLS cert renewal runbook** for artifactory-pd-infra. **ADO AB#12450200** · PR #84.
- **Production TLS cert renewal** (Jul 13, 2026): coordinated F5 + AKS ingress secret update for `packageregistry.geico.net`; posted maintenance comms to `#help-pkg-mgmt`; **<1 min outage**; CRQ000000930431.
- **PD1 AKS SP rotation** + post-incident validation (Jul 2026).
- **Grafana dashboards runbook** (AB#11008552).

### 1.2 amp-control-plane (Go control plane on ACS)

- **Deployed `amp-control-plane` to ACS production** (May 2026). **ADO AB#12142920 / AB#12162997** · `artifact-management-platform` PR #371.
- **Entra ID user-delegated auth** for GHE group on NP: Go JWT middleware + APISIX custom-jwt + APIM defense-in-depth. Cross-team work with Identity (Srinivasa Reddy), APIM (Rajasree Gunda). **ADO AB#12178284** · PRs #440, #457.
- Vault service annotation fix for PD spec. PR #377.
- Host swap in `repo-manager-worker` for PD endpoint. PR #30.
- ACS prod deployment guidance sought from PaaS (Lianyi Ma); Club MCP server integration per paved-roads docs.

### 1.3 JFrog SaaS POC (technical lead)

- **Three GitHub Actions workflows** validating **all 11 supported JFrog package types** end-to-end on `geicoeast.jfrog.io`:
  - `jfrog-saas-poc-demo.yml` — 11 parallel jobs (Maven, Gradle, npm, PyPI, Go, NuGet, Docker, Helm, Debian, RPM, Generic)
  - `jfrog-saas-poc-helloworld.yml` — 4 languages with committed hello-world projects
  - `jfrog-saas-poc-real-artifacts.yml` — re-publish real GEICO artifacts from packageregistry via OIDC
- **OIDC smoke-test composite action** (`.github/actions/jfrog-oidc-smoke-test`) — proves GitHub-OIDC → JFrog token exchange independent of repo provisioning.
- **`.github/repo-settings.yaml`** for amp-control-plane-driven JFrog SaaS resource provisioning. **ADO AB#12143170** (Closed).
- **ADO pipeline** for JFrog SaaS POC across 4 languages. **ADO AB#12218515** · PR #32.
- **JFrog SaaS POC setup and operations guide** (docs in `pkg-mgmt`).
- **SaaS load test** characterization: 5,000 repos / 5,000 parallel artifacts (target envelope for cutover).
- Co-authored with Cursor / Claude Sonnet agents on workflow debugging (Maven settings.xml, npm cache, Kaniko OIDC, ar-based .deb construction).

### 1.4 Documentation & runbooks

| ADO | Title | Repo / PR |
|-----|-------|-----------|
| AB#12711206 | ZTNA CLI troubleshooting runbook for packageregistry | AMP PR #478 · `pkg-jfrog-charts` PR #89 |
| AB#12695325 | Service principal and credential rotation runbook | AMP PR #475 |
| AB#12538848 | packageregistry repo creation skill | AMP PR #466 (open) |
| AB#11652168 | Martech legacy NP URL and onboarding entitlements | AMP PR #181 |
| AB#11222466 | Artifactory 7.125.11 release notes | AMP PR #29 |
| AB#11533442 | Slack MCP integration doc and guideline | AMP PR #169 |
| — | JFrog Package Registry onboarding guide | AMP PR #115 |
| — | AKS upgrade PDB runbook | AMP PR #113 |
| — | RTFS and Circle of Trust setup | `pkg-jfrog-charts` PR #69 |
| — | Debian package template + sample | AMP PRs #80, #82 |

### 1.5 OIDC / PCI migration (earlier)

- **SDK pipelines OIDC migration** for `packageregistry.geico.net` (7 pipeline stages, Go 1.25, docker pull+run strategy). **ADO #10277904** · `hut8-workspaces` (co-authored).

---

## 2. AI / agent engineering at GEICO

### 2.1 DE AI Showcase 2026 portfolio (in flight)

Four initiatives entered into GEICO's org-wide DE AI Showcase (282 DE associates):

1. **Claude Agent SDK triage prototype** for `#help-pkg-mgmt` Slack channel
2. **AI-powered CI/CD migration engine** — opens per-team PRs for JFrog SaaS cutover (target: 100% of inventoried pipelines)
3. **Claude Code plugin for AMP/JFrog** — plain-English Artifactory ops; targeting `developer-agent-hub` marketplace
4. **AI-consumable artifact-auth ADR** — any AI agent can onboard external teams without AMP hand-holding

### 2.2 Cursor × Claude Code MCP bridge

- Invited to **GEICO Claude Code pilot** (Jack Crissey's team).
- Authored step-by-step guide to **decrypt Cursor's encrypted Slack MCP token** from `state.vscdb` and inject into Claude Code via `claude mcp add` — first bridge between Cursor and Claude Code enterprise auth at GEICO.
- Shared with pilot team; advocated for official Slack MCP for Claude (Apr–May 2026).
- Researched Cursor background agents vs. local Claude Code for secure enterprise use (Sep 2025 DM with Alexander Galushka) — recommended local CLI agents over cloud background agents for ADO/network red-tape reasons.

### 2.3 MCP servers & agent skills (production)

- Shipped **Club MCP server config** into `amp-control-plane`.
- Introduced **JFrog / Slack / ADO / GitHub MCP servers** and Claude/Cursor agent skills: `solve-case`, `close-case`, `build-kb` across AMP support, RCA, and runbook workflows.
- Follow-on Club skills + Cursor agent hooks via `club-developer-agent-plugins`.

### 2.4 AI-augmented engineering practice

- Every May–Jul 2026 AMP / pkg-mgmt PR authored with **Claude Code or Cursor** (Entra ID auth, JFrog SaaS POC workflows, ACS prod deployment, PD stability, runbooks).
- Surgical Slack RCAs are **AI-augmented end-to-end** (packet-level Azure Firewall TLS DPI, npm EINTEGRITY, ZTNA policy debugging).

---

## 3. Incident leadership & RCA (resume-ready STAR stories)

### NOCIM-12455 — npm EINTEGRITY / Chainguard remote (Jun–Jul 2026)

- **Situation:** `bolt-npm-virtual` consumers hit `npm ERR! code EINTEGRITY` after Chainguard remote returned metadata ≠ tarball checksums.
- **Action:** Direct SHA512 tarball checks against `chainguard-npm-remote` vs `shared-npm-remote`; identified upstream 403 on package paths (expired creds); reordered virtual repo resolution; rotated credentials; authored **CoE** (AB#12524243, PR #464).
- **Result:** Workaround (shared-npm-remote before chainguard) restored consumers; documented root cause + prevention for Problem Management.

### NOCIM-11695 — Entra-ID-driven Artifactory outage (Apr 2026)

- **CoE author** for April 2026 Entra-ID-driven Artifactory outage. PR #363.

### ZTNA / packageregistry CLI timeouts (Jul 2026)

- Reproduced `jf docker login` timeout for COSRT engineer (ADO #12711206); packet-level `curl -vvv` through Zscaler proxy; identified TLS SNI / policy issue; authored **ZTNA CLI troubleshooting runbook** (PRs #478, #89); confirmed fix with reporter.

### Azure Firewall TLS DPI — S3-backed repos

- Packet-level RCA on S3-backed Artifactory repos (Azure Firewall TLS deep packet inspection).

### JFrog Go-module cache RCAs

- Multiple production RCAs on Go module cache behavior.

### PD1 credential rotation outage (Jul 2026)

- Led annual SP rotation recovery; "Done, good to use now" within hours.

---

## 4. Slack operational footprint (selected)

| Channel | Role | Examples |
|---------|------|----------|
| `#help-pkg-mgmt` | Primary support engineer | ZTNA RCA, cert renewal comms, scope clarification (BoatUS CVE ticket), integration guide pointers |
| `#team-pkg-mgmt` | Team standups, PR reviews | PD stability PR #88, npm EINTEGRITY follow-ups, daily async standup |
| `#sig-ai-assisted-development` | AI tooling advocate | Active participant |
| DMs: Jack Crissey | Claude Code pilot | MCP bridge guide, Slack MCP advocacy |
| DMs: Rajasree Gunda, Srinivasa Reddy | Entra ID / APIM | amp-control-plane auth boundary unblock |
| DMs: Ryan Murphy | Internal mobility | R0062059 Applied AI inquiry |

---

## 5. GitHub — merged PR inventory (`jiaming_geico`)

### artifact-management-platform (15+ merged)

| PR | Title | ADO |
|----|-------|-----|
| #371 | Deploy amp-control-plane to ACS prod | AB#12142920, AB#12162997 |
| #377 | Vault service annotation for spec.pd.yaml | — |
| #378 | Comment out jfrog ping in health handler | AB#12162997 |
| #457 | Entra ID user-delegated auth for GHE group (NP) | AB#12178284 |
| #440 | Entra ID auth on amp-control-plane NP (APISIX custom-jwt) | AB#12178284 |
| #464 | CoE for NOCIM-12455 npm EINTEGRITY | AB#12524243 |
| #363 | CoE for NOCIM-11695 — Azure East US outage | — |
| #181 | Martech legacy NP URL and onboarding entitlements | AB#11652168 |
| #169 | Slack MCP integration doc | AB#11533442 |
| #115 | JFrog Package Registry onboarding guide | — |
| #113 | AKS upgrade PDB runbook | — |
| #29 | Artifactory 7.125.11 release notes | AB#11222466 |
| #11 | Grafana dashboards runbook | AB#11008552 |

### pkg-mgmt (6+ merged)

| PR | Title | ADO |
|----|-------|-----|
| #22 | JFrog SaaS POC workflows + hello-world demo projects | AB#12143170 |
| #23 | repo-settings.yaml for JFrog SaaS POC provisioning | AB#12143170 |
| #28 | Remove generic language repo from repo-settings | AB#12143170 |
| #31 | Add generic language repo to repo-settings | AB#12143170 |
| #32 | ADO pipeline for JFrog SaaS POC (OIDC) | AB#12218515 |

### pkg-jfrog-charts (8+ merged)

| PR | Title | ADO |
|----|-------|-----|
| #81 | Artifactory 7.146.8 + X-Ray 3.143.12 upgrade | AB#12104170 |
| #82 | Stdout JSON logging (NP) | AB#12289049 |
| #84 | TLS cert renewal runbook | AB#12450200 |
| #85 | Stdout JSON logging (PD1 + PD2) | AB#12289049 |
| #86 | Bump PD deploy defaults to latest chart versions | AB#12621934 |
| #69 | RTFS and Circle of Trust setup | AB#10812212 |
| #67 | Xray Helm chart 3.131.20 | AB#10181837 |
| #66 | Terraform proxy config fix (co-authored) | AB#10171954 |
| #76 | Artifactory HA on AKS, deploy workflows | AB#11577207 |

### repo-manager-worker

| PR | Title | ADO |
|----|-------|-----|
| #30 | Restore amp-control-plane host (PD) | AB#12162997 |

### Open PRs (Jul 2026)

| PR | Title | ADO |
|----|-------|-----|
| AMP #478 | ZTNA CLI troubleshooting runbook | AB#12711206 |
| AMP #477 | GenAIInn (ailens) JFrog project request | AB#12712377 |
| AMP #475 | Service principal / credential rotation runbook | AB#12695325 |
| AMP #466 | packageregistry repo creation skill | AB#12538848 |
| `pkg-jfrog-charts` #88 | PD Phase 1 stability (sizing, HPA, pool exclusion) | AB#12711221 |
| `pkg-jfrog-charts` #89 | ZTNA CLI troubleshooting runbook | — |

---

## 6. ADO work items — assigned / created (selected)

| ID | Type | Title | State |
|----|------|-------|-------|
| AB#12143170 | User Story | AMP: Push sample artifacts via GitHub workflows (JFrog CLI) | Closed |
| AB#12178284 | User Story | AMP: Implement Entra User Access Control for AMP Control Plane | New (PRs merged) |
| AB#12142920 | — | Deploy amp-control-plane to ACS prod | — |
| AB#12162997 | — | amp-control-plane PD host / health handler | — |
| AB#12218515 | — | ADO pipeline for JFrog SaaS POC (OIDC) | Closed |
| AB#12289049 | — | Stdout JSON logging Artifactory + Xray | Closed |
| AB#12450200 | — | TLS cert renewal runbook | Closed |
| AB#12524243 | Feature | CoE for NOCIM-12455 npm EINTEGRITY | Closed |
| AB#12711221 | User Story | PD Phase 1 stability — sizing, HPA, system pool exclusion | New |
| AB#12711206 | — | ZTNA CLI troubleshooting runbook | Active |
| AB#12695325 | — | Service principal / credential rotation runbook | Active |
| AB#12538848 | — | packageregistry repo creation skill | Active |

*Full activity query returned 50+ items in Developer Engineering (Jun 2025 – Jul 2026).*

---

## 7. Personal / academic AI projects (`mailming`)

| Project | Role | Highlights |
|---------|------|--------------|
| **OpenClaw cost-aware runtime** | Project lead & primary implementer | Purdue ECE 50874/59500 Team 17; token/cost/step budgets; AgentOps + Langfuse; IEEE-style report |
| **SmartTuna** ([smarttuna.ai](https://smarttuna.ai)) | Founder | LangGraph multi-agent stock analysis; Python + Astro UI |
| **AgentOne** | Builder | Multi-agent system |
| **ai-engineering-from-scratch** | Learner/builder | "Learn it. Build it. Ship it." curriculum repo |
| **job-ops** | Builder | DevOps principles applied to job hunting pipeline |
| **gemini-chat-userscript** | Builder | Gemini Chat MCP / API bridge |
| **clearmail** | Builder | AI-powered Gmail filter |
| **OpenClawAgent** | Builder | OpenClaw agent experiments |
| **Purdue ECE 874 Lab2** | Student | LLM-augmented engineering coursework |

---

## 8. Prior employers (pre-GEICO) — evidence anchors

| Employer | Role | Key metrics |
|----------|------|-------------|
| **Navan** (01/2022 – 04/2025) | Staff Release Engineer | SOC 2 Type II remediation; Vault + SonarCloud; IPO readiness; mobile CI/CD (Bitrise) |
| **Turn/Amobee** (12/2015 – 11/2021) | Lead Release Engineer | Jenkins HA ($500K+/yr saved); Nexus HA ($100K+/yr saved); 2 RE + 5 offshore NOC; ~500 engineers, thousands of servers |
| **Skytree** (04/2014 – 11/2015) | Sr. SWE | ML platform CI/CD; AWS EMR dynamic clusters; PaaS on-demand environments |
| **Walmart Labs** (03/2013 – 04/2014) | Sr. SWE | Build/release automation Dev→Prod |
| **Macrovision/Rovi** (11/2009 – 02/2013) | SWE | 20+ projects CM; Hadoop/MapReduce/MongoDB ops; company-wide Git migration |
| **Helio/Virgin/Sprint** (02/2007 – 10/2009) | SCM Manager | CI/CD (CruiseControl, Hudson/Jenkins); VM automation |

---

## 9. Resume bullet candidates (copy-paste ready)

### Platform / Release Platform (R0064074 style)

- Drove GEICO's enterprise package registry from **~1 major incident/month to 99.99% availability SLO**; AMP on-call lead and CoE author for production incidents (NOCIM-11695, NOCIM-12455).
- **Technical lead, JFrog SaaS POC**: three GitHub Actions workflows validating all 11 JFrog package types end-to-end on `geicoeast.jfrog.io`; OIDC smoke-test action; repo-settings-driven provisioning; SaaS load test at 5,000 repos / 5,000 parallel artifacts.
- **Architected Entra ID auth boundary for `amp-control-plane`** (Go JWT + APISIX + APIM); deployed to ACS production; cross-team with Identity and API Management.
- **PD Phase 1 stability** (Jul 2026): cluster forensics on dual-region AKS; fixed broken Xray HPA, undersized requests, system-pool scheduling; authored runbook + PR #88.
- Led **production TLS cert renewal** for `packageregistry.geico.net` with **<1 min outage**; coordinated F5 + ingress + customer comms (CRQ000000930431).
- Authored **10+ runbooks** (ZTNA CLI, TLS renewal, SP rotation, repo creation skill, onboarding guide, AKS PDB, Grafana dashboards).

### AI / Applied AI style

- **Cursor × Claude Code MCP bridge**: built enterprise Slack MCP credential bridge for GEICO Claude Code pilot; shared with pilot cohort.
- **MCP & agent skills in AMP production**: JFrog/Slack/ADO/GitHub MCP servers; `solve-case` / `close-case` / `build-kb` skills across support and RCA workflows.
- **DE AI Showcase 2026**: four initiatives — Claude Agent SDK triage, AI-powered CI/CD migration engine, Claude Code plugin for AMP/JFrog, AI-consumable artifact-auth ADR.
- **AI-augmented engineering practice**: every AMP/pkg-mgmt PR since May 2026 co-authored with Claude Code or Cursor; packet-level RCAs AI-augmented end-to-end.

### STAR story hooks

1. **npm EINTEGRITY / Chainguard** — virtual repo reordering, tarball forensics, CoE, consumer restore
2. **Entra ID auth for amp-control-plane** — cross-org Identity/APIM unblock, VPN vs ZTNA gap closure
3. **JFrog SaaS POC OIDC** — 11 package types, repo-settings provisioning chain, smoke-test action
4. **ZTNA packageregistry timeout** — curl forensics through Zscaler, runbook, confirmed fix same day
5. **TLS cert renewal** — dual-region AKS + F5 coordination, <1 min outage, customer comms
6. **Cursor MCP bridge** — invented workaround when official Slack MCP for Claude didn't exist

---

## 10. Gaps / in-flight (update as shipped)

- [ ] Claude Code plugin publication to `developer-agent-hub`
- [ ] Club MCP server skills + Cursor agent hooks (`club-developer-agent-plugins`)
- [ ] AI-powered CI/CD migration engine (100% pipeline inventory target)
- [ ] `pkg-jfrog-charts` PR #88 merge + PD deploy
- [ ] amp-control-plane PD Entra ID auth (AB#12178284 — NP done, PD in progress per Slack Jun 2026)
- [ ] OpenClaw cost-aware runtime blog publish (`portfolio/blog-openclaw-cost-aware-runtime.md`)

---

*Refresh this file periodically: `slack_search_public_and_private from:<@U08V0N1LMU2>`, `gh search issues is:pr author:jiaming_geico`, ADO `wit_my_work_items`.*
