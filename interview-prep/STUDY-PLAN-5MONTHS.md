# 5-Month Interview Study Plan

**Window:** 2026-05-26 (Mon, Week 1 start) → 2026-10-11 (Sun, Week 20 end).
**Budget:** 10-12 hrs/week sustainably (≈ 1.5-2 hrs Mon-Fri + 2-3 hrs Sat + 1 hr Sun review). Phone screens / onsites replace study blocks 1:1 on the day they fall.
**Targets at the end:** ~85 LC problems (65 mediums + 20 hards), 8 system-design write-ups internalised + 2 deeper variants, 10 STAR stories polished, 6-7 mock interviews logged, 1 polished public artifact shipped, 3 staff-level deep dives keynote-ready, 3-5 onsite loops run, 2+ offers in hand by Week 20.

This file is the **single weekly schedule**. Every concrete asset already lives in this folder — links inline. The 5-month version (vs the original 3-month) gives more foundation breathing room, an explicit portfolio month, mid-flight resume iteration, and a realistic onsite ramp.

## Study materials (live in `study-materials/`)

The content you actually study from. Use alongside the weekly schedule below.

| File | Use when |
|------|----------|
| [study-materials/coding-patterns.md](study-materials/coding-patterns.md) | Daily — Python templates + idioms for every LC pattern. Read the relevant section before each problem. |
| [study-materials/behavioral-question-bank.md](study-materials/behavioral-question-bank.md) | Before every phone screen + onsite — 60+ questions mapped to your STAR stories. |
| [study-materials/system-design-cheatsheet.md](study-materials/system-design-cheatsheet.md) | Night-before onsite — 1-page numbers, headlines, traps, follow-ups per design topic. |
| [study-materials/reading-list.md](study-materials/reading-list.md) | Weekly — papers + blog posts aligned to each week's design topic. |
| [study-materials/company-briefs.md](study-materials/company-briefs.md) | Night-before screen + onsite — thesis, format, values, your hook, traps per company. |
| [study-materials/outreach-templates.md](study-materials/outreach-templates.md) | Every message — cold-outreach, referral ask, thank-you, negotiation, resignation. |

---

## Why 5 months > 3

| Slack lever | What changes |
|-------------|--------------|
| Foundation pace | LC weeks 1-4 stay at 5 problems/wk; we then *spiral* the same patterns in W5-8 rather than rushing onto new ones. Patterns stick. |
| Public artifact | Original plan rushed this into 4 weeks (Month 2). Now: a full month (W9-12) to ship one polished artifact (OpenClaw blog + benchmarks, or MCP server in Anthropic registry). Recruiters can read it before the onsite. |
| Resume iteration | Real conversion data from W4-W8 phone screens informs a W9 resume rewrite. The 3-month plan didn't have time for this loop. |
| Onsite buffer | Frontier-AI loops take 6-8 weeks from screen to offer. 5 months means **2 distinct waves of onsites** — first wave in W13-16 (lower-stakes practice), second wave in W17-20 (real targets). |
| Health | Sustainable cadence over 20 weeks beats heroic 12-week sprint. Sleep, partner relationship, GEICO performance all stay intact. |

---

## How to use this plan

1. **Every Monday morning, read the current week.** Cross off items as you finish. Don't skip ahead.
2. **Daily template** (weekday): 1 hr coding + 1 hr "other" (design / STAR / mock / phone screen / portfolio).
3. **Replace study with interviews** when they land. If a phone screen books for Wed afternoon, drop Wed coding; if an onsite books, drop the whole day's study and put it on Sat.
4. **Weekly checkpoint** (Sun 1 hr): retrospective in the "Weekly checkpoint log" at the bottom. Update conversion metrics in [../target-companies.md](../target-companies.md).
5. **If a week slips,** don't try to catch up; just continue forward. Cumulative coverage matters more than perfect adherence.

---

## Month 1 — Foundation (Weeks 1-4)

**Theme:** clean LC reflexes on the 5 most common patterns + first half of system-design canon + first 4 STAR stories + apply funnel filled.

### Week 1 (2026-05-26 → 2026-06-01) — Setup & Arrays/Hash

