# Company Briefs — Tier-S / Tier-1 Targets

One page per company covering: thesis, interview format, what they value, what to research before onsite, your specific hook, and the "watch out for" trap. Drawn from the live careers-page snapshots in [../../hot-jobs-may-2026.md](../../hot-jobs-may-2026.md) and 2026 interview reports.

For each: read it the **night before the screen**, then re-read the night before the onsite.

---

## Anthropic

**Thesis.** Safety-first frontier AI lab; Claude as a model and a product. Public-benefit corporation; founders ex-OpenAI; deeply opinionated about alignment, interpretability, and reliable AI. ~5000+ employees in 2026 with strong Bay/NYC/Seattle/London presence.

**Interview format.**
- 4-6 rounds: recruiter screen → hiring-manager screen → 2-3 technical rounds (coding, system design, behavioral) → sometimes a values round.
- **Coding:** practical Python, real-world problems. *Generally* no AI tools allowed in SWE rounds. *May* allow Claude Sonnet in ML/Prompt Engineering rounds — confirm with recruiter.
- **System design:** AI-infra heavy. Expect inference serving, evals, distributed training.
- **Behavioral:** values-heavy. They've published their values; map your STAR stories to them.

**What they value (their published list):**
1. **Safety-first** — talk about systems whose failure modes you proactively designed against.
2. **High talent density** — don't over-credit your team; show what *you* drove.
3. **Helpful, harmless, honest** — they apply this to people too. Don't bluff; say "I don't know" cleanly.
4. **Pragmatism** — frontier work, but shipped. They value engineers who ship over engineers who theorise.
5. **Anti-careerism** — they have a (public) policy of not optimising for promo cycles. Frame your work in impact, not title.

