# STAR Stories — 10 Behavioral Narratives

Each story uses Situation / Task / Action / Result. Keep the spoken version to ~2 min; the written one captures the full detail so you don't blank under pressure. Practice each one out loud until you can do it without notes.

After each STAR there is an **"if they ask a follow-up"** section — the 2-3 most likely probes and a one-line answer for each.

---

## 1. Artifactory 99.99% turnaround (GEICO, 2025–2026)

**Situation.** When I joined GEICO's Artifact Management Platform team in mid-2025, Artifactory was the backbone for every container image, every model artifact, and every CI pipeline binary across our engineering org. It was also experiencing roughly one major incident every month — usually a cascade from a network or auth dependency that cratered build velocity for hours.

**Task.** As the new Staff-IC tech lead I owned the reliability outcome. The implicit ask was "stop the bleeding"; the explicit ask was "get us to four-nines SLO within the year."

**Action.**
1. **Mapped the failure surface.** Every incident from the prior 12 months went into a single sheet — class, dependency, MTTD, MTTR, root cause. Half the incidents had three or four root causes; one — Azure Firewall TLS DPI on S3-backed repos — accounted for 40% of total outage minutes.
2. **Fixed the dominant class first.** Owned the packet-level RCA, drove the cross-team plan with Network and Database Platform, shipped the firewall reconfig and JFrog client mitigations.
3. **Made on-call survivable.** Wrote AI-consumable runbooks (so any agent or new on-call engineer could resolve common pages without paging me); introduced JFrog / Slack / ADO MCP servers and Claude / Cursor agent skills like `solve-case`, `close-case`, `build-kb`.
4. **Hardened identity.** Architected Entra ID auth for `amp-control-plane` — Go JWT middleware plus APIM defense-in-depth — and deployed it to ACS production.
5. **Authored the CoE for NOCIM-11695** (April 2026 Entra-ID-driven outage) which surfaced two latent issues we then fixed before they re-tripped.

**Result.** Incident rate from ~1 major/month down to a sustained four-nines (99.99%) availability SLO. AMP on-call is now answerable in plain English by Claude Code with the runbook skills. Cross-team Entra ID work cleared the path for the broader GEICO Entra rollout.

**If they ask a follow-up.**
- *What was the hardest tradeoff?* Choosing to ignore three smaller incident classes for the first quarter; they were noisy but the single firewall class was 40% of outage minutes — sequencing mattered.
- *What would you do differently?* Have written the AI-consumable runbooks **first**, not last; they paid back the most operational time.
- *What did your manager push back on?* The MCP-agent rollout — initially seen as a side project. I framed it as on-call survivability and tied it to the SLO.

---

## 2. NOCIM-11695 — Entra-ID-driven outage CoE (GEICO, April 2026)

**Situation.** Production Artifactory went out for ~90 minutes after a cross-tenant Entra ID change rippled into APIM's token validation. Builds globally backed up. This was the highest-severity AMP incident of the year.

**Task.** I was on-call lead and CoE author. The CoE had to produce a credible root cause, an accurate sequence of events, and a corrective-action list that the wider org could execute.

**Action.**
- Started the bridge call within 5 minutes; got Identity, Network, and APIM teams in one room.
- Ran the timeline in parallel with mitigation so the CoE was ready the next day, not the next week.
- Identified two latent issues neither team had owned: APIM cache TTL was too long for our auth model, and our health-check probed a code path that bypassed the failing component (so the page came late).
- Authored five corrective actions with owners and dates; tracked them to closure.

**Result.** Two latent issues fixed before they re-tripped. The CoE became a referenced template in the org for how to write Entra-related CoEs. My credibility in the cross-team Entra working group jumped — that's what unlocked architectural authority for the AMP Entra rollout.

**If they ask a follow-up.**
- *What was the actual root cause?* A change in upstream tenant token signing material wasn't propagated to our APIM cache before the old material aged out.
- *How did you find the latent issues?* The health-check one was already in my "investigate later" list — the outage moved it to "investigate now." The cache-TTL one came from comparing observed vs expected MTTD.