**Coding (5 problems):** Group Anagrams · Top K Frequent · Product Except Self · Longest Consecutive · 3Sum.
Source: [coding-log.md § Week 1](coding-log.md). Patterns reference: [study-materials/coding-patterns.md § 1-2](study-materials/coding-patterns.md). Use the daily template at the bottom of that file.

**System design (1 doc):** Read and outline [01-llm-inference-serving.md](system-design/01-llm-inference-serving.md). Goal: speak the architecture in 8-10 min from memory by Sunday. Sketch on whiteboard / iPad. Reading: [reading-list.md § Month 1 Week 1](study-materials/reading-list.md) — pick 1 of vLLM paper or vLLM docs.

**Behavioral:** Draft Stories #1 (Artifactory 99.99%) and #2 (NOCIM-11695) in [star-stories.md](star-stories.md). Each: 90 sec spoken time; record on phone; listen back; cut filler.

**Pipeline:**
- Send Tier-S applications #1-4 from [../hot-jobs-may-2026.md](../hot-jobs-may-2026.md) (Anthropic Dev Productivity, Cursor Agent Harness, Cursor Agent Eval, Anthropic AI Reliability). Pre-read [company-briefs.md](study-materials/company-briefs.md) for Anthropic + Cursor before drafting cover notes. Use [outreach-templates.md § 1](study-materials/outreach-templates.md) if cold-messaging a hiring manager.
- Update LinkedIn headline + About from [../linkedin-rewrite.md](../linkedin-rewrite.md). Flip "Open to Work" privately.

### Week 2 (2026-06-02 → 2026-06-08) — Sliding Window / Stack / Binary Search

**Coding (5):** Longest Substring No Repeat · Longest Repeating Char Replacement · Min Stack · Daily Temperatures · Search Rotated Sorted Array.

**System design (1):** [02-vector-db-at-scale.md](system-design/02-vector-db-at-scale.md). Whiteboard HNSW vs IVF-PQ vs DiskANN tradeoffs out loud.

**Behavioral:** Draft Stories #3 (Jenkins HA) and #4 (Vault SOC 2). Record + critique.

**Pipeline:**
- Send Tier-1 applications #7-10 (Modal MTS, Databricks AI Platform, Databricks Agent Quality, OpenAI Enterprise).
- Activate referral path #1 from [../referrals.md](../referrals.md) (GEICO Claude pilot teammates → ask for 2 intros).

### Week 3 (2026-06-09 → 2026-06-15) — Linked List / Trees / BFS-DFS

**Coding (5):** Reorder List · Remove Nth from End · Validate BST · Level Order Traversal · Build Tree from Preorder + Inorder.

**System design (1):** [03-agent-orchestration.md](system-design/03-agent-orchestration.md). Most-likely surface at Cursor / Sierra / LangChain / Databricks Agent Quality. Talk through state machine, retry semantics, fan-out parallelism.

**Behavioral:** Draft Stories #5 (SaaS POC) and #6 (Cursor × Claude Code MCP bridge). The MCP bridge story is the single best "Tell me about a recent technical win" answer you have; rehearse it 5×.

**Pipeline:**
- Send Tier-1 applications #11-14 (Browserbase, Sierra, Perplexity, LangChain).
- 1st phone screen this week if any came back. Day-before: read [phone-screen-playbook.md](phone-screen-playbook.md) + the [company-briefs.md](study-materials/company-briefs.md) section for that company + the relevant section of [behavioral-question-bank.md](study-materials/behavioral-question-bank.md). Send a post-screen thank-you using [outreach-templates.md § 5](study-materials/outreach-templates.md).

### Week 4 (2026-06-16 → 2026-06-22) — Graphs / Trie / Heap

**Coding (5):** Number of Islands · Clone Graph · Pacific Atlantic · Implement Trie · Kth Largest. Day 5: paper-only (no IDE) — simulates whiteboard.

**System design (1):** [04-eval-pipelines.md](system-design/04-eval-pipelines.md). Direct overlap with Cursor Agent Eval and Anthropic AI Reliability roles. Draw the eval graph from data → judges → regression alerts → dashboards.

