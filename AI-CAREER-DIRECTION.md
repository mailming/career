# AI Career Direction — Ming Jia

_Synthesized 2026-07-14 from deep-research round 1 (18 verified findings) + workspace profile._
_Inputs: applied/integration engineering; open to 10–25% cut but not wealthy, needs steady income; passions = AI film/video generation + AI robotics integration; wants work he genuinely enjoys._

---

## The one-sentence answer

**Anchor your career on the applied-AI / agent-platform / Forward-Deployed path (your existing skills, the tightest and most age-friendly market, and probably NO pay cut) — and point that anchor at a robotics or autonomy company so the job itself touches a passion. Treat AI video as a passion + opportunistic target, not the thing your rent depends on.**

---

## Why this, in plain terms

You are not trying to become something you're not. You already are the profile the 2026 market is short on:

- **The market wants seniors, not juniors.** AI-native firms hire ~15% *fewer* entry-level people and ~20% *more* senior people (HBS/INSEAD WP 26-090). The recent contraction hit devs aged 22–25 (~20% drop); over-40 employment stayed flat. Age is a real headwind on *research* and *junior* tracks — it is **not** a meaningful headwind on staff/infra/platform/solutions/forward-deployed tracks. That's your lane.
- **Your premium grows with level.** AI-skills wage premium: Entry +6.2%, Senior +14.2%, **Staff +18.7%**. Seniority is an asset here, not a liability.
- **The bottleneck is deployment, not modeling.** Enterprise AI postings sit 134% above 2020 baseline (vs 6% for all jobs). The scarce person is the one who can *wire models into real systems reliably* — which is literally your GEICO job (MCP bridges, agent SDK, CI/CD, four-nines reliability).

So the honest framing: you're not "a 48-year-old breaking into AI." You're **a Staff platform engineer with rare AI-native production experience, choosing which AI vertical to point at.**

---

## The money reality (important, since you're not rich)

Your "10–25% cut is OK" worry is probably **unnecessary if you stay on the infra/applied path.** Bay Area data:

| Path | Total comp (Bay Area, 2026) | Source confidence |
|------|------------------------------|-------------------|
| Applied AI / FDE at applied-AI startup | ~$250K–$640K | medium (corroborated) |
| FDE / Applied at frontier lab | $385K–$1M+ | medium |
| Enterprise AI solutions/FDE (F500) | $190K–$420K | medium |
| SF AI Engineer (general) | median TC ~$211K; senior $340K–$550K | high |
| Robotics infra (e.g. Figure median TC) | ~$247K | medium |
| Luma AI Forward Deployed Engineer (real posting) | $170K–$290K | high |

The cut only shows up if you try to enter a **new domain as a junior** (e.g. cold-switching into video research). Stay on infra/platform/FDE and you're likely at or above current comp.

---

## Your two passions — the honest verdict

### AI robotics integration → **a real, fundable career for you**
The scary barrier (C++/ROS/controls) applies to *embedded/controls* roles — that claim was actually **refuted** in the research for the roles you'd target. Robotics companies desperately need **cloud infra, fleet management, data pipelines, simulation infra, and MLOps-for-robot-learning** — your exact skillset, no C++ required. Round 1 flagged **1X's "Software Engineer, Cloud & Infrastructure"** as an ideal fit. Figure, Waymo, Nuro, Apptronik all have this shape of role. **This is the passion you can actually get paid for.**

### AI film/video generation → **keep as passion + opportunistic target, not the anchor**
It's well-capitalized (Runway raised $315M at $5.3B in Feb 2026) and it does hire non-research people — **Luma hires Forward Deployed Engineers**, Runway hires backend/product/DevRel. But it's a *thin* market: a handful of firms, small teams, few net-new applied roles per quarter, fierce competition. The creator/prosumer economy is real but power-law (a few earn a lot, most earn little). **Verdict:** apply to a Luma/Runway FDE role opportunistically, make AI films on the side for joy (and as portfolio proof), but don't bet your income on it.