---

## 3. Jenkins HA migration at Turn/Amobee (2018–2019)

**Situation.** At Turn/Amobee we had one Jenkins primary node serving a ~500-person engineering org deploying to thousands of production servers worldwide. Outages were measured in hours per week. UI pages took 12 seconds. We were also evaluating CloudBees enterprise at roughly $500K/year.

**Task.** Get to high availability and answer the CloudBees question. Both at once.

**Action.**
1. Designed an HA topology with multiple controllers, shared storage, and ephemeral agents on pools sized to peak parallelism.
2. Built the migration runbook to be reversible at every step. Cutover happened in three production-load windows over a weekend.
3. Drove a careful benchmark of our scale (queue depth, parallel builds, plugin set) against CloudBees features — the features we'd use mapped to maybe $50K/year of equivalent OSS effort.
4. Wrote the recommendation against CloudBees with the data, and the migration plan to prove HA OSS Jenkins met our needs.

**Result.** Unplanned outages went from hours/week to under 5 minutes of planned downtime per month. UI page-load dropped from 12 s to 0.5 s. We declined CloudBees and saved $500K+/year on enterprise licensing.

**If they ask a follow-up.**
- *Hardest piece?* Plugin compatibility. Some plugins behaved differently under HA, and we found two corrupting shared state in subtle ways during the load test.
- *What did you measure to validate HA?* Mean-time-between-failures across both controllers, builds completed during a forced primary failover, and a synthetic week of injected failures.

---

## 4. Nexus HA migration at Turn/Amobee (2019)

**Situation.** Same shape as Jenkins; same shop. Nexus was the artifact backbone and a single point of failure.

**Task.** Get Nexus HA and answer the Sonatype enterprise question.

**Action.**
- Designed Nexus HA with multiple nodes and a shared blob store; instrumented heavy load test that simulated peak parallel uploads from CI.
- Caught and fixed two real issues during load test (replication lag under parallel writes, GC tuning).
- Wrote the migration runbook and ran cutover off-hours with three rollback checkpoints.

**Result.** Unplanned outages eliminated post-migration. Saved $100K+/year vs Sonatype enterprise licensing. Combined with Jenkins migration, the team's total saving was $600K+/year, which I cited in the writeup that got the team's headcount approved.

**If they ask a follow-up.**
- *What broke during load test?* Replication lag pushed reads out-of-date by up to 8 seconds during peak; the fix involved write-through behavior plus read-after-write checks for one critical client.

---

## 5. SOC 2 Type II + Vault + SonarCloud at Navan (2022–2023)

**Situation.** Navan (TripActions then) was on the IPO-readiness track. Engineering had to demonstrate SOC 2 Type II controls. Engineering CI/CD was the loudest gap in the auditor's pre-assessment.

**Task.** I owned audit remediation for the engineering org. The deliverables: secrets centrally managed, static analysis enforced at PR time, and audit-trail-grade evidence the controls were operating.

**Action.**
1. Stood up HashiCorp Vault as the secrets backbone; built migration scripts to move existing secrets out of CI variables and into Vault with namespaced policies.
2. Rolled out SonarCloud as a required PR gate across repos.
3. Wrote the runbooks and evidence harness so audit pulls were repeatable.
4. Owned the back-and-forth with auditors and Internal Audit through the Type II observation window.

**Result.** Passed SOC 2 Type II. Vault is still the secrets backbone. SonarCloud became the default static-analysis gate. Engineering wasn't on the critical path for the IPO readiness checklist after this.

**If they ask a follow-up.**
- *How did you handle resistance to a required SonarCloud gate?* Phased it in by severity. First, "warn only" for 4 weeks. Then "fail on critical." Then "fail on high+critical." Each phase gave teams time to clean their backlogs.
- *Hardest part of Vault rollout?* Bootstrapping namespaces and policies in a way that scaled. Wrote a Terraform module that teams could self-serve a namespace + a service-account policy.

---

## 6. JFrog SaaS POC at GEICO (2026)