**Behavioral:** Draft Stories #7 (OpenClaw) and #8 (SmartTuna). Pre-load 3 "what would you do differently" answers per story.

**Pipeline:**
- Aim for 2-3 phone screens this week (the apply queue from W1-W3 should be landing).
- Mid-month retro: am I converting 25%+ apply → screen? Log baseline; we'll iterate in W9.

**Month 1 exit gate:**
- ☐ 20 LC mediums solved
- ☐ 4 system designs internalised (can deliver each in 10 min cold)
- ☐ 8 STAR stories drafted + recorded once
- ☐ Resume sent for ≥ 15 Tier-1 roles
- ☐ ≥ 2 phone screens completed and logged
- If any gate misses by >20%, replan Week 5 to close it before adding new surface.

---

## Month 2 — Depth & First Mocks (Weeks 5-8)

**Theme:** harder LC patterns, second half of design canon, first mocks, double phone-screen cadence.

### Week 5 (2026-06-23 → 2026-06-29) — DP / Intervals / Greedy

**Coding (5 medium):** House Robber · Coin Change · LIS · Merge Intervals · Non-overlapping Intervals. Source: [coding-log.md § Week 5](coding-log.md).

**System design (1):** [05-distributed-training-orchestration.md](system-design/05-distributed-training-orchestration.md). Slurm vs K8s, gang scheduling, checkpoint sharding. Anthropic Cluster Infra / Databricks AI Research Infra surface.

**Behavioral:** Draft Stories #9 (hardest disagreement) and #10 (biggest mistake). These two land the hardest if you've never said them out loud. Record both; redo if any answer ducks the question.

**Pipeline:** Schedule **Mock #1 (coding)** for Sat. interviewing.io or Pramp. Topic: arrays/hash/sliding window (your strongest area, build confidence). Log in [mock-interviews.md](mock-interviews.md).

### Week 6 (2026-06-30 → 2026-07-06) — DP+ / Backtracking + 1st Hard

**Coding (5 medium + 1 hard):** Word Break · Unique Paths · Combination Sum · Word Search · Subsets · **Trapping Rain Water (LC 42, hard)**. First hard — give it 60-90 min on Saturday, do not time-pressure.

**System design (1):** [06-gpu-autoscaling.md](system-design/06-gpu-autoscaling.md). Most-likely Modal / Anthropic Node Infra surface.

**Behavioral:** Polish all 10 stories to ≤ 2 min spoken. Build the question→story cheat sheet section in [star-stories.md](star-stories.md).

**Pipeline:**
- 3-5 phone screens this week. After each, write a 5-line debrief in [target-companies.md](../target-companies.md) Notes column.

### Week 7 (2026-07-07 → 2026-07-13) — Trie+ / Heap+ / Mixed

**Coding (5 medium + 1 hard):** Word Ladder · Course Schedule · Course Schedule II · Find Median from Data Stream (hard) · Task Scheduler · Design Add and Search Word.

**System design (1):** [07-multi-tenant-inference-cost.md](system-design/07-multi-tenant-inference-cost.md). Most differentiated topic — pairs with OpenClaw blog story.

**Behavioral:** "Why this company?" answers for top 5 active processes. 60-90 sec each. Template in [phone-screen-playbook.md](phone-screen-playbook.md).

**Pipeline:** **Mock #2 (system design)** this week. Topic: pick whichever of the 6 designs you've covered feels weakest.

### Week 8 (2026-07-14 → 2026-07-20) — Graph+ / Hard mix

**Coding (5 medium + 2 hard):** Number of Connected Components · Graph Valid Tree · Word Ladder II (hard) · Min Window Substring (hard) · Encode/Decode Strings · Longest Palindromic Substring · Spiral Matrix.

**System design (1):** [08-prompt-eval-registry.md](system-design/08-prompt-eval-registry.md). Last of the 8 designs. Useful for any "design a developer tool" prompt at Cursor / Anthropic Developer Productivity.

