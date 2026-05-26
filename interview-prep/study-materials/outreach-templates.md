# Outreach & Communication Templates

Copy-paste-ready text for every email / DM / LinkedIn message you'll send during the 5-month search. Each template has the **send-when**, **fill-in fields** marked in `{curly braces}`, and the **trap** to avoid.

For voice and tone: warm, specific, short. The first 60 seconds of an interviewer's read is the test; if they get to sentence 3, you've won.

---

## 1. Cold LinkedIn message to a hiring manager / IC at a target company

**Send when:** You've identified an HM or senior IC on the team that owns the role; you have a *specific* hook (not just "AI infra").

**Length:** 4-5 sentences. Under 700 characters total.

**Template:**

```
Hi {name},

I came across the {role title} role on {company}'s careers page and noticed it
explicitly mentions {a phrase from the JD - 5-8 words}. That's exactly the
problem I've been solving at GEICO for the last year — I {1-sentence specific
example with a number or named artifact}.

I'm planning to apply, but wanted to ask first: would a 15-min chat be useful
to see if it makes sense before I formally submit? Happy to send a one-pager
ahead of time so you can decide if the conversation is worth your time.

Best,
Ming
```

**Trap:** Don't open with "I'm interested in your company." Open with a specific reference to what *they're* doing. They get 50 of the first kind a week.

**Example (Anthropic Dev Productivity):**

```
Hi Mark,

I noticed the Anthropic Staff+ Developer Productivity role explicitly mentions
"developer tooling that deeply integrates Claude into engineering workflows."
That's exactly what my team and I have been shipping at GEICO this year — I
authored the Cursor x Claude Code MCP bridge BRD and shipped 4 internal MCP
servers (JFrog, Slack, ADO, GitHub) plus 3 Cursor agent skills used in
production on-call.

I'm planning to apply, but wanted to ask first: would a 15-min chat be useful
before I submit? Happy to send a one-pager ahead.

Best,
Ming
```

---

## 2. Referral request to a current or former colleague

**Send when:** You have a colleague who works at — or is one degree from — a target company. Use sparingly; ask for one referral per quarter per person max.

**Template:**

```
Hey {name},

Hope you're well — saw your update about {something they posted recently / a project they shipped}.

I'm wrapping up a 5-month-out job search aimed at AI-infra / agent-platform IC roles, and {company} is one of my top targets. The most relevant role is {role title} ({URL}).

If you have any internal sense of the team — and especially if you'd be willing to put my resume in front of the hiring manager — I'd really appreciate it. I'm attaching a one-pager + my resume so you can scan the fit in 30 seconds.

No pressure either way. Happy to do the same for you anytime.

Best,
Ming
```

**Attach:**
- [../../portfolio/one-pager.md](../../portfolio/one-pager.md) (rendered to PDF)
- `Mingresume.docx`

**Trap:** Don't ask them to "vouch for you" or "say nice things." Ask them to forward your resume. That's a much lower ask and gives them an easy yes.

---

## 3. Recruiter response — initial outreach reply

**Send when:** A recruiter messaged you. Don't ghost; reply within 24 hours even if you're not interested.

**If interested:**

```
Hi {recruiter},

Thanks for reaching out. The {role title} role looks like a strong fit on my
side — {1 sentence why}.

I'm targeting decisions around {month, e.g., October 2026}, so timing works.
A 30-min intro call would be great. Here's my Calendly: {link}, or pick a time
that works and I'll match it.

Two quick context items:
- {salary range — I'm looking in the range of $X-Y base + equity at the band}
- {geo / hybrid expectations — I'm Indianapolis-based; happy to discuss hybrid/relocation}

Best,
Ming
```

**If not interested but want to keep door open:**

```
Hi {recruiter},

Thanks for reaching out. {Company} is on my radar but {role title} isn't the
right fit for me right now — I'm focused on {AI infra / agent platform IC
roles}. If a more aligned role opens up, please do reach back out.

Best,
Ming
```

**Trap:** Don't oversell on the first reply. Be plain about salary, geo, and timing — those are the disqualifiers and they'll come up anyway. Get them out of the way fast.

---

## 4. Phone-screen prep — confirmation note

**Send when:** The recruiter confirms the screen time, ~24h before.

**Template:**

```
Hi {recruiter},

Confirming the {date/time} screen with {interviewer name} for the {role title}
role.

Two quick questions to help me prep:
1. What format will this screen take — primarily behavioral / technical / both?
2. Anything specific {interviewer} typically wants candidates to come ready to
   discuss?

See you {date/time}.

Best,
Ming
```

**Trap:** Don't ask too many questions; you're checking that you understand the format. Two is the right number.

---

## 5. Post-screen thank-you note

**Send when:** Within 24 hours of any interview round (screen or onsite round).

**Template:**

