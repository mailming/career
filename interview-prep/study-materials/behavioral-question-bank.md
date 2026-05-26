# Behavioral Question Bank

60+ likely questions, each mapped to which of your 10 STAR stories to use. For each: the question, the **primary** story, a **backup** story, the one-sentence opener, and the trap to avoid.

Stories referenced (full text in [../star-stories.md](../star-stories.md)):

1. **Artifactory 99.99% turnaround** (Staff-IC reliability leadership)
2. **NOCIM-11695 CoE** (incident command + writing)
3. **Jenkins HA** (older platform migration)
4. **Vault SOC 2** (compliance under deadline)
5. **SaaS POC** (vendor evaluation + decision)
6. **Cursor × Claude Code MCP bridge** (AI dev-tools innovation)
7. **OpenClaw** (cost-aware agent runtime, academic project)
8. **SmartTuna** (multi-agent LangGraph, side project)
9. **Hardest disagreement** (conflict + influence)
10. **Biggest mistake** (humility + learning)

---

## Section A — Leadership & Influence

### A1. "Tell me about a time you led a cross-functional project."
- **Primary:** #1 Artifactory · **Backup:** #6 MCP bridge
- **Opener:** "When I joined GEICO's AMP team mid-2025, Artifactory was the backbone for every CI pipeline but failing roughly monthly. I owned the four-nines outcome as the new staff-IC tech lead..."
- **Trap:** Don't list 5 teams; pick the 2 that mattered (Network, Identity) and explain the joint plan.

### A2. "Describe a time you had to influence without authority."
- **Primary:** #9 Hardest disagreement · **Backup:** #1 Artifactory (the MCP rollout sub-plot)
- **Opener:** "Early in the AMP work my manager treated the MCP-agent rollout as a side project. I had to reframe it from 'shiny AI thing' to 'on-call survivability tied to the SLO'..."
- **Trap:** "Influencing" is not "I was right and they finally agreed." Show you adjusted *your* model based on their pushback.

### A3. "Tell me about a project where you had to set technical direction."
- **Primary:** #1 Artifactory · **Backup:** #4 Vault SOC 2
- **Opener:** "I owned the technical strategy for getting Artifactory to four-nines. The default plan was 'fix each incident class as it arose.' I sequenced by outage-minutes contribution instead..."
- **Trap:** Don't pretend you invented every idea. Cite which ideas were yours vs. team contributions.

### A4. "How do you mentor / grow other engineers?"
- **Primary:** #1 Artifactory (runbook + AI-skills work) · **Backup:** #6 MCP bridge
- **Opener:** "My biggest mentorship leverage at GEICO has been making senior knowledge agent-consumable. I wrote runbooks as MCP skills (`solve-case`, `close-case`, `build-kb`) so any on-call engineer or AI agent can resolve common pages..."
- **Trap:** Don't say "I taught them X." Show structured artefacts (docs, skills, code review patterns) that scale beyond 1:1 mentoring.

### A5. "Describe a time you owned a project end-to-end."
- **Primary:** #7 OpenClaw · **Backup:** #4 Vault SOC 2
- **Opener:** "OpenClaw is the Purdue ECE 50874 final project where I originated the cost-aware runtime concept — a governance plugin around browser agents with token, cost, and step budgets..."
- **Trap:** For an academic project, name the production-style discipline you imposed (CI, benchmarks, write-up).

---

## Section B — Conflict & Disagreement