**Behavioral:** Pick the artifact you'll ship in Month 3 — read [../portfolio/README.md](../portfolio/README.md) and decide between:
- **A: OpenClaw blog + benchmarks** (recommended; highest-leverage if you have GitHub repo data)
- **B: MCP server in Anthropic registry**
- **C: Substantive OSS PR** (vLLM / Ray / SkyPilot / LiteLLM)

**Month 2 exit gate:**
- ☐ ~43 LC problems cumulative (40 mediums + 3 hards)
- ☐ All 8 system designs delivered out loud at least once
- ☐ 2 mocks logged with self-scores
- ☐ ≥ 6 phone screens, ≥ 1 first-round onsite scheduled
- ☐ Question→story cheat sheet finalised
- ☐ Portfolio option picked

---

## Month 3 — Portfolio + Iterate (Weeks 9-12)

**Theme:** ship one polished public artifact, iterate resume from real screen data, second wave of mocks, first onsites likely land.

### Week 9 (2026-07-21 → 2026-07-27) — Resume iteration + Portfolio kickoff

**Coding (3 medium):** Pick from re-do queue (any unsolved problem from W1-W8). Light week on purpose.

**Resume iteration:** Based on W4-W8 phone-screen conversion data, rewrite [../resume-ai-infra.md](../resume-ai-infra.md):
- If apply→screen is < 25%: rewrite top-of-resume (summary + headline + first bullet) with 2 outside readers.
- If screen→onsite is < 40%: probably a phone-screen issue, not resume; instead re-record a screen and listen for filler.
- Update [../linkedin-rewrite.md](../linkedin-rewrite.md) with the same iteration; push to LinkedIn.

**Portfolio:** Kick off whichever artifact you picked in W8.
- **A (OpenClaw blog):** outline from [../portfolio/blog-openclaw-cost-aware-runtime.md](../portfolio/blog-openclaw-cost-aware-runtime.md); pull repo metrics; draft first 2 sections.
- **B (MCP server):** scope a useful server (e.g. wraps a GEICO-relevant external API — read-only). Write spec.
- **C (OSS PR):** identify the issue you'll tackle. Open the conversation thread with maintainer.

**System design:** Deliver doc 01 (LLM inference) cold, end-to-end, on whiteboard. Record yourself. The first time you do this it's painful; that's the point.

**Pipeline:** Phone screens should be at ≥ 2/week steady state.

### Week 10 (2026-07-28 → 2026-08-03) — Portfolio core + Mock #3

**Coding (3 medium):** Re-do queue.

**Portfolio:**
- **A (blog):** complete draft + figures. Show to 1 outside reader.
- **B (MCP server):** implement core read tool + 3 example prompts. Get it running locally with Claude Desktop / Cursor.
- **C (OSS PR):** PR opened and CI passing.

**System design:** Deliver doc 04 (eval pipelines) cold. Same recording protocol.

**Mock #3 (behavioral):** Book this week. Partner asks 6 random STAR prompts + 1 follow-up each. Time each answer. Anything > 3 min gets shortened.

**Pipeline:**
- Comp data first pass: pull levels.fyi numbers for top 5 active companies at your target band. Save to [negotiation-and-offers.md § Comp data](negotiation-and-offers.md).

### Week 11 (2026-08-04 → 2026-08-10) — Portfolio polish + 1st Onsite likely

**Coding (3 medium + 1 hard):** Re-do queue + 1 new hard.

**Portfolio:**
- **A:** final polish + publish to a writing surface (Substack / personal blog / GitHub). Share to LinkedIn + Twitter + send to active recruiters.
- **B:** publish MCP server to Anthropic registry; document in README; share.
- **C:** PR merged or in active review with maintainer engagement.

**System design:** Deliver doc 03 (agent orchestration) cold.

**Onsite #1 likely lands this week.** Day-before checklist:
- Re-read [company-briefs.md](study-materials/company-briefs.md) for the company + the JD; pull 3 specific phrases into your "why this team" answer.
- Re-read [system-design-cheatsheet.md](study-materials/system-design-cheatsheet.md) sections for the surfaces most likely to come up at that company (per the brief).
- Re-read [behavioral-question-bank.md](study-materials/behavioral-question-bank.md) sections likely to come up (A & B for HM screens; G for Anthropic; F for Cursor).
- Re-read the deep dive matching the project they cited in your recruiter call.
- 20-min sprint of the company's interview style (Cursor = live IDE; Anthropic = practical code; Modal = systems depth).
- Sleep ≥ 7 hrs.