```
Hi {interviewer name},

Thanks for the time today. I especially appreciated {a specific thing from the
conversation — a question they asked that landed, a problem they shared, a
piece of feedback}.

A follow-up on {something you discussed}: {1-2 sentences with a sharper answer
than you gave in the moment, OR a link to something relevant}.

Looking forward to next steps.

Best,
Ming
```

**Example (good):**

```
Hi Sarah,

Thanks for the time today. I appreciated the question about prefix caching
vs. KV cache eviction tradeoffs — it pushed me to think more carefully about
when one matters over the other.

A follow-up: you asked about prefix caching at the request level vs. session
level. I think the right move depends on tenant access patterns — for stable
system prompts you want session-level; for prompt-template variants, you want
content-addressed caching at the request level. There's a clean discussion of
both in the vLLM paged-attention paper if you haven't seen it.

Looking forward to next steps.

Best,
Ming
```

**Trap:** Don't write a generic thank-you. The follow-up bullet is the value. If you can't think of a follow-up, skip it and keep the thank-you short.

---

## 6. Onsite thank-you (with multiple interviewers)

**Send when:** Within 24 hours of the onsite, *one* note per interviewer, individually.

Each note is the same template as #5 but **tailored**. The shared content across notes is OK; the *specific reference* (the line about what landed in that interviewer's round) must be unique per note.

**Trap:** Don't BCC the recruiter on the per-interviewer notes; that's needy. Send one separate note to the recruiter summarising.

---

## 7. Status check — "haven't heard back" follow-up

**Send when:** 7-10 days after a screen with no response. (For onsite results: 14 days.)

**Template:**

```
Hi {recruiter},

Quick check-in — I wanted to follow up on the {role title} interview from
{date}. Any update on next steps?

I'm also actively interviewing elsewhere with timelines around {a specific
date — e.g., end of October}, so if there's any way to align on a decision
window, let me know.

Best,
Ming
```

**Trap:** Don't say "just checking in" or "circling back." Say what you want.

---

## 8. Competing-offer leverage note

**Send when:** You have a real offer in hand and want to accelerate another company's process.

**Template:**

```
Hi {recruiter},

Quick update — I received a written offer from {company} this morning with a
{date} response deadline. {Target company} is genuinely my top choice, and
I'd like to see if there's any way to accelerate the remaining steps so I can
make a fully informed decision.

I have {next round / onsite / final round} on the calendar; if there's any
way to consolidate or move that up, I'd really appreciate it.

If you can't accelerate, that's also useful information — I'd rather know
now than later. Either way, thank you for the process so far.

Best,
Ming
```

**Trap:** Be **honest**. If you don't have a real offer, don't claim one — the AI-infra industry is small and people compare notes. If your other offer is a Tier-2 you don't actually want, don't pretend it's Tier-1.

---

## 9. Verbal-offer response (buying time)

**Send when:** A recruiter calls with a verbal offer.

**On the call:**

```
"Thank you so much — I'm genuinely excited. Before we get into specifics, can
you send the written offer to me by EOD? I want to make sure I give it the
serious consideration it deserves, and I'll come back to you within 5-7 days
with any questions."
```

**Trap:** Don't accept on the call. Don't negotiate on the call. Get the written offer first.

---

## 10. Written-offer initial response

**Send within:** 24 hours of receiving the written offer.

**Template:**

```
Hi {recruiter},

Thanks for the offer for {role title} at {company} — it's a real pleasure to
have gotten this far. I'm spending the next few days reviewing carefully and
will come back to you with any questions by {date 5-7 days out}.

In the meantime, two clarifying questions:
1. {Component-specific question — e.g., "Can you confirm the vesting schedule
   on the equity grant?"}
2. {Other clarifying question — e.g., "What's the band / level for this role,
   and is there flexibility on base / equity composition?"}

Looking forward to digging in.

Best,
Ming
```

**Trap:** Don't ask for a number bump in the first response. Get the facts straight first.

---

## 11. Counter-offer / negotiation ask

**Send when:** You've reviewed the offer, gathered comp data, and decided on your ask.

**Template:**

```
Hi {recruiter},

I've spent the past few days digging into the offer and the role, and I want
to reiterate how excited I am about {team / mission specific thing}.

I'd like to ask about a few specifics:

- **Base salary.** Based on levels.fyi data for {comparable companies at the
  band — e.g., L5 SWE at Anthropic, IC4 at Cursor, comparable at Modal}, the
  range is $X-Y. The current offer of $Z is below that. Could we adjust to
  ${target}?
- **Equity.** {Same structure if asking on equity.}
- **Sign-on.** I'm leaving a stable role at GEICO mid-fiscal-year; a sign-on
  of ${amount} would offset the loss of {bonus / pro-rated equity / etc.}.

Two of these would put the offer where I need it to make a confident decision.
{Company} is genuinely my top choice; I'd like to find a path to yes.

Best,
Ming
```

