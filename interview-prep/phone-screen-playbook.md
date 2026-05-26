# Phone Screen Playbook (Month 2 cadence: 3-5/week)

Goal: 3-5 phone screens per week, tracked against the cumulative number you've applied for, with conversion rates visible at-a-glance. Track in `target-companies.md` (the "Application logging" table) — this doc is the playbook for what to do *inside* a screen.

## Stages of a typical loop

```
cold/referral submitted -> recruiter screen (20-30 min)
                        -> hiring-manager screen (30-45 min)
                        -> tech screen (45-60 min)
                        -> onsite loop (3-5 hours)
                        -> offer
```

Phone screens = the first two. The recruiter screen filters for fit and basic credibility; the hiring-manager screen filters for tech depth and motivation.

## Recruiter screen — what they really ask

- "Tell me about yourself" → use the **60-second elevator pitch** below.
- "Why this company / why now?" → 2-sentence company-specific answer.
- "Compensation expectations" → defer politely; "I'd want to learn more about the level and team scope first, but my current comp band is roughly $X-$Y" only when pushed.
- "Location and work setup" → answer plainly (Fremont CA; hybrid Bay Area or remote-US).
- "Visa / work authorization" → U.S. Citizen.

### 60-second elevator pitch

> I'm a Staff platform engineer who builds production agentic systems and the platforms that run them. At GEICO I lead the Artifact Management Platform — I drove our Artifactory from monthly incidents to a four-nines availability SLO — and I'm shipping a portfolio of Claude Agent SDK + MCP + Cursor work into our 2026 DE AI Showcase. Outside of work I led the OpenClaw cost-aware runtime plugin at Purdue (token / cost / step governance for browser agents) and I run SmartTuna, a LangGraph multi-agent stock-analysis product. Twenty years of platform engineering underneath, MS in AI in progress at Purdue, U.S. citizen.

### Company-specific "why now" two-sentence template

> I've been doing AI-augmented platform engineering daily for the last year and shipped a cost-aware runtime for browser agents as my Purdue final project. [Company] is one of a small set of places where that specific intersection — agentic systems plus the infrastructure they run on — is the actual job; that's why I'm raising my hand for this role.

## Hiring-manager screen — pattern

Expect three buckets:

1. **Walk me through a project** → pick from STARs in `interview-prep/star-stories.md`. Default first pick is OpenClaw (it's deep + recent + concrete). Backup: Artifactory 99.99% turnaround.
2. **System-design lite** (30 min) → likely sliced from `interview-prep/system-design/*.md`. Common drops: "how would you scale a small piece of [their product]", "what would you change about [hot AI tooling]", "design a tiny version of X."
3. **Why you, why us, what do you want?** → close strong:
   - "I'm picking by team, scope, and proximity to the model. The work you're hiring for has all three."
   - "I want to keep going on the agentic-systems + platform reliability intersection; this role is exactly that."

### Pre-screen, 15 min checklist

- Read the JD twice; underline two specific phrases to mirror back.
- Read 2-3 recent engineering blog posts from the company.
- Skim the hiring manager's LinkedIn for shared context (alumni / past employers / public work).
- Open the relevant STAR + design doc in another tab.
- Glass of water; phone in another room.

### During

- Mirror language. If they say "agent runtime" you say "agent runtime"; if they say "agent loop" you say "agent loop."
- Have one concrete number ready per story (99.99%, $600K/yr, 5,000 repos, 11 package types, 282 associates, four nines).
- End with one question that proves you know their work: "I noticed [X recent thing]; is that team likely involved in this role's first 6-month roadmap?"

### After (within 30 minutes)

Log in `target-companies.md`:

| Date | Company | Role | Stage | Outcome | Next |
|------|---------|------|-------|---------|------|
| | | | hiring-manager | advanced / hold / rejected | tech screen YYYY-MM-DD |

Plus a 3-bullet note for yourself:

- What you said that landed.
- What you said that wobbled.
- One thing to add to STARs / pitch.

## Tech screen — pattern

Coding (45 min) or system design (45 min) or trace-the-bug (rarer).

- **Coding:** use `interview-prep/coding-log.md`. Warm up with 2 problems same morning.
- **Design:** open the relevant doc; rehearse the 5-min "requirements clarification" out loud once.

## Conversion rate dashboard

Track this in `target-companies.md`. Bare minimum monthly snapshot:

| Stage | Count | Conversion vs prior stage |
|-------|-------|---------------------------|
| Applied | (n) | — |
| Recruiter screen | (n) | (%) |
| Hiring-manager screen | (n) | (%) |
| Tech screen | (n) | (%) |
| Onsite | (n) | (%) |
| Offer | (n) | (%) |

Healthy Staff-IC conversion at AI-native companies looks roughly: 30-50% apply → recruiter, 50-70% recruiter → hiring manager, 30-50% hiring manager → tech, 30-50% tech → onsite, 25-40% onsite → offer.

If yours is much worse at a specific step, that's where to invest:

- Apply → recruiter low → resume needs work (or you're applying to mis-matched levels).
- Recruiter → HM low → elevator pitch / motivation answer needs work.
- HM → tech low → STAR depth and "why" answer.
- Tech → onsite low → fundamentals (coding, design).
- Onsite → offer low → integration of all of the above + behavioral edge cases.

## Stress test calendar

In Month 2, aim for at least one phone screen on each of M / T / Th — give yourself W to recover and a midweek prep window. Two on Friday is fine for less-prepared targets. Avoid weekends.

## Don't lose the slow lane

When momentum gets going, you'll over-index on phone screens and stop applying. Set a rule: **apply to 2 new roles every Monday morning**, no matter how busy. The pipeline empties faster than you think.
