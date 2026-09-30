# Ming Jia — Platform & AI Engineer

**Fremont, CA** · mailming@gmail.com · (626) 354-7866 · [linkedin.com/in/mailming](https://www.linkedin.com/in/mailming) · [github.com/mailming](https://github.com/mailming)

Staff-scope platform engineer building production agentic systems and the reliability platforms they run on. **29 merged PRs** across GEICO's Artifact Management Platform (Jun 2025 – Jul 2026). Pursuing MS in AI at Purdue.

---

## 1. Artifactory 99.99% turnaround — *Staff-IC tech lead, AMP on-call*

- Drove Artifactory from **~1 major incident/month → four-nines (99.99%) availability SLO** — backbone for every container image, model artifact, and pipeline binary GEICO's 3000+ engineers consume.
- **PD Phase 1 stability** (Jul 2026): cluster forensics on PD1/PD2 AKS; fixed broken Xray HPA, undersized resource requests, system-pool scheduling — PR #88, AB#12711221.
- **Production TLS cert renewal** (Jul 13): coordinated F5 + dual-region ingress; **<1 min outage**; customer comms to `#help-pkg-mgmt`.
- **CoE author**: NOCIM-11695 (Apr 2026 Entra-ID outage), NOCIM-12455 (npm EINTEGRITY / Chainguard).
- **10+ runbooks**: ZTNA CLI troubleshooting, TLS renewal, SP rotation, onboarding guide, AKS PDB, Grafana dashboards.

## 2. JFrog SaaS POC — *technical lead*

- Three **GitHub Actions** workflows validating **all 11 JFrog package types** end-to-end on `geicoeast.jfrog.io`; OIDC smoke-test composite action; repo-settings-driven provisioning via `amp-control-plane`.
- ADO pipeline for 4-language POC (OIDC). SaaS load test: **5,000 repos / 5,000 parallel artifacts**.
- AB#12143170 (Closed) · 6+ merged PRs in `pkg-mgmt`.

## 3. amp-control-plane — *architect & deployer*

- **Deployed to ACS production** (May 2026). Go service on Azure Container Service.
- **Entra ID auth boundary**: Go JWT middleware + APISIX custom-jwt + APIM; cross-team with Identity + API Management. AB#12178284.
- Club MCP server config shipped into control plane.

## 4. Cursor × Claude Code MCP bridge — *inventor*

- GEICO Claude Code pilot: built **Cursor-cached-token bridge** that lets Claude Code reuse Cursor's encrypted Slack MCP credentials.
- MCP servers + agent skills in production: JFrog, Slack, ADO, GitHub; `solve-case`, `close-case`, `build-kb`.
- **DE AI Showcase 2026**: four initiatives (Claude Agent triage, AI CI/CD migration engine, Claude Code plugin, AI-consumable ADR).

## 5. OpenClaw cost-aware runtime — *project lead, Purdue ECE 50874*

[github.com/mailming/openclaw](https://github.com/mailming/openclaw)

- Governance layer: per-task token/cost/step budgets; AgentOps + Langfuse; IEEE-style report. p95 cost ↓ without dropping success rate.

## 6. Jiadroid — *founder · phone-as-robot-brain*

[github.com/mailming/jiadroid](https://github.com/mailming/jiadroid)

- Open **phone↔robot protocol** (device discovery, walk commands, latched estop) so a phone supplies brain/eyes/ears for any compatible body.
- **Follow Me** on Android + iOS (person / marker / QR) driving Open Duck Mini simulator over Wi-Fi; voice listen/reply in-app.
- Thesis: one brain, many bodies — embodied agent platform without waiting for a humanoid employer.

---

**Other:** Founder of [SmartTuna](https://smarttuna.ai) (LangGraph multi-agent). Staff Release Engineer at Navan (SOC 2 Type II, IPO). HA Jenkins + Nexus at Turn/Amobee (**$600K+/yr** savings). U.S. Citizen.

*Full evidence catalog: `portfolio/work-evidence.md`*