**Trap:** Don't ask for all four levers (base + equity + sign-on + start-date). Pick 2; that's the credible ask. Asking for all 4 reads as inexperienced.

---

## 12. Decline an offer cleanly

**Send when:** You've accepted elsewhere or you're declining.

**Template:**

```
Hi {recruiter},

Thank you again for the offer and for the thoughtful process. After careful
consideration, I've decided to accept a different role that's a closer fit
for the kind of work I want to be doing next.

{Company} was genuinely high on my list, and I have a lot of respect for the
team I met with. If circumstances change in 18-24 months and the timing
aligns, I'd love to reconnect.

Best,
Ming
```

**Trap:** Don't say "I got a better offer." That's true but it lands badly. Say "closer fit." Don't disparage their offer or process.

---

## 13. Resign from GEICO

**Send when:** You have a signed offer with a confirmed start date.

**Format:** This is a *conversation* first — never a written first contact. Schedule 30 min with your manager, voice or in-person.

**Verbal opener:**

```
"Thanks for making time. I want to let you know I've accepted an offer to
join {company} as a {role title}, with a start date of {date}. I'm planning
to give the standard two weeks; today is my first day of notice."

[Pause. Let them respond.]

"I want to make this transition as clean as possible for the team. {Suggest a
specific transition plan — who picks up what, what documentation needs
finishing, what handoff meetings we should hold.}"
```

**Written follow-up (same day):**

```
Hi {manager},

To put what we discussed in writing: I'm resigning from my role at GEICO
effective {two weeks out date}. I've accepted a position at {company}
starting {start date}.

It's been a real privilege to work on {AMP team / Artifactory / MCP rollout /
the four-nines turnaround}, and I'm proud of what we built together. I'll
focus the next two weeks on a clean transition — documentation, handoff,
and ensuring on-call coverage is stable.

Thank you for the latitude you've given me on the AI tooling work; it's been
one of the most professionally rewarding chapters of my career.

Best,
Ming
```

**Trap:**
- Don't surprise your manager via email/Slack. Voice first.
- Don't engage with counter-offers from GEICO unless you've genuinely changed your mind. Counter-offers accept rate is < 20% retention at 12 months for a reason.
- Don't badmouth GEICO or the role to anyone. The industry is small.

---

## 14. Re-activation message (months later)

**Send when:** A company you applied to didn't move forward, and 6-12 months have passed. You're now in a new search or you have a new artifact to share.

**Template:**

```
Hi {recruiter or HM},

Last fall I interviewed for the {role title} role at {company} and it didn't
work out. Since then I've {shipped a major artifact — blog, OSS contribution,
new role}, which I think makes the fit notably stronger for {original or new
role}.

Specifically: {2 sentences with concrete evidence}.

If there's an open role that fits, I'd love to reconnect. If not, no problem —
just wanted to keep you in my loop.

Best,
Ming
```

**Trap:** Don't reactivate if you have nothing new to show. Wait until you do.

---

## 15. Generic LinkedIn connection request to a target-company IC

**Send when:** You want to build a relationship, not ask for anything yet.

**Template (must fit in LinkedIn's character limit ~300):**

```
Hi {name}, came across your work on {specific thing — a talk, blog post, OSS
commit}. I'm doing {related work — OpenClaw cost-aware runtime, MCP
servers}, and your post on {specific topic} sharpened my thinking on
{specific point}. Would love to connect.
```

**Trap:** Don't use the default LinkedIn "I'd like to add you to my professional network." That's anti-signal. Always customize.

---

## Universal voice/tone rules

- **Warm, specific, short.** Three adjectives. If your message fails one, rewrite it.
- **No fluff openers.** "I hope this finds you well" — cut.
- **No emoji unless replying in kind.** Different industries have different norms; AI startups in 2026 lean light-emoji but it's not universal.
- **Sign off "Best, Ming"** — not "Cheers", "Regards", "Sincerely." "Best" is the default; vary it occasionally if a specific thread has built a particular voice.
- **Send during business hours of the recipient's timezone.** Most recruiters work 9-5 local; respect that and your reply rates double.
- **One thread per topic.** Don't pile a question and a thank-you and a status check into one message. Separate threads = separate priority signals.

---

## What I deliberately didn't include

- **Cold email templates to executives.** Generally low ROI for a 5-month search. Better to use referrals or HMs.
- **Aggressive "you should hire me" pitches.** They land badly at AI-native shops. Show, don't tell.
- **Multi-paragraph "story" emails.** Three short paragraphs is the upper bound. Most messages should be 1-2.

---

## Tracking

Every message you send should go into [../../target-companies.md](../../target-companies.md) Notes column with the date and a one-line summary. Otherwise you'll lose track of who you've followed up with.
