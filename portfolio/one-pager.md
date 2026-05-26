# Ming Jia — AI Infrastructure / Platform Engineer

**Fremont, CA** · mailming@gmail.com · (626) 354-7866 · [linkedin.com/in/mailming](https://www.linkedin.com/in/mailming) · [github.com/mailming](https://github.com/mailming)

Staff-scope platform engineer building production agentic systems and the reliability platforms they run on. Currently shipping Claude Agent SDK + MCP + Cursor work into GEICO's 2026 DE AI Showcase, and led the OpenClaw cost-aware runtime plugin at Purdue (ECE 50874).

---

## 1. OpenClaw cost-aware runtime — *primary implementer, project lead*

[github.com/mailming/openclaw](https://github.com/mailming/openclaw/tree/feature/llm-insights-manual-pricing)

A governance layer around [OpenClaw](https://github.com/openclaw-ai/openclaw) browser agents.

- Per-task budgets on tokens, cost, wallclock, and steps; policy decisions at step boundaries (allow / throttle / halt / escalate-to-human) — no changes to agent core.
- LLM Insights gateway plugin with rolling cost/latency aggregates and manual pricing overrides for non-standard model SKUs.
- Integrated AgentOps (routing + budget state) and Langfuse (trace telemetry); deployed with Playwright automation and a Telegram control surface.
- Cost-aware compresses the cost tail dramatically (p95 cost ↓) without dropping task success rate. Benchmarks + IEEE-style report in repo.

## 2. Cursor × Claude Code MCP bridge at GEICO — *BRD author + primary implementer*

GEICO Developer Engineering, 2026 DE AI Showcase (282-associate org-wide program).

- Invited to GEICO's Claude Code pilot. Authored the *"Cursor MCP × Slack"* BRD.
- Built the Cursor-cached-token bridge that lets Claude Code reuse Cursor's encrypted Slack MCP credentials — first time the two products shared an enterprise auth state.
- Shipped Club MCP server config into `amp-control-plane`; introduced JFrog / Slack / ADO / GitHub MCP servers and Claude / Cursor agent skills (`solve-case`, `close-case`, `build-kb`) across the AMP team's support, RCA, and runbook workflows.

## 3. Artifactory 99.99% turnaround at GEICO — *Staff-IC tech lead*

- Drove Artifactory from ~1 major incident/month to a **four-nines (99.99%) availability SLO** — the backbone for every model artifact, container image, and ML pipeline binary the org consumes.
- Technical lead on the JFrog SaaS POC: three GitHub Actions workflows validating all 11 supported package types end-to-end; SaaS load test at 5,000 repos / 5,000 parallel artifacts.
- Architected Entra ID auth for `amp-control-plane` (Go JWT middleware + APIM defense-in-depth). Deployed to ACS production.
- CoE author for NOCIM-11695 (April 2026 Entra-ID-driven outage). Packet-level Azure Firewall TLS DPI RCAs on S3-backed repos.

---

**Other:** Founder of [SmartTuna](https://smarttuna.ai) (LangGraph multi-agent stock-analysis platform). Staff Release Engineer at Navan through IPO readiness (SOC 2 Type II, Vault, SonarCloud). HA Jenkins + Nexus migrations at Turn/Amobee ($600K+/yr savings). Pursuing MS in Artificial Intelligence at Purdue. U.S. Citizen.
