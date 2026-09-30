# Portfolio Artifact — Month 2

Pick ONE primary ship target. Finished beats fancy.

## Active primary (Physical AI) — Jiadroid

**[Jiadroid](https://github.com/mailming/jiadroid)** is the Outcome A build: phone-as-robot-brain + open body protocol + Follow Me (Android/iOS + Open Duck Mini sim). Career framing, pitch, and milestones: **[jiadroid.md](jiadroid.md)**.

Ship order for 2026 H2:

1. Demo video (phone → sim) + LinkedIn Featured pin  
2. ESP32 / real duck (or clear next-body plan)  
3. Keep OpenClaw blog as the *agent-infra* companion artifact (below)

Isaac Lab is **deferred** until Jiadroid hits a hardware milestone or you need it for GRAD 58900.

## Recommendation (AI-native / agent-infra companion)

**Option A: OpenClaw cost-aware runtime blog post + benchmark report.** Highest ROI for Anthropic/Cursor/Databricks:

- You already built the work; you're not starting from scratch.
- Three audiences read it: hiring managers (proof of senior-IC thinking), interviewers (deep-dive material), and the agent-tooling community (Hacker News, r/LocalLLaMA).
- Pairs naturally with the OpenClaw GitHub repo and the IEEE-style report you wrote for Purdue ECE 50874.
- 3-4 weekends of work to publish at high quality.

The blog draft is started at `portfolio/blog-openclaw-cost-aware-runtime.md`.

## Option B: Publish a polished MCP server to the Anthropic registry

Pick **JFrog MCP** (you already built the GEICO version) or **Artifactory MCP** (same idea, OSS-clean). What you need to ship:

- Clean repo with README, install instructions, tests.
- `mcp.json` manifest published.
- A 90-second demo video.
- Submit to https://github.com/modelcontextprotocol/servers as a community server.

Investment: ~3-4 weekends. Higher engineering effort than the blog, but the artifact is reusable as Cursor + Anthropic interview material.

## Option C: Substantive OSS PR

Target one of: vLLM, Ray, SkyPilot, LiteLLM, LangGraph, the official MCP servers repo, or Cursor extensions. Aim for a feature PR, not a typo fix. Suggested candidates:

- **vLLM:** a small "manual pricing override" feature would be on-thesis with OpenClaw work.
- **LiteLLM:** add an MCP-server-as-provider adapter.
- **LangGraph:** improve cost-tracking instrumentation hooks (Langfuse already plugs in; bake cost in natively).
- **MCP servers repo:** contribute a JFrog or Artifactory server (overlaps with Option B).

Investment depends on how quickly the maintainers respond — risky for a hard timeline. Pair with Option A if possible.

## Once shipped

- Replace one item in your LinkedIn "Featured" section with the artifact (see `linkedin-rewrite.md`).
- Add a single sentence to the "Selected AI Work" section of `resume-ai-infra.md`.
- Drop a 4-6 sentence LinkedIn post linking to it (tags: #AIInfrastructure #MCP #LangGraph #AgentOps — or #Robotics #PhysicalAI for Jiadroid).
- Forward to all open recruiter conversations and referral contacts as a "fresh proof point" before onsites.

## Files in this directory

- `work-evidence.md` — **master catalog** of all work (Slack + GitHub + ADO sourced). Start here for resume tailoring.
- `one-pager.md` — 1-page summary you attach to referrals + interview follow-ups.
- `jiadroid.md` — Physical AI primary artifact mapping.
- `blog-openclaw-cost-aware-runtime.md` — Option A draft.
- (Add `mcp-server/` if you pick Option B; add `oss-pr-notes.md` if you pick Option C.)