**Situation.** Strategic decision to evaluate JFrog SaaS as a possible replacement for parts of our self-hosted Artifactory footprint. POC needed to validate that **all 11** supported JFrog package types worked end-to-end at our scale.

**Task.** Technical lead on the POC. The deliverables: working pipelines for all 11 package types, a load-test result, a recommendation.

**Action.**
1. Built three GitHub Actions workflows covering the package-type matrix (upload, resolve, promote — for each type).
2. Designed a load test profile: 5,000 repos / 5,000 parallel artifacts on `geicoeast.jfrog.io`. Calibrated against our peak production load.
3. Co-developed an AI-powered CI/CD migration engine that opens per-team PRs to switch their pipelines to SaaS — targeting 100% of inventoried pipelines on cutover day.
4. Ran the load test, captured failures and SaaS-side limits, and wrote up the findings.

**Result.** Validated SaaS coverage across all 11 package types; surfaced two scale-side issues with JFrog that we filed and that they are tracking. The migration engine produces ready-to-merge PRs at low engineering cost. POC moves to the cutover stage in Q3 2026.

**If they ask a follow-up.**
- *What surprised you in the load test?* SaaS rate limits behave differently from self-hosted under bursty parallel writes; our cutover plan now includes a warm-up step.
- *How does the AI migration engine actually work?* Inventory pipelines from GitHub + ADO, classify by template family, generate a PR with the SaaS endpoint swap and any extra auth shifts; human review before merge.

---

## 7. Cursor × Claude Code MCP bridge (GEICO, 2026)

**Situation.** I was invited to GEICO's Claude Code pilot. The pilot ran in parallel with Cursor adoption. Each product had its own enterprise auth state (especially for Slack MCP), which meant developers were authenticating twice — and security wasn't going to approve two parallel cred stores forever.

**Task.** Authored the *"Cursor MCP × Slack"* BRD. The product ask: let Claude Code reuse Cursor's encrypted Slack MCP credentials without exposing them in clear.

**Action.**
1. Wrote the BRD: requirements, security model, threat model, rollback story.
2. Designed the bridge: Cursor's cached token store is read via an OS-level read with an explicit user-consent prompt; Claude Code receives a derived short-lived token, never the raw store contents.
3. Implemented the bridge; shipped it through the Claude Code pilot.

**Result.** Developers in the pilot got single-sign Slack MCP across both products. Security approved the design. The pattern is being looked at for ADO, GitHub, and other MCP servers — same shape repeats.

**If they ask a follow-up.**
- *How did you handle the cross-process auth boundary safely?* Short-lived derived token, never the raw store; explicit user-consent dialog on first bridge; revocation hooked into Cursor's existing logout.
- *Who pushed back?* Security initially read this as "let Anthropic see your Slack." Walking them through the actual data flow turned them into champions.

---

## 8. OpenClaw cost-aware runtime plugin (Purdue ECE 50874, 2026)

**Situation.** ECE 50874 final project, Team 17. We had to ship something real — code, paper, and demo — using the LLM-augmented engineering tools the course was built around.

**Task.** I originated the project idea: take open-source OpenClaw browser agents and add a runtime layer that gives them per-task budgets and policy enforcement without forking the agent core.

**Action.**
1. Defined four design constraints: no agent-core changes, policy decisions at step boundaries, cost as a first-class signal, human-editable pricing tables.
2. Designed the LLM Insights gateway plugin: sits between agent and any LLM call; tags every call with run/step IDs; emits cost events; resolves pricing through a manual-override layer.
3. Built the AgentOps integration for routing + budget state, and Langfuse for trace telemetry.
4. Wrote the benchmark harness and the IEEE-style report.

**Result.** Runtime ships in our repo branch. Cost-tail compresses dramatically vs baseline OpenClaw with task success rate flat. Cited as a finalist project in the cohort. Publishing the blog post + benchmark publicly in Month 2 of my job-search plan.