**Research before onsite.**
- Read [Anthropic's core views](https://www.anthropic.com/news/core-views-on-ai-safety) (or current equivalent) cover-to-cover.
- Read [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) — quote from this in your answers.
- Try Claude Code and the Claude desktop app for 1 hour with intent. Note 2-3 specific things you'd improve.
- Skim 1-2 recent interpretability papers from their research blog so you can speak to their research culture.

**Your specific hook.**
- "I'm leading the Claude Code / Cursor / MCP enterprise rollout at GEICO" — single strongest opener.
- "I authored the Cursor × Claude Code MCP bridge BRD and shipped it" — concrete evidence of doing the work they care about.
- "The four-nines AMP turnaround" — proves you can carry reliability at scale.

**Watch out for.**
- Don't over-recite Anthropic's PR. They can tell. Speak from genuine reflection.
- Values rounds: pick a story where you **didn't** know the answer in advance — they're looking for thinking-out-loud, not polished answers.
- Don't speak as if Anthropic is the obvious right place to be. Show you've weighed alternatives.

**Top open roles ([../../hot-jobs-may-2026.md](../../hot-jobs-may-2026.md) #1, 4, 5, 6):**
- Staff+ Software Engineer, Developer Productivity (your single best match)
- Staff + Sr. Software Engineer, AI Reliability
- Staff Software Engineer, Kubernetes Platform
- Staff Infrastructure Engineer, Cluster Infrastructure

---

## Cursor (Anysphere)

**Thesis.** AI-native code editor; goal: automate coding. Tiny team (~50 in 2026), extreme talent density, flat org, no management layers. Ship velocity is the brand.

**Interview format.**
- 2-3 short technical screens (45 min each) → 1-day onsite project at SF or NYC office.
- **Onsite day:** you work on a small project in their codebase / on real tools, discuss ideas, meet the team. Intense. Bring food.
- No traditional system-design round; the onsite project *is* the system-design signal.

**What they value:**
1. **Shipping** — "we particularly like people who are truth-seeking, passionate, and creative." Show shipped artifacts.
2. **Taste** — "you have taste and strong opinions on model and agent behaviors." Have opinions.
3. **Gray-area judgment** — "you make good calls when there isn't a single 'right' answer." Show how you've adjudicated trade-offs.
4. **Engineering depth** — they ship at a very high bar. Demonstrate it in the live project.
5. **Anti-process** — small flat team; don't talk about your processes / frameworks. Talk about decisions.

**Research before onsite.**
- Use Cursor *heavily* for 1 week before. Be fluent: Cmd+I, Cmd+K, agent mode, MCP tools, agent skills, custom commands. Don't be the candidate fumbling the IDE.
- Read [Cursor's official blog](https://cursor.com/blog) for the latest 5 posts. Note features they've shipped recently.
- Try [Cursor agents in background mode](https://cursor.com/docs/agents/background) — they're shipping this aggressively in 2026.
- Read 1-2 of their public papers / posts about model training (they fine-tune custom models for low-latency code completion).

**Your specific hook.**
- "OpenClaw cost-aware runtime is essentially the governance pattern Cursor's Agent Harness team is shipping at production scale" — direct thesis match.
- "I wrote Cursor agent skills (`solve-case`, `close-case`, `build-kb`) for GEICO production on-call" — proves you build *on* their platform.
- "Cursor × Claude Code MCP bridge BRD" — proves architectural thinking, not just usage.

**Watch out for.**
- Don't talk about your processes or how things scale at "enterprise" scope. Cursor is anti-bureaucracy by culture.
- The 1-day project is real work. Don't pace yourself; treat it like a hackathon you're trying to win.
- They have a slight bias for raw IC ability over breadth. If asked "what would you do as a manager?" — pivot to IC scope.

**Top open roles ([../../hot-jobs-may-2026.md](../../hot-jobs-may-2026.md) #2, 3):**
- Software Engineer, Agent Harness
- Software Engineer, Agent Evaluation and Quality
- Software Engineer, DevEx / Infrastructure / Client Infra

---

## OpenAI

**Thesis.** Mission to ensure AGI benefits all humanity. Largest scale (~3k+ engineering), most resourced, most product-shipped. Hybrid 3 days in-office in SF.

**Interview format.**
- Recruiter screen → 1-2 technical screens → onsite (5-6 rounds: coding, system design, behavioral, sometimes ML literacy).
- **Coding:** distributed-systems flavoured; Python or Go for most teams. For the Analytics Platform role specifically: Rust or C++ required.
- **System design:** infra-heavy. Expect inference, training orchestration, data infra.
- **Behavioral:** standard FAANG-style + mission alignment.

**What they value:**
1. **Scale + ship velocity** — "design systems for the next order of magnitude" recurs in their JDs.
2. **Mission alignment** — they take it seriously even if it's become a cliché.
3. **Pragmatism with rigour** — they don't romanticise research; engineering chops matter.
4. **Hands-on operational ownership** — many JDs mention on-call and "operational excellence." Don't dodge SRE-flavoured questions.

**Research before onsite.**
- Read [OpenAI's engineering blog](https://openai.com/blog/engineering) cover-to-cover for the past 3 months.
- Try OpenAI products (ChatGPT, Codex, Operator, Realtime API) with intent. Have an opinion on which is best designed.
- Skim their published research papers — even the ones not directly relevant to your role tell you about their engineering culture.

**Your specific hook.**
- "I shipped enterprise AI tooling at GEICO across MCP servers, agent skills, and the Cursor × Claude Code bridge" — relevant to Enterprise AI Platform role.
- "Artifactory four-nines + JFrog SaaS POC at 5,000-repos scale" — credible enterprise platform story.
- "Entra ID + APIM defense-in-depth for amp-control-plane" — the security-compliance angle they explicitly ask about.

**Watch out for.**
- For the Analytics Platform role specifically: don't apply unless you're willing to ramp Rust. The JD is explicit and they screen for it.
- Hybrid 3 days in SF — confirm you're committed before applying.
- Don't bash competitors (Anthropic / Cursor / etc.) — they hate that.

**Top open roles ([../../hot-jobs-may-2026.md](../../hot-jobs-may-2026.md) #10, 15, 16, 17):**
- Software Engineer, Enterprise AI Platform (best fit)
- Software Engineer, Data Infrastructure
- Capacity Systems Software Engineer
- (Skip: Analytics Platform — Rust requirement)

---

## Modal

**Thesis.** Serverless GPU compute for AI. Python-first developer experience, custom container runtime, custom file system, sub-second cold starts. Small team (~100 in 2026, NYC/SF/Stockholm), high-systems-depth bar.

**Interview format.**
- Recruiter screen → 45-min hiring-manager screen (deep "why Modal" + role-specific calibration) → 3-4 technical rounds → references + team match.
- **Coding:** systems flavoured; expect questions about scheduling, containers, performance.
- **System design:** GPU scheduling, cold-start, container runtime tradeoffs.
- **Bar:** comparable to Stripe / HashiCorp, higher than typical startup.
- Glassdoor reports ~3.2/5 difficulty, 11-day timeline.

**What they value:**
1. **Systems depth** — they built their own container runtime and scheduler. They want engineers who care about systems internals.
2. **Developer experience** — Python-first is core; they think hard about the API.
3. **Reliability** — when customer GPU jobs fail, Modal engineers diagnose. Strong on-call expectation.
4. **Craft-focused** — Erik Bernhardsson's culture; thoughtful engineering, public writing, low-ego.

**Research before onsite.**
- Read [Erik Bernhardsson's blog](https://erikbern.com/) — broad, opinionated; gives you the founder's thinking.
- Read [Modal's engineering blog](https://modal.com/blog) end to end — there are deep posts on the scheduler, cold-start, file system.
- Try Modal: build a small inference deployment in 30 min. The API is the product; understand it.
- Familiarise with the GPU autoscaling and container internals that Modal has differentiated on.

**Your specific hook.**
- "I led the AMP four-nines turnaround — I know how to be the first reliability hire" (their open role is literally for first reliability-focused MTS).
- "JFrog SaaS POC at 5,000 repos / parallel artifact load" — relevant scale signal.
- "OpenClaw cost-aware runtime + Langfuse / AgentOps for governance observability" — shows you understand the operational side of AI workloads.

**Watch out for.**
- Don't BS on systems depth. They'll catch you. If you don't know NCCL internals, say so and pivot to what you do know.
- MTS title structure has no formal ladder — they hire by scope, not band. Don't ask for "what's the next level after MTS" early.
- NY/SF/Stockholm only; remote is harder to land. Confirm geo before deep prep.

**Top open roles ([../../hot-jobs-may-2026.md](../../hot-jobs-may-2026.md) #7):**
- Member of Technical Staff – Platform Engineering / Reliability Engineering
- Member of Technical Staff – Systems
- Infrastructure Security Engineer

---

## Databricks (Mosaic AI)

**Thesis.** Data + AI platform; Mosaic AI fast-growing for foundation-model APIs, agent framework, AI gateway. Public company, structured org, mature interview process.

**Interview format.**
- Standard FAANG-style: phone screen → technical screen → onsite (4-5 rounds).
- **Coding:** LC mediums; one hard expected.
- **System design:** AI/ML infra leaning depending on team — agent quality team will go deep on evals; AI platform on MLflow/AI Gateway/Agent Framework.
- **Behavioral:** their "GeNZ" interview style is structured; stick rigorously to STAR.

**What they value:**
1. **Production-readiness** — they sell to Fortune 500; "demos don't ship" is the cultural posture.
2. **Ownership across systems** — many JDs say "from user-facing features to low-level GPU orchestration."
3. **Customer empathy** — they're enterprise-first; show you understand how your work affects customer engineers.
4. **OSS contributions** — they value MLflow / PyTorch / Ray contributors; mention any.

**Research before onsite.**
- Read [Mosaic AI's product docs](https://docs.databricks.com/aws/en/machine-learning/) — Agent Framework, Agent Bricks, AI Gateway, Foundation Model APIs.
- Read 2-3 recent [Databricks engineering blog posts](https://www.databricks.com/blog).
- Familiarise with MLflow (they bought it; it's central to many of their AI roles).

**Your specific hook.**
- "SmartTuna multi-agent LangGraph + Anthropic / OpenAI provider plug-ins" — direct mapping to Agent Framework.
- "MCP servers shipped at GEICO" — modern agent tooling.
- "OpenClaw cost-aware runtime" — agent quality / evaluation framing.

**Watch out for.**
- Their structured interview format means deviation costs you. Don't ramble; STAR every behavioral answer.
- Some open Mosaic AI roles are NYC-only — confirm geo.
- Be ready for the "tell me about your most production-relevant agent" question — name something specific you've shipped.

**Top open roles ([../../hot-jobs-may-2026.md](../../hot-jobs-may-2026.md) #8, 9, 20):**
- Staff Backend Software Engineer (AI Platform) — best fit
- Staff Software Engineer, Agent Quality — NYC
- Staff Software Engineer, AI Research Infrastructure

---

## Perplexity

**Thesis.** AI-first answer engine with citations; rapid growth (~500 employees in 2026), SF/Palo Alto/NYC. AI-specific system design is the differentiator in their interview process.

**Interview format.**
- Recruiter screen → technical coding screen (Python-heavy, practical) → potential take-home for senior roles → multi-round onsite.
- **Coding:** practical not LC-hard. 3.31/5 difficulty per Glassdoor.
- **System design:** RAG architecture, search infra at scale, LLM serving. **This is the differentiator.**
- **Behavioral:** standard.

**What they value:**
1. **AI product taste** — they want users of Perplexity who have opinions on the product.
2. **AI-specific system design** — generic distributed-systems thinking is table-stakes; RAG / search / inference is the real test.
3. **Ship velocity** — high recommendation rate from employees suggests fast culture.
4. **Hybrid friction tolerance** — SF/PA/NYC, mostly in-person.

**Research before onsite.**
- Use Perplexity heavily for a week. Note: how do they handle citations? How do they balance freshness vs. quality? Multi-step research mode?
- Read their [Pro features documentation](https://www.perplexity.ai/) — Comet (browser agent), API platform.
- Skim public Perplexity engineering posts.
- Read RAG architecture papers (see [reading-list.md](reading-list.md) Month 1 Week 2).

**Your specific hook.**
- "OpenClaw cost-aware runtime over browser agents" — adjacent to Comet (their browser agent).
- "SmartTuna multi-agent LangGraph" — agent platform experience.
- "MCP servers shipped at GEICO" — relevant to their API platform direction.

**Watch out for.**
- The interview spike is AI-specific system design. If you can't deliver doc 02 (vector DB) and a RAG design fluidly, you'll get filtered.
- Coding is practical — don't over-show LC chops; show clean code.

**Top open roles ([../../hot-jobs-may-2026.md](../../hot-jobs-may-2026.md) #13, 25):**
- MTS (AI Infrastructure Engineer)
- MTS (Software Engineer, AI Platform)
- MTS (Backend Software Engineer, API Platform)

---

## Sierra

**Thesis.** Conversational AI for business (Bret Taylor + Clay Bavor). Enterprise customer experience agents — voice + chat. Primarily in-person SF + global offices.

**Interview format.**
- Recruiter → 1-2 technical screens → onsite (in person).
- **Coding:** standard; Go and TypeScript bias for platform roles.
- **System design:** agent orchestration, eval systems, retrieval. Very direct overlap with their product.
- **Behavioral:** high-agency, ownership-mindset emphasis.

**What they value:**
1. **High agency** — JDs say "motivation and high-agency to drive outcomes in a high-autonomy culture."
2. **Agent SDK / platform thinking** — they invest in agent dev experience; they want builders who get this.
3. **Enterprise reliability** — production-ready, retrieval-grounded, evaluable.
4. **In-person collaboration** — they're explicit about being in-person primarily.

**Research before onsite.**
- Read Bret Taylor's recent essays / podcast interviews.
- Try a Sierra demo if accessible.
- Read [the Sierra blog](https://sierra.ai/blog/).
- Read their agent SDK docs if public.

**Your specific hook.**
- "OpenClaw cost-aware runtime + Langfuse / AgentOps eval pipelines" — Sierra cares deeply about agent evaluation.
- "SmartTuna multi-agent LangGraph" — agent SDK / orchestration overlap.
- "Enterprise AI deployment at GEICO" — enterprise empathy.

**Watch out for.**
- In-person SF emphasis — confirm geo commitment.
- Don't talk only about consumer AI; they're enterprise-first.

**Top open roles ([../../hot-jobs-may-2026.md](../../hot-jobs-may-2026.md) #12, 21, 22):**
- Software Engineer, Agent Architecture
- Software Engineer, Platform / Infrastructure / SRE
- Software Engineer, Agent Data Platform

---

## LangChain

**Thesis.** Open-source agent framework + commercial LangSmith / LangGraph platform. Used by Fortune 500 + millions of devs. Mission: make intelligent agents ubiquitous.

**Interview format.**
- Recruiter → 1-2 technical → onsite (in-person SF preferred, also Boston / NYC).
- **Coding:** Python / TypeScript depending on role. Storage engine role: Rust-required.
- **System design:** agent orchestration, evaluation, observability storage.

**What they value:**
1. **Open-source engagement** — strong bias for OSS maintainers / contributors.
2. **Production agent experience** — they sell to people building agents in production; they want builders.
3. **Ownership-mindset** — "you excel at managing your work without close supervision."
4. **In-person 5 days/week** — confirm geo.

**Research before onsite.**
- You already use LangGraph (SmartTuna). Deepen: read the source code for one core package (`langgraph.graph` or `langchain_core.runnables`).
- Read LangSmith docs to understand the commercial side.
- Read 2-3 of their blog posts on agent evaluation.

**Your specific hook.**
- "SmartTuna multi-agent LangGraph" — you're literally building on their platform.
- "OpenClaw cost-aware runtime" — production agent governance.

**Watch out for.**
- 5 days/week in SF (or Boston). Confirm geo before applying.
- Storage engine role is Rust-required; skip unless you've committed to Rust.

**Top open roles ([../../hot-jobs-may-2026.md](../../hot-jobs-may-2026.md) #14, 23):**
- Python OSS Engineer
- Fullstack Applied AI Engineer

---

## Browserbase

**Thesis.** Cloud-hosted headless browser infra for AI agents. Open-source Stagehand framework (~17k stars, ~2M monthly downloads). SF in-person 5 days/week. ~9 open roles in mid-2026.

**Interview format.**
- Recruiter → technical screens → onsite.
- **Coding:** TypeScript bias; also Python / Go welcomed.
- **System design:** distributed systems, browser automation infra, agent runtime.

**What they value:**
1. **Open-source experience** — Stagehand is the brand; they want OSS contributors.
2. **AI / agent product taste** — "experience building AI agents/LLMs."
3. **Distributed systems / reliability** — headless browser fleets are hard.
4. **In-person SF** — explicit 5 days/week.

**Research before onsite.**
- Read the [Stagehand docs](https://www.stagehand.dev/) — it's the closest commercial product to OpenClaw.
- Read [Browserbase blog](https://www.browserbase.com/blog).
- Try Stagehand for 30 min — build a small automation.

**Your specific hook.**
- "OpenClaw cost-aware runtime over Playwright-based browser agents" — direct on-thesis match. Bring this up early.
- "Stagehand-style governance and evaluation telemetry through Langfuse + AgentOps" — show you understand their problem space.

**Watch out for.**
- 5 days/week SF only — confirm.
- Their team is small; come ready to discuss specifics, not generalities.

**Top open roles ([../../hot-jobs-may-2026.md](../../hot-jobs-may-2026.md) #11, 24):**
- Software Engineer (Stagehand) — best fit
- Software Engineer (Agent Platform)
- Software Engineer (Core Infrastructure / Distributed Systems)

---

## Universal pre-onsite prep (always)

For *any* company, the day-before-onsite ritual is:

1. **Re-read this brief** for the company.
2. **Re-read the JD** for the specific role. Pull 3 phrases verbatim.
3. **Re-read** your "why this company / why this role / why now" answers.
4. **Re-read** the [system-design-cheatsheet.md](system-design-cheatsheet.md) section likely to come up.
5. **Re-read** the [behavioral-question-bank.md](behavioral-question-bank.md) sections likely to come up (use the brief above to pick).
6. **Sleep ≥ 7 hours.** Studies on this are unambiguous; you cannot make this up day-of.
7. **Eat protein** before the onsite. Energy crashes after 2-3 rounds are the most common onsite failure mode.
8. **5 questions to ask them** — pre-pick from the question bank Section I.

---

## Universal "watch out for" list

- **Don't trash-talk competitors.** Everyone at the AI labs talks to everyone else; the industry is small.
- **Don't claim to know a paper you've only skimmed.** They'll go 3 questions deep and you'll be caught.
- **Don't dodge "tell me about a failure."** The dodge is the failure. Have a real one rehearsed.
- **Don't optimise for the offer at the screen.** Optimise for the conversation. Offers come from conversations that are real.