---

## Ranked paths (income viability × interest fit × skill leverage)

| Rank | Path | Income | Interest | Skill leverage | Verdict |
|------|------|:------:|:--------:|:--------------:|---------|
| **1** | **Applied-AI / DevAI / infra role AT a robotics or autonomy company** (Waymo DevAI, 1X Cloud & Infra, Nuro, Figure infra) | High | High (robotics) | Very high | **Primary target — hits all three axes** |
| **2** | **FDE / Applied AI Engineer** at frontier lab or applied-AI startup (Anthropic, OpenAI, Palantir, Scale, Sierra, Decagon) | Highest | Neutral | Very high | **Best income + safety net; run in parallel** |
| **3** | **Applied/FDE/solutions at an AI-video company** (Luma, Runway, ElevenLabs) | Good | Highest | High | **Opportunistic — apply when a fit opens** |
| 4 | AI-video **creator/side income** | Low/variable | Highest | Medium | Passion + portfolio, not anchor |
| 5 | Core ML research / robotics controls | — | — | Low | **Not recommended** — wrong pivot for your profile |

**The insight:** Rank 1 dissolves the false choice between "safe boring infra" and "passion." A DevAI/platform role at Waymo or a cloud-infra role at 1X *is* infra work *and* robotics — no compromise.

---

## Waymo is your single best shot — and you already started it

You have `interview-prep/waymo-devai-surge.md` and it's genuinely your warmest, best-fit target: it's **robotics/autonomy + developer tooling + exactly your GEICO DevAI work** (inner-loop code acceleration, outer-loop triage, MCP/agents). Senior Staff, $298K–$368K base. This is Rank-1 embodied. **Prioritize it.**

---

## Action plan (reuses your existing, currently-stalled workspace)

Your 5-month plan is excellent but stalled (coding log empty, Tier-1 apps unsent, target list untouched since May 25). Don't rebuild — **re-aim and restart it** around this thesis:

1. **This week:** Fire the Waymo DevAI application + the 15 pre-written Tier-1 cold notes in `applications-tier1.md`. Volume now; the calendar is the constraint.
2. **Re-tier your target list** around Rank 1 + 2:
   - *Robotics infra:* Waymo (DevAI), 1X (Cloud & Infra), Figure (infra/solutions), Nuro, Apptronik, Physical Intelligence
   - *Applied/FDE anchor:* Anthropic, OpenAI, Palantir, Scale, Sierra, Decagon, Cognition
   - *Video (opportunistic):* Luma (FDE), Runway (backend/product), ElevenLabs
3. **Ship ONE public artifact** that proves the bridge — you already have the raw material: publish the **OpenClaw cost-aware runtime** (browser-agent infra — reads as both agent-platform AND robotics-adjacent "physical AI" governance) or the **SmartTuna** multi-agent system. Public + linkable beats "in-flight."
4. **Positioning for 48:** lead every resume/pitch with *"Staff platform engineer + AI-native production experience."* Prefer **referrals over cold applies** (AI startups skew pedigree/network — your SF location + in-progress MS AI help). Favor age-friendlier segments (**enterprise AI, big-tech AI orgs, robotics infra, Waymo**) over junior-heavy seed-stage startups.
5. **Feed the passion without betting on it:** make 2–3 AI short films this quarter. If one lands, it's a portfolio piece for a Luma/Runway FDE conversation. If not, you enjoyed it. Either way you win.

---

## The sincere part

At 48, needing steady income, wanting work you love — the mistake would be a romantic leap into video research or a robotics controls role you'd have to reboot your skills for. You don't need to leap. The market is handing experienced infra people a rare moment, and the robotics-infra + DevAI lane lets you do work you'll actually enjoy *using the skills you already have*, at comparable pay, with age working *for* you. Point the anchor at robotics/autonomy, keep filmmaking as the thing that feeds your soul, and run the plan you already built.