**If they ask a follow-up.**
- *Where do you draw the line between agent logic and runtime governance?* The runtime never makes the agent's decisions — it only decides whether the agent can keep going. That mental model is the whole point.
- *Why manual pricing overrides?* Vendors invent SKUs faster than billing systems can model them; pricing has to be a hot-reloadable config, not a code change.
- *What's next?* Multi-provider cost-quality routing.

---

## 9. SmartTuna — solo product build (2024–present)

**Situation.** I wanted a public, end-to-end agentic system I owned. Outside any employer's code. Stock analysis was a domain I cared about and one where reasoning over multi-source data made sense.

**Task.** Ship a multi-agent product with a public UI. No team. Limited time.

**Action.**
1. Picked LangGraph as the orchestration layer.
2. Built the backend: data ingestion, agent graph, model-pluggable providers (Claude / GPT / Gemini).
3. Built the front-end (Astro) and wired up live trades / rationale rendering.
4. Deployed at [smarttuna.ai](https://smarttuna.ai).

**Result.** Public product I can demo end-to-end. Multi-agent design that I can show anyone in an interview. Forcing function for my own LangGraph fluency.

**If they ask a follow-up.**
- *Why LangGraph?* Explicit state-machine + checkpoint model maps well to multi-agent workflows; alternatives required more glue.
- *What did you have to throw away?* My first agent graph was a single big graph; rewrote it as a hierarchy because debugging one big graph at runtime is awful.

---

## 10. Hardest disagreement / biggest mistake

(Pick whichever the interviewer asks. Both stories below.)

### 10a. Hardest disagreement — JFrog SaaS cutover sequencing (GEICO)

**Situation.** A senior peer wanted to cut over the largest pipeline family first. I disagreed and wanted to cut over the smallest first, then medium, then largest — the standard reversible-rollout argument.

**Task.** Convince the room, or change my mind.

**Action.**
- Built a one-pager listing the four pipeline families and the rollback cost for each.
- Showed that the largest family's rollback cost was 6x the smallest, and the smallest family's coverage of distinct package types was 80% of the largest.
- We could de-risk most of the surface with the smallest family first.

**Result.** Plan adopted. We caught two SaaS-side issues during the smallest family's cutover that would have hurt much more at the larger scale.

**Follow-up if probed.** Reasonable people can disagree; what's not reasonable is to disagree without building a rollback-cost number.

### 10b. Biggest mistake — Vault rollout phase 1 (Navan)

**Situation.** Early Vault rollout. I provisioned namespaces and policies myself instead of building the Terraform module first.

**Task.** Onboard ~30 service accounts in the first month.

**Mistake.** Hand-provisioning meant inconsistent policy structure across teams. Three months later, an audit pull surfaced the inconsistency and we did a painful retroactive cleanup.

**Lesson.** The second user of a system is the one whose pattern matters; design for the second user, not the first. I now write the Terraform module / API before doing the second hand-provision.

---

## Practice schedule

- **Week 5 (Month 2):** read each story once silently; speak it out loud once. Refine the wording where you stumbled.
- **Week 6:** record yourself doing each in ≤ 2 minutes. Listen back at 1.5x. Cut filler.
- **Week 7:** do all 10 in one sitting with no notes. The ones you blank on are the ones to re-write — they're not yet *yours*.
- **Week 8:** alternate with the 2 mock interviews (see `mock-interviews.md`). After every mock, append one new follow-up question to the relevant story.

## Story-to-question mapping (cheat sheet)

| Question style | Use story |
|----------------|-----------|
| "Tell me about a time you owned reliability" | 1 (99.99%), 3 (Jenkins HA), 4 (Nexus HA) |
| "Tell me about a high-stakes incident" | 2 (NOCIM-11695) |
| "Tell me about driving change you didn't have authority for" | 7 (Cursor × Claude Code MCP bridge), 5 (SonarCloud rollout) |
| "Tell me about a project you originated" | 8 (OpenClaw), 9 (SmartTuna) |
| "Tell me about cost / resource tradeoffs" | 3, 4, 6 |
| "Tell me about disagreement / conflict" | 10a |
| "Tell me about your biggest mistake" | 10b |
| "Tell me about leading without formal authority" | 1, 5, 7 |