**Post-onsite debrief:** Within 2 hrs of leaving, write into [target-companies.md](../target-companies.md): what went well · what bombed · what they liked · gut conversion read · per-interview summary.

### Week 12 (2026-08-11 → 2026-08-17) — One-pager update + Mock #4

**Coding (3 medium + 1 hard):** Re-do queue + 1 hard.

**Portfolio one-pager:** Update [../portfolio/one-pager.md](../portfolio/one-pager.md) with the now-shipped artifact as the lead. Send to:
- Anyone who replied to a referral or recruiter (warm reactivation)
- Recruiters at Tier-2 companies you haven't applied to yet
- 2-3 Tier-1 hiring managers identified from LinkedIn (cold but with a specific hook)

**System design:** Deliver doc 06 (GPU autoscaling) cold.

**Mock #4 (system design):** Topic = the design surface for any onsite booked into Months 4-5.

**Month 3 exit gate:**
- ☐ ~58 LC problems cumulative (~50 mediums + ~6 hards)
- ☐ Portfolio artifact shipped publicly + linked in resume and LinkedIn
- ☐ Resume iterated; LinkedIn refreshed
- ☐ 4 mocks logged
- ☐ ≥ 10 phone screens cumulative; ≥ 2 onsites scheduled or completed
- ☐ Comp data captured for top 5

---

## Month 4 — Onsite Rehearsal + First Wave of Loops (Weeks 13-16)

