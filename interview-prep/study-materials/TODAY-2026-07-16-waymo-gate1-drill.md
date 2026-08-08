# TODAY Drill — Waymo Gate 1 (Thu Jul 16)

**How to use this file:** Do not invent content. Read the scripts below **out loud**, time yourself, then do the LC problem. Total ~90–100 min.

**Frame (say this once before every script):**  
*"I accelerate the humans building the Driver — I build tools for Waymo's engineers, not the Driver itself."*

---

## Block 1 — What “perception” means (read this first — you are NOT expected to be an AV expert)

### You do not need a perception background

Waymo DevAI is **developer tools for Waymo’s software engineers**. You are not interviewing to train lidar models or write the Driver’s vision stack. Your Artifactory / MCP / Slack-bot / CI migration background is the real fit.

**Perception** (in Waymo’s world) just means:  
*the software that turns sensor data (cameras, lidar, radar) into “what’s around the car”* — e.g. “there’s a pedestrian at X”, “car ahead going Y mph”.

| Word | Plain English |
|------|----------------|
| **The Driver** | Waymo’s self-driving software stack |
| **Perception** | The part that “sees” the world (detect objects) |
| **Prediction / planning** | What might happen next / how the car should move (you can ignore details) |
| **Simulation / sim** | A recorded or synthetic drive they replay in software to test the Driver |
| **Replay** | “Play back that test run and look at what the software thought at time T” |
| **Ground truth** | The correct answer labels (human or trusted labels) for that scene |
| **Perception miss** | The Driver’s software *failed to see* something that was actually there in the test |

**Why DevAI cares:** When a sim test fails (“we missed a pedestrian at 12.3s”), a **Waymo engineer** spends hours digging through logs. DevAI would build an **agent/tool** that helps that engineer dig faster — same job shape as your Slack triage bot and RCA skills at GEICO, different domain nouns.

**Your honest interview line if they go deep on AV:**  
*"I'm not a perception researcher — I build the tooling layer. Enough vocabulary to design a debug assistant for those engineers: fetch replay at T, compare to labels, suggest hypotheses. Depth on sensors and model training stays with their specialists."*

---

### Step 1 — The only “3-step” you need (map it to GEICO)

Same pattern as your `#help-pkg-mgmt` triage bot:

| GEICO (you know this) | Waymo perception-debug agent (same shape) |
|-----------------------|-------------------------------------------|
| Ticket comes in Slack | Engineer reports: “missed pedestrian in scenario S at T=12.3s” |
| Bot pulls Artifactory / logs / MCP tools | Agent pulls **sim replay** + **labels** at that time |
| Bot suggests first-pass RCA | Agent **diffs** “what perception said” vs “what was true” |
| Skills: solve-case / close-case | Agent ranks causes + finds similar past tickets |

Memorize only this:

1. **Fetch** — get sim replay + perception output + ground truth at timestamp T  
2. **Diff** — what did we miss / misclassify?  
3. **Report** — ranked guesses + similar past failures (RAG); **human decides**; agent never ships Driver code  

### Step 2 — Speak this paragraph cold (3 attempts)

> "I don't claim AV perception expertise. Perception means the Driver's 'what do I see' stack. A DevAI agent would help *engineers* debug a sim miss: take scenario and timestamp, pull replay and ground-truth labels, diff what perception predicted versus truth, then suggest ranked hypotheses and similar past failures. Same outer-loop pattern as my GEICO Slack triage bot — tools, first-pass RCA, human in the loop. The agent never changes vehicle software."

| Attempt | Time | Filler? | Notes |
|---------|------|---------|-------|
| 1 | ___ s | Y / N | |
| 2 | ___ s | Y / N | |
| 3 | ___ s | Y / N | Target ≤ 50 s |

### Step 3 — One sentence in your words (close file 60 sec, then write)

_________________________________________________________________
_________________________________________________________________

---

## Block 2 — Four STAR scripts with Waymo frame (40 min)

For each: **read aloud once → close notes → deliver from memory → check time.**  
Target: **90–120 seconds** each.

### STAR A — Outer loop: Slack triage (Claude Agent SDK)

**Script (speak this):**

> "Situation: GEICO's package-mgmt Slack channel was a human triage queue — engineers waiting on AMP for first-pass answers.  
> Task: I built a Claude Agent SDK bot that classifies tickets and runs first-pass response.  
> Action: Wired MCP tools for JFrog/Slack/ADO, shipped agent skills `solve-case`, `close-case`, `build-kb`, and put Club MCP into amp-control-plane so it was production, not a demo.  
> Result: First-pass automation on the help channel; pattern now part of our DE AI Showcase for a 282-person org.  
> **Waymo frame:** This is the outer loop in your JD — automate triage and eng workflows. At Waymo I'd apply the same pattern to CI/sim regressions for AV engineers."

| Attempt | Time | Hit Waymo frame? |
|---------|------|------------------|
| 1 | | Y / N |
| 2 | | Y / N |

---

### STAR B — Inner loop: AI CI/CD migration engine + JFrog POC

**Script:**

> "Situation: GEICO evaluating JFrog SaaS cutover across many pipelines.  
> Task: I tech-led the POC and the migration path.  
> Action: Built workflows covering all 11 package types; load-tested 5,000 repos / 5,000 parallel artifacts; built an AI migration engine that opens per-team PRs to switch endpoints.  
> Result: Coverage validated; scale issues filed with JFrog; migration cost drops because PRs are generated, not hand-written.  
> **Waymo frame:** That's inner-loop acceleration — spec/inventory → generated change → tests → human merge. Same shape as helping Waymo engineers go from intent to verified code faster."

