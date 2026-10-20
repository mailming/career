# Ming Jia — Platform & AI Engineer

**Fremont, CA** · mailming@gmail.com · (626) 354-7866 · [linkedin.com/in/mailming](https://www.linkedin.com/in/mailming) · [github.com/mailming](https://github.com/mailming)

Staff-scope platform engineer building production agentic systems and the reliability platforms they run on. GEICO Artifact Management (Jun 2025 – Present). MS AI @ Purdue. U.S. Citizen.

---

## 1. Artifactory reliability + Load Healer — *Staff-IC, AMP on-call*

- Drove Artifactory from **~1 major incident/month → four-nines (99.99%) SLO**; upgraded to **7.161.15**.
- **Load Healer Reactive** (Oct 2026, PR #109/#111): NP validated + **PD2** deployed — Tomcat OUTAGE → per-account **HTTP 429** instead of node meltdown; data-driven ~640 concurrent/account threshold.
- **CoE author**: NOCIM-11695 (Entra-ID), NOCIM-12455 (npm EINTEGRITY), **NOCIM-13154** (MarTech PD upgrade), **NOCIM-13213** (router OOM).
- PD Phase 1 stability; TLS renewals with **&lt;1 min** outage; 10+ runbooks + Slack maintenance-announcement skill.

## 2. Martech → JFrog SaaS cutover — *program lead (with AMP)*

- Hard date **Jan 30, 2026** — no rollback to artifactory-pd.
- Stood up `#amp-martech-migration` / `#amp-cdp-migration`; kicked off **MAP, CDP Self Serve/Chameleon, Billing, Payments, Bolt·Athena**.
- Installed **`amp-migrate`** for OIDC + repo-settings campaigns; PATH Martech→SaaS / CDN auth (AMP #694).
- Earlier: SaaS POC tech lead — **11 package types** e2e; load test **5,000 repos / 5,000 parallel artifacts**.

## 3. amp-control-plane + Entra ID — *architect & deployer*

- Deployed to **ACS production**; Entra ID auth (Go JWT + APISIX + APIM). Club MCP in control plane.

## 4. Cursor × Claude Code MCP + DE AI Showcase

- Claude Code pilot: **Cursor-cached-token bridge** for Slack MCP credentials.
- MCP servers + skills in production (`solve-case`, `close-case`, `build-kb`); Showcase portfolio (triage, migration engine, Claude Code plugin, AI-consumable ADR).

## 5. Jiadroid — *founder · phone-as-robot-brain*

[github.com/mailming/jiadroid](https://github.com/mailming/jiadroid)

- Open phone↔robot protocol; **ESP32-S3** 2WD firmware (Wi-Fi / USB-C / OTA); Follow Me on Android+iOS; duck + rover sims (MuJoCo).

## 6. OpenClaw cost-aware runtime — *Purdue ECE 50874 lead*

[github.com/mailming/openclaw](https://github.com/mailming/openclaw) — token/cost/step budgets; AgentOps + Langfuse.

---

**Other:** [SmartTuna](https://smarttuna.ai) (LangGraph). Navan Staff RE (SOC 2 / IPO). Turn/Amobee Jenkins+Nexus HA (**$600K+/yr**).

*Evidence catalog: `portfolio/work-evidence.md` · Updated 2026-10-19*