**Theme:** polish 3 staff-level deep dives, run 2-3 lower-stakes onsites (practice loops at companies you want but aren't top choice), keep apply funnel warm.

### Week 13 (2026-08-18 → 2026-08-24) — Deep Dive #1 polish + 1st wave onsite

**Coding (2 medium + 1 hard):** Light. Re-do queue + 1 hard.

**Deep Dive #1 — Artifactory 99.99%:** Polish to 30-min keynote quality. Outline in [onsite-deep-dives.md](onsite-deep-dives.md). Practice the 3-min compact version too. Record both.

**System design:** Deliver doc 05 (training orchestration) cold.

**Onsite this week (if booked).** Same day-before checklist as W11. Post-onsite debrief same day.

### Week 14 (2026-08-25 → 2026-08-31) — Deep Dive #2 + Mock #5

**Coding (2 medium + 1 hard):** Re-do queue + 1 hard.

**Deep Dive #2 — OpenClaw cost-aware runtime:** Polish to 30-min keynote. Practice "what would you do differently" answers; this is the question that separates Staff from Senior. Pair with your shipped blog post (W11) — the artifact is the evidence.

**System design:** Deliver doc 07 (multi-tenant cost) cold.

**Mock #5 (system design with hostile interviewer):** Ask the partner to push hard on failure modes. Topic: GPU autoscaling or inference cost (whichever your next onsite needs).

**Pipeline:**
- After every 1st-wave onsite, get a 1-line read from the recruiter ("do you have a sense of timing?"). Use that to start stacking offers into a 2-3 week window.

### Week 15 (2026-09-01 → 2026-09-07) — Deep Dive #3 + 2nd wave application surge

**Coding (2 medium + 1 hard):** Re-do queue + 1 hard.

**Deep Dive #3 — Claude/Cursor/MCP enterprise rollout:** Polish to 30-min keynote. This is your most "AI-native" deep dive and most likely to land at Anthropic / Cursor / OpenAI / Databricks. Practice with the MCP bridge BRD as a handout.

**System design:** Deliver doc 02 (vector DB) cold.

**Apply surge:** Send 5-8 more applications to **Tier-1 or Tier-2 companies you haven't applied to yet**. The point: by Month 5, you want a 2nd wave of onsites landing in W17-19 to stack against the 1st wave's offers.

### Week 16 (2026-09-08 → 2026-09-14) — Negotiation Rehearsal + Mock #6

**Coding (2 medium):** Re-do queue only.

**Negotiation rehearsal:** Read [negotiation-and-offers.md](negotiation-and-offers.md) + [outreach-templates.md § 9-12](study-materials/outreach-templates.md) end-to-end. Rehearse the "ask" script **aloud** with a partner playing the recruiter. Cover:
- Initial response to a verbal offer ("I'm excited; when can I see the written offer?")
- The competing-offer leverage script
- Walking back from an aggressive ask without losing face
- Asking for sign-on / stock refresh / start-date flexibility

**System design:** Deliver doc 08 (prompt/eval registry) cold. (You've now re-delivered all 8 designs cold over Months 3-4.)

**Mock #6 (behavioral, with deep dive):** Combo session — 15 min STAR Q&A + 30 min deep dive. Topic: pick the deep dive your next onsite is most likely to ask for.

**Month 4 exit gate:**
- ☐ ~75 LC cumulative (~58 mediums + ~17 hards)
- ☐ All 3 deep dives polished + recorded
- ☐ All 8 designs re-delivered cold
- ☐ 6 mocks total logged
- ☐ ≥ 2 first-wave onsites complete; ≥ 2 second-wave onsites scheduled
- ☐ Negotiation script rehearsed aloud
- ☐ Comp data refreshed (data older than 6 weeks is stale)

---

## Month 5 — Live Loops + Offers + Decision (Weeks 17-20)

**Theme:** execute the 2nd wave of onsites, stack offers into a single decision window, negotiate, close.

### Week 17 (2026-09-15 → 2026-09-21) — Onsite Wave 2 starts

**Coding:** 1-2 problems only, re-do queue. The interviews are happening; protect cognitive load.

**Onsites this week (Wave 2):** Same day-before checklist + same-day debrief.

**Drive timelines:** When a recruiter sends positive feedback, **explicitly state your timeline** ("I'm interviewing with several aligned teams and expect to be at decision around Oct 10. Can your process align with that?"). This is the single most important sentence you say in Month 5.

**Behavioral:** Brief STAR refresher — re-read [star-stories.md](star-stories.md). Don't add new stories.

### Week 18 (2026-09-22 → 2026-09-28) — Onsite Wave 2 continues + Offer #1 likely

**Coding:** Optional warmup only.

**Offers landing:** When the first verbal offer comes:
- Express genuine excitement.
- Ask for the written offer in email by EOD.
- Buy yourself 5-7 days to evaluate ("I want to give this the serious consideration it deserves").
- **Do not negotiate on the first call.** Negotiation happens after the written offer + after you've had 24 hrs to think.

**Decision matrix:** Open the template in [negotiation-and-offers.md § Decision matrix](negotiation-and-offers.md). Pre-populate the weights (comp · team thesis fit · learning velocity · location · risk). Don't open this for the first time during a live call.

### Week 19 (2026-09-29 → 2026-10-05) — Closing remaining loops + Offer #2

**Coding:** 0 unless re-doing favourites.

**Final loops:** Whatever's still in flight, focus everything here. After each interview, immediate debrief.

**Use Offer #1 as leverage:**
- Tell every other active company: "I have an offer in hand; can we accelerate?" Be honest about timing; don't fake it.
- For top-choice companies, ask the recruiter to expedite (most can if the offer is real).

**Negotiation:** Once written offers are in, the ask script from W16 goes live. Aim for 2+ rounds of back-and-forth before signing anything.

### Week 20 (2026-10-06 → 2026-10-11) — Decision Week

**Coding:** Zero.

**Decision:** Compare via [negotiation-and-offers.md § Decision matrix](negotiation-and-offers.md). Weight by: comp · team thesis fit · learning velocity · location/commute · risk profile. Sleep on the answer for ≥ 24 hrs before accepting.

**Soft-close:** Decline non-chosen offers cleanly with "would love to stay in touch" note. Those recruiters become your friends for Round 2 in 18-24 months.

**Resignation prep:** If you've signed:
- Draft GEICO resignation note (2 weeks notice; gracious tone; don't burn bridges).
- Schedule the conversation with your manager — voice or in-person, never text.
- Do not tell anyone at GEICO until the offer is signed and the start date is set.

**Reflective writeup (Sun Oct 11):** Write 1 page in [mock-interviews.md § Reflections](mock-interviews.md) covering: 3 things you wish you'd started earlier; 3 things you'd cut; what to tell future-you.

---

## Daily template (weekday)

| Block | Duration | Activity |
|-------|----------|----------|
| Morning before work | 30 min | 1 LC problem (read + plan, code at lunch if time-boxed correctly) |
| Lunch | 30 min | Finish LC + write 1-line pattern note in [coding-log.md](coding-log.md) |
| Evening | 60 min | The "other" block for that day (system design / STAR / mock / phone screen prep / portfolio) |

Weekend:
- Sat 2-3 hrs: mock interview OR onsite rehearsal OR deeper system-design walkthrough OR portfolio chunk.
- Sun 1 hr: weekly checkpoint (next section).

## Weekly checkpoint log

Update every Sunday. Append; don't overwrite. Format:

```
Week N (YYYY-MM-DD):
- LC: x / target done; pattern weakness: ___
- Design: doc 0X delivered cold? Y/N; weakest area: ___
- STAR: # of stories rehearsed; weakest one: ___
- Portfolio (M3 only): % complete; blocker: ___
- Pipeline: applied x; screens x; onsites x; offers x
- Health: sleep avg ___ hrs; energy 1-5
- Adjust next week: ___
```

(Placeholders below — fill in weekly.)

```
Week 1 (2026-06-01):
Week 2 (2026-06-08):
Week 3 (2026-06-15):
Week 4 (2026-06-22):
Week 5 (2026-06-29):
Week 6 (2026-07-06):
Week 7 (2026-07-13):
Week 8 (2026-07-20):
Week 9 (2026-07-27):
Week 10 (2026-08-03):
Week 11 (2026-08-10):
Week 12 (2026-08-17):
Week 13 (2026-08-24):
Week 14 (2026-08-31):
Week 15 (2026-09-07):
Week 16 (2026-09-14):
Week 17 (2026-09-21):
Week 18 (2026-09-28):
Week 19 (2026-10-05):
Week 20 (2026-10-11):
```

---

## Company-specific surge prep

When an onsite lands, replace the week's "system design" block with the surge below.

### Anthropic
- **AI usage rule:** check with recruiter — SWE rounds typically no AI; ML rounds may allow Claude Sonnet as a tool. Practice both modes.
- **Coding:** practical, real-world Python; pair with one design.
- **System design:** lean on docs 01 (inference), 04 (evals), 06 (GPU autoscaling).
- **Behavioral:** values-heavy. Re-read Anthropic's published values; map 3 STAR stories to each value.

### Cursor (Anysphere)
- **Format:** 2-3 short technicals (45 min) + in-person 1-day project at SF/NY office.
- **Surge:** spend the day before the technicals using Cursor agent mode on an open-source repo. Be fluent in `Cmd+I`, `Cmd+K`, MCP tool calls, agent skills. Don't be the candidate fumbling the IDE.
- **Project day prep:** sleep + meals + travel buffer. The day is intense — bring snacks.
- **Design:** docs 03 (agent orchestration) + 04 (evals) are the surface.

### OpenAI
- **Coding:** distributed-systems flavoured. Python or Go.
- **Design:** doc 01 (inference) + 05 (training orchestration) + 07 (cost attribution) are the surface.
- **For Analytics Platform role only:** Rust/C++ required — skip unless you've committed to Rust prep.

### Modal
- **Systems depth bar:** higher than typical. Be ready to discuss container runtime internals, scheduling tradeoffs, GPU cold-start.
- **Surge:** read Modal's published blog posts (Erik Bernhardsson writes a lot). Know their custom file system + container runtime story.
- **Design:** docs 06 (GPU autoscaling) + 07 (cost) are key.

### Databricks
- **Coding:** standard LC mediums + 1 hard.
- **Design:** doc 03 (agent orchestration) for Agent Quality role; doc 05 (training) for AI Research Infra; doc 01 (inference) for AI Platform.
- **Behavioral:** their structured interview style — stick to STAR rigorously.

### Perplexity
- **AI-specific design:** RAG architecture, search infra at scale, LLM serving — read up before onsite.
- **Coding:** practical not LC-hard; design is the differentiator.
- **Surge:** spend an hour using Perplexity heavily. Pattern-match what trade-offs they made.

### Sierra
- **Format:** in-person SF.
- **Surge:** agent SDK + orchestration framework lit review. Read Bret Taylor's recent writing.
- **Design:** docs 03 (agent orch) + 04 (evals).

### Browserbase
- **Surge:** read Stagehand docs + Browserbase blog. Bring up OpenClaw early; it's the strongest "I've done this" credential they will hear.
- **Coding:** TypeScript bias.

---

## What I'd rebalance if the plan slips

**If apply→screen conversion < 25% by end of W4:** Use W9 resume iteration aggressively. Get 2 outside readers (a hiring manager and a peer at a target company).

**If screen→onsite < 40% by end of W7:** Re-record one of your phone screens (with consent); listen for filler, pacing, "I" vs "we". Adjust elevator pitch in [phone-screen-playbook.md](phone-screen-playbook.md).

**If 0 onsites by end of W12:** Pivot 2 hrs/week from coding to active referral chases (Path 2 + 3 in [../referrals.md](../referrals.md)). The funnel needs warm intros more than it needs more LC.

**If portfolio artifact slipping by mid-M3 (W10):** Drop scope, not quality. Better to ship a tight blog post than a sprawling unfinished one. Option B (MCP server) is easier to scope down than Option A (blog).

**If you're crushing the plan ahead of schedule:** Add 1 hard LC per week (cap at 25 total hards); deepen 1 system design with a written 1-pager you can send to interviewers as a follow-up; or build a second portfolio artifact.

---

## Don't do these

- **Don't grind LC > 1 hr/day.** Past 1 hr you're memorising rather than internalising patterns. Better: 1 problem, 30 min thinking, 10 min review, stop.
- **Don't write any new STAR story after Week 6.** Polish the 10 you have; new stories under interview pressure underperform polished ones.
- **Don't take > 1 mock per week.** Mocks cost real energy; the value is the debrief, not the volume.
- **Don't open the negotiation playbook for the first time during a live call.** Rehearse the ask script aloud in W16 before any offer call.
- **Don't tell your current employer until you have 1 signed offer in hand.** GEICO is a stable fallback; protect it.
- **Don't start a new portfolio artifact in Month 4 or 5.** Ship what you started in Month 3; the artifact serves interviews, not the other way around.
- **Don't take vacation in Weeks 17-20.** That window is where offers stack. Take vacation in Month 4 weeks 13-14 instead if you need a break.

---

## Summary table

| Month | Weeks | Focus | LC cumulative | Designs cumulative | STARs | Portfolio | Mocks | Apps | Screens | Onsites | Offers |
|-------|-------|-------|---------------|---------------------|-------|-----------|-------|------|---------|---------|--------|
| 1 | 1-4 | Foundation patterns + apply | 20 | 4 (delivered once) | 8 drafted | — | 0 | 15-20 sent | 2-3 | 0 | 0 |
| 2 | 5-8 | Depth + first mocks | 43 (+3 hards) | 8 | 10 polished | picked | 2 | 25 cumul. | 6-8 cumul. | 0-1 sched. | 0 |
| 3 | 9-12 | Portfolio + iterate | 58 (+6 hards) | 8 (re-delivered 4×) | 10 + cheat sheet | shipped | 4 | 30 cumul. | 10 cumul. | 1-2 | 0 |
| 4 | 13-16 | Deep dives + 1st loops | 75 (+17 hards) | 8 (re-delivered 8×) | 10 (refresher only) | shipped | 6 | 35 cumul. | 12 cumul. | 2-3 cumul. | 0-1 verbal |
| 5 | 17-20 | Live loops + decision | 85 (+20 hards) | — | — | — | 6-7 | 35-40 cumul. | 14 cumul. | 4-5 cumul. | **2+ signed** |