| Attempt | Time | Hit Waymo frame? |
|---------|------|------------------|
| 1 | | Y / N |
| 2 | | Y / N |

---

### STAR C — Adoption: Cursor × Claude Code MCP bridge

**Script:**

> "Situation: Claude Code pilot and Cursor both needed Slack MCP; dual auth was a security and DX problem.  
> Task: I authored the Cursor MCP × Slack BRD and built the bridge.  
> Action: Cursor cached token → user consent → short-lived derived token for Claude Code — never expose the raw store.  
> Result: Pilot users got one Slack auth across tools; security approved; pattern reusable for other MCP servers.  
> **Waymo frame:** Your JD calls out driving adoption of novel AI tools across teams. I've done that cross-tool adoption in a regulated enterprise, not a greenfield lab."

| Attempt | Time | Hit Waymo frame? |
|---------|------|------------------|
| 1 | | Y / N |
| 2 | | Y / N |

---

### STAR D — Reliability: Artifactory four-nines

**Script:**

> "Situation: Artifactory was ~1 major incident a month — critical path for every container and model artifact.  
> Task: As staff-IC lead I owned the reliability outcome.  
> Action: Ranked incident classes by outage minutes; fixed the dominant Azure Firewall TLS class first; wrote AI-consumable runbooks and MCP skills so on-call wasn't hero-dependent; authored NOCIM-11695 CoE after an Entra outage.  
> Result: Sustained 99.99% availability.  
> **Waymo frame:** DevAI tools will sit on the critical path for 1,000+ AV engineers. I bring reliability ownership for developer platforms that can't go down."

| Attempt | Time | Hit Waymo frame? |
|---------|------|------------------|
| 1 | | Y / N |
| 2 | | Y / N |

---

## Block 3 — Inner / Outer loop flashcards (10 min)

Cover the right column. Say the left term, then uncover.

| Term | Your answer (memorize) |
|------|------------------------|
| **Inner loop** | Spec → code → test → iterate faster for one engineer (my CI/CD migration PR engine + Claude Code AMP plugin) |
| **Outer loop** | Automate org workflows: triage, RCA, multi-step eng tasks (my Slack triage bot + MCP skills) |
| **Perception debug** | Tools for engineers to RCA *sim* perception misses — not me training the model |
| **Your one-liner** | "I accelerate the humans building the Driver." |

**Drill:** 60-second cold dump — say all four without looking. ☐ Pass ☐ Fail (retry once)

---

## Block 4 — Hands-on LC (30 min) — do this in an editor

**Problem:** Group Anagrams (LC 49)  
**Pattern:** hash map — read [coding-patterns.md §1](coding-patterns.md) if stuck (2 min max).

### Starter — fill the blanks, then run against the tests

```python
from collections import defaultdict
from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)
    for s in strs:
        # TODO: key that is identical for anagrams, different otherwise
        key = ______________________________
        groups[key].append(s)
    return list(groups.values())

# Tests — must print True True True
assert sorted(map(sorted, groupAnagrams(["eat","tea","tan","ate","nat","bat"]))) == sorted(
    map(sorted, [["bat"],["nat","tan"],["ate","eat","tea"]])
)
assert groupAnagrams([""]) == [[""]]
assert groupAnagrams(["a"]) == [["a"]]
print("PASS")
```

**Answer key (only after you try 20 min):**  
`key = tuple(sorted(s))`  
or `key = tuple(counts)` where `counts` is length-26 letter frequencies.

**Log one line in [coding-log.md](../coding-log.md):**

```
2026-07-16 · LC 49 Group Anagrams · hash · ________________
```

---

## Block 5 — Gate 1 cold pass test (4 min) — end of session

Phone timer. **No notes.** Deliver in order:

1. Spec-driven (90s) — if you don't have a script yet, use this temporary one:

> "For me spec-driven means a machine-checkable contract before code. At GEICO: AI-consumable ADRs for artifact auth, the JFrog package-type matrix as the POC spec with automated pass/fail, and the Claude Code plugin BRD as the contract for implementation. Spec first, then agents and humans implement against it."

2. Why Waymo DevAI (90s):

> "DevAI builds the platform that lets AV engineers ship faster — same problem I've attacked at GEICO: inner loop with AI CI/CD PRs and Claude Code, outer loop with Slack triage and MCP skills. I want the harder domain: sim RCA and perception debug where tooling quality hits safety-critical engineering. Spec-driven + multi-agent outer loops can compress weeks to hours, and Waymo is the place to prove it."

3. Inner loop (30s) + Outer loop (30s) — from Block 3.

| Total time | Pass if ≤ 4:00 and no freeze > 5s |
|------------|-----------------------------------|
| ___ : ___ | ☐ Pass ☐ Fail — retry tomorrow AM |

---

## Done checklist (check before you stop)

- [ ] Perception paragraph spoken 3×  
- [ ] STAR A–D each spoken ≥2× with Waymo frame  
- [ ] Inner/outer flashcards cold  
- [ ] LC 49 coded + logged  
- [ ] 4-min Gate 1 pass test timed  

**Tomorrow (Fri):** Apply Req 4857 + finalize referrer packet — not more invention of pitches if tonight's Pass is checked.