### B1. "Tell me about a time you disagreed with a manager/peer."
- **Primary:** #9 Hardest disagreement · **Backup:** Artifactory MCP rollout (sub-thread of #1)
- **Opener:** "..." [from your #9 story]
- **Trap:** Don't pick a low-stakes disagreement. Interviewers can smell it. Pick the one that actually risked your standing.

### B2. "Describe a conflict on your team and how you handled it."
- **Primary:** #9 · **Backup:** #5 SaaS POC (vendor vs. internal-build camp)
- **Opener:** "On the JFrog SaaS POC, the platform team wanted on-prem indefinitely; the leadership team wanted SaaS yesterday. I was the engineer running the actual evaluation..."
- **Trap:** Don't paint either side as villain. Show you sought their best argument.

### B3. "How do you handle pushback on your design?"
- **Primary:** #1 Artifactory · **Backup:** #6 MCP bridge
- **Opener:** "When I proposed sequencing by outage-minutes rather than incident count, Network and DB Platform pushed back because three smaller classes were noisier in their queues..."
- **Trap:** Don't claim you "convinced" them. Show a compromise: I went after the biggest class first AND committed to a public dashboard so everyone could see the others weren't being ignored.

### B4. "Tell me about a difficult stakeholder."
- **Primary:** #5 SaaS POC (the procurement / security stakeholder) · **Backup:** #4 Vault SOC 2 (auditor)
- **Opener:** "On the Vault SOC 2 audit, the auditor flagged our secrets-rotation cadence as insufficient and wanted an immediate full re-rotation across all environments..."
- **Trap:** "Difficult" doesn't mean "they were wrong." Show what they were right about.

---

## Section C — Failure, Mistakes, Learning

### C1. "Tell me about a time you failed / made a mistake."
- **Primary:** #10 Biggest mistake · **Backup:** A specific decision in #1 you'd reverse
- **Opener:** "..." [from your #10 story]
- **Trap:** Don't pick a "humble-brag" failure ("I worked too hard"). Pick something that genuinely cost the org something measurable.

### C2. "What's something you'd do differently today?"
- **Primary:** #1 Artifactory · **Backup:** #7 OpenClaw
- **Opener:** "On Artifactory I'd write the AI-consumable runbooks **first**, not last. They paid back the most operational time of anything I did, and starting with them would have shortened MTTR for the team by months..."
- **Trap:** Don't say "nothing." That's a credibility-killer at staff level.

### C3. "Tell me about a time you got critical feedback."
- **Primary:** Personal anecdote from #1's MCP-rollout pushback · **Backup:** #10
- **Opener:** "My GEICO manager initially gave me feedback that I was 'gold-plating' the MCP rollout — bringing AI tooling into reliability work before the underlying reliability problems were stable..."
- **Trap:** Show you *acted* on the feedback (sequenced the work; didn't drop the idea but didn't lead with it either).

### C4. "When have you missed a deadline?"
- **Primary:** #4 Vault SOC 2 (initial scope miss) · **Backup:** #7 OpenClaw (the eval suite was tighter than the runtime)
- **Opener:** "Our initial Vault SOC 2 plan had me delivering all environments by end of Q1. By end of January it was obvious we'd miss; I escalated the slip 6 weeks before the deadline rather than after..."
- **Trap:** Don't claim you "still hit the deadline." Show how you escalated early.

---

## Section D — Technical Judgment & Trade-offs

### D1. "Tell me about a difficult technical decision."
- **Primary:** #5 SaaS POC · **Backup:** #1 (sequencing by outage minutes)
- **Opener:** "The JFrog SaaS evaluation forced a 3-year directional bet — SaaS, self-hosted, or hybrid — across 5,000 repos and the org's entire CI/CD..."
- **Trap:** Don't make the decision sound obvious in hindsight. Show what would have made you pick the other way.

### D2. "Describe a time you had to make a decision with incomplete information."
- **Primary:** #1 (the first incident response) · **Backup:** #6 MCP bridge
- **Opener:** "When the first major Artifactory outage hit after I joined, the symptom was 'builds failing' but the cause space included network, auth, storage, and the JFrog client. I had ~20 minutes to bisect..."
- **Trap:** Don't pretend you knew. Show you bisected the space efficiently.

### D3. "Tell me about a time you over-engineered something."
- **Primary:** #10 (if your story has this shape) · **Backup:** #7 OpenClaw (the policy DSL — could have been simpler)
- **Opener:** "On OpenClaw I built a policy DSL for governance rules. In retrospect a handful of typed Python functions would have done 80% of it for 20% of the LOC..."
- **Trap:** Don't claim you "always under-engineer." That's a different problem.

### D4. "When have you advocated for a technology choice?"
- **Primary:** #6 MCP bridge · **Backup:** #5 SaaS POC
- **Opener:** "When MCP came out of Anthropic in late 2024 I saw it as the missing layer between our internal services and Claude / Cursor. I built the Cursor × Claude Code credential bridge and shipped the JFrog / Slack / ADO MCP servers..."
- **Trap:** Show you accounted for risk (lock-in, immaturity) not just upside.

### D5. "Tell me about a technical debt you took on intentionally."
- **Primary:** Sequencing in #1 (smaller incident classes deliberately deferred) · **Backup:** #7 OpenClaw (the eval suite scope)
- **Opener:** "On Artifactory I deliberately deferred fixing three smaller incident classes for the first quarter while we tackled the firewall class. That was visible debt..."
- **Trap:** Show how you tracked the debt so it didn't quietly grow.

---

## Section E — Speed, Pressure, Ambiguity

### E1. "Tell me about your most high-pressure moment."
- **Primary:** #2 NOCIM-11695 (live outage) · **Backup:** #4 Vault SOC 2 deadline week
- **Opener:** "April 2026, Artifactory went out for ~90 minutes due to an Entra-ID cascade into APIM. I was on-call lead. I had Identity, Network, APIM, and a customer-comms thread all live in one bridge..."
- **Trap:** Don't make it a hero story. Show the team made it work.

### E2. "How do you handle ambiguous problems?"
- **Primary:** #1 (which incident class to fix first?) · **Backup:** #7 OpenClaw (cost-aware was an original concept)
- **Opener:** "When I joined AMP the explicit ask was 'get to four-nines' but no one had named the dominant failure class. I built the incident sheet because the question wasn't actionable without it..."
- **Trap:** Show *one* concrete artefact you produced that reduced ambiguity.

### E3. "Describe a time you had to learn something new fast."
- **Primary:** #7 OpenClaw (Playwright + agent runtime in 8 weeks) · **Backup:** #8 SmartTuna (LangGraph)
- **Opener:** "For Team 17's final project I went from zero browser-agent experience to shipping a cost-aware runtime plugin in 8 weeks. The first 2 weeks I just read..."
- **Trap:** Don't claim mastery. Show you knew enough to ship and identified what you still didn't know.

### E4. "Tell me about a time priorities shifted suddenly."
- **Primary:** #2 NOCIM-11695 (incident pre-empted everything) · **Backup:** #4 Vault SOC 2 audit
- **Opener:** "..."
- **Trap:** Show how you communicated the shift to your team and stakeholders.

---

## Section F — Innovation & Initiative

### F1. "Tell me about a time you went above and beyond."
- **Primary:** #1 (the AI runbooks were not in the original plan) · **Backup:** #6 MCP bridge
- **Opener:** "The AI-consumable runbooks weren't asked for; my management chain wanted incident-class fixes. I built the runbook-as-MCP-skill pattern in parallel because I saw the on-call burden compounding..."
- **Trap:** Don't say you "worked extra hours." Show you used the time on a high-leverage thing.

### F2. "Describe something you built that wasn't required."
- **Primary:** #6 MCP bridge · **Backup:** #7 OpenClaw · #8 SmartTuna
- **Opener:** "The Cursor × Claude Code credential bridge wasn't on any roadmap. I noticed every engineer was re-auth'ing Claude Code daily while Cursor was already authed, and I wrote the BRD plus the bridge..."
- **Trap:** Show adoption / outcome, not just "I built it."

### F3. "Tell me about a time you championed a new idea."
- **Primary:** #6 MCP bridge · **Backup:** #7 OpenClaw cost-aware runtime
- **Opener:** "I championed MCP server adoption at GEICO before there was an internal narrative for it. Started with JFrog (because it solved a real Artifactory operator pain) and used the demo to make the broader case..."
- **Trap:** Show the resistance you overcame.

### F4. "Describe your most creative solution."
- **Primary:** #7 OpenClaw (governance-as-plugin pattern) · **Backup:** #6 (cached-token bridge)
- **Opener:** "OpenClaw's cost-aware runtime is implemented as a non-invasive plugin: it observes every browser-agent action and applies post-action policies (token / cost / step budgets) without rewriting the core agent logic..."
- **Trap:** "Creative" should mean "non-obvious in retrospect," not "complicated."

---

## Section G — Culture / Values Fit (Anthropic-style)

### G1. "Tell me about a time you prioritised safety over speed."
- **Primary:** #4 Vault SOC 2 (audit-driven decision to slow rollout) · **Backup:** #7 OpenClaw (policy enforcement before runtime expansion)
- **Opener:** "On Vault SOC 2 I made a call to slow the multi-environment rollout by 6 weeks because we didn't have automated rotation drills in place. The audit only required rotation; I argued we needed drills before we declared compliance..."
- **Trap:** Don't make this a "compliance theater" story. Show real risk avoided.

### G2. "How do you think about responsible AI?"
- **Primary:** #7 OpenClaw cost-aware runtime · **Backup:** #6 MCP bridge (auth + audit log scope)
- **Opener:** "My OpenClaw work is essentially about constraining agent behavior to a known cost and policy envelope. The cost-aware runtime is a governance primitive: agents that can't be governed can't safely be deployed in production environments..."
- **Trap:** Don't recite generic AI safety language. Be concrete about your work.

### G3. "Tell me about a time you said no to a stakeholder."
- **Primary:** #5 SaaS POC (declined a vendor's escalation) · **Backup:** #9 disagreement
- **Opener:** "During the SaaS evaluation the vendor pushed hard to lock in before our security review completed. I held the line — said 'we will not sign until security has signed off' — and accepted the schedule risk..."
- **Trap:** Show you said no with a reason and a path forward.

### G4. "What do you do when you see something unsafe / ethically off?"
- **Primary:** A real example from your AMP work (find the closest) · **Backup:** Hypothetical with the framework
- **Opener:** "I think of it as a three-step: name it concretely, ask the owner if it's already known, and write a one-page risk note if the answer is no. I did this for a quiet auth path in AMP that bypassed our health checks..."
- **Trap:** Don't be preachy. Show concrete action.

---

## Section H — "Why" Questions

### H1. "Why this company?"
- **Approach:** Use the company brief from [company-briefs.md](company-briefs.md). 60-90 seconds. Always **specific**: name a product, a paper, a team value, and connect to a concrete piece of your work.
- **Template:** "Three reasons. First, [company-specific thesis I align with — name a public thing they've shipped or written]. Second, [piece of my work that maps to that thesis — name one project]. Third, [team-level fit — what I want to learn here that I can't elsewhere]."
- **Trap:** Avoid "I love your mission" generic openers. Name a specific shipped thing.

### H2. "Why are you leaving GEICO?"
- **Opener:** "GEICO has been the right place to build deep AI-platform credibility — owning AMP to four-nines, shipping MCP servers to production, leading the Claude Code rollout. The work I'm most excited about now — cost-aware agent runtimes, agent-eval pipelines, agent dev-tooling — happens at the AI-native shops at a velocity I can't match from inside an insurance company..."
- **Trap:** **Never** disparage GEICO. The opposite signal lands harder: "I'd recommend GEICO to anyone who wants to build platform credibility with the latitude to ship AI tooling."

### H3. "Why this role specifically?"
- **Approach:** Quote two phrases from the JD verbatim back to them and connect each to a project of yours.
- **Trap:** If you can't quote phrases from the JD, you haven't done the prep.

### H4. "Why now?"
- **Opener:** "Two reasons. The frontier of useful AI shipped to enterprises moved from 'demos' to 'tools production engineers depend on daily' over the last 12 months — the work my team at GEICO does today wouldn't have been possible 18 months ago. And second, I've now done enough at GEICO to know my next step is purely AI-native work, not a hybrid role..."

### H5. "Where do you see yourself in 5 years?"
- **Opener:** "Doing AI-platform IC work that's two or three steps ahead of what's shipping today — building the governance, cost, and eval primitives that make agents safe to deploy at production scale. I'm not chasing a manager track..."
- **Trap:** Don't be vague. Name the specific kind of problem.

---

## Section I — Questions You Ask Them (closing 5-10 min)

Always have 5 questions ready. Pick 3-4 based on the conversation. The right questions signal seniority.

### About the team
1. "What's the team's hardest problem right now — the one that hasn't been solved yet?"
2. "If I joined and you came back from a quarter of being away, what would I have moved forward?"
3. "Where does this team draw the line between research and engineering? How does that hand-off work in practice?"

### About the role
4. "What does the ramp-up look like in the first 90 days? What's the biggest thing I could deliver in that window?"
5. "Who would I be sitting in design reviews with? What's the IC seniority distribution on the team?"
6. "How is success measured for this role — what does 'crushing it' look like at the 6-month mark?"

### About the company
7. "What's a strategic decision the company made in the last year that you disagreed with? How did the decision-making play out?"
8. "What's the company's stance on [a thing they're publicly trying to figure out — RL, retrieval, on-device, etc.]? How is it evolving?"

### About the interviewer (always close with one of these)
9. "What made *you* join? What's kept you here?"
10. "What's the biggest thing you've changed your mind about since joining?"

---

## Universal STAR rules

1. **Lead with the result in one sentence** (the "headline"). Then back-fill the situation. Interviewers grade on the headline — the rest is evidence.
2. **"I" not "we"** for actions; **"we"** for results — show what *you* did inside the team accomplishment.
3. **Quantify or qualify** — a number ("99.99% SLO", "5,000 repos") or a named artefact ("the NOCIM-11695 CoE") beats "lots of impact."
4. **2 minutes spoken max.** Past 2 min, the interviewer mentally checks out. Practice with a stopwatch.
5. **End with a beat of silence.** Don't fill it. The interviewer will follow up with the most interesting probe — which you've pre-rehearsed.
6. **Have one "result-was-mixed" story ready.** If every story ends with "and it worked perfectly," interviewers stop believing you.

---

## Red flags to avoid

- "**We** built X." → Show your specific contribution.
- "**Lots of**" / "**a lot of**" / "**many**" → Always replace with a number or a named example.
- "**Basically**" / "**kind of**" / "**sort of**" → Filler. Cut.
- "**I learned a lot.**" → Useless. Replace with: "I'd do X differently today because Y."
- "**It was a great experience.**" → No. Show specific tradeoffs.
- Skipping the failure / disagreement question and pivoting to a success — interviewers notice instantly.

---

## How to practice this bank

**Week 1-4 (Month 1):** After writing each STAR story, look up the 3-4 questions in this bank that map to it. Read the opener and the trap. Update your story if the trap reveals a hole.

**Week 5-6 (Month 2):** Have a friend pick 6 random questions (e.g., A1, B2, C3, D4, E5, F1). Answer each in 2 min, time yourself. Self-score 1-5; redo any < 4.

**Week 7-16:** Light maintenance. Re-read this file before any phone screen or onsite. Don't drill answers daily after Week 6 — at staff level, over-rehearsed answers sound worse than slightly fresh ones.

**Day-of-interview:** Re-read only the section likely to come up (e.g., A & B for HM screens; G for Anthropic; F for Cursor). 10 min total.
