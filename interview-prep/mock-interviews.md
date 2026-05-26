# Mock Interview Plan — 4 Sessions in Month 2

Goal: 2 system-design + 2 coding mocks in weeks 5-8 of the plan. Real interviewer voice + real time pressure. Cheap and fast.

## Booking sources

| Source | Cost | Notes |
|--------|------|-------|
| **interviewing.io** | $$ (free tier exists for senior) | Anonymous, senior interviewers from FAANG/AI labs. Best for design. |
| **Pramp** | Free | Peer-to-peer; pair up by topic. Good for coding. |
| **Hello Interview** | $$ | Strong on system design for senior+ roles. |
| **Peer from GEICO Claude pilot** | Free | One of the strongest sources — they're targeting similar roles. |
| **Purdue ECE 50874 classmate** | Free | Especially good for the OpenClaw deep-dive variant. |

Book all four within the first week of Month 2 so the dates are on the calendar — these slip otherwise.

## Schedule

| Week | Type | Source | Topic | Pre-work |
|------|------|--------|-------|----------|
| 5 | System design | interviewing.io | "Multi-tenant LLM inference serving" | Re-read `system-design/01-llm-inference-serving.md`; pick 2-3 weak spots to test |
| 6 | Coding | Pramp | LC-medium graphs / DP | Do 3 fresh problems beforehand to warm up |
| 7 | System design | Hello Interview or peer | "Agent orchestration platform" or "Vector DB at scale" | Re-read corresponding design doc |
| 8 | Coding | Pramp or peer | LC-medium + a tricky LC-hard | Solve 2 hards from coding log |

## Per-session protocol

### 24 hours before

- Sleep enough.
- Re-read the relevant design doc / coding-log pattern tracker.
- Refuse to learn anything new the day before.

### 30 minutes before

- Set up: webcam, mic, clean shared editor or whiteboard (Excalidraw is great).
- Glass of water nearby.
- `pyodide.org/repl` or your local Python set up so you don't fumble env.
- Phone in another room.

### During

- **First 5 min:** clarify requirements (design) or restate problem + edge cases (coding). Out loud.
- **Always narrate.** Silent thinking gets graded as not thinking.
- **Use the whiteboard / editor early.** Don't reason in your head past 2 minutes.
- **Ask for hints** if you're stuck past 5 min. Asking is graded better than spinning.
- **Run examples** in coding. Always.

### Immediately after (write while it's fresh)

Fill in this block at the end of the doc:

```
### YYYY-MM-DD · <type> · <topic> · <source>
- Score self 1-5
- What I did well: <2-3 bullets>
- What blew up: <2-3 bullets>
- Most useful interviewer feedback: <verbatim>
- 1 thing to change before next mock: <action>
- Update STAR / design / coding-log files? <which>
```

## Calibration check after all 4

After mock #4, write up a "where I am" page:

- Coding: comfortable patterns vs shaky ones
- Design: comfortable surfaces (inference, agents) vs shaky (training, GPU autoscaling — see Month-2 design extension)
- Behavioral: which STARs still feel awkward; need re-rehearsal

If self-score on design is consistently ≥ 4 and on coding is consistently ≥ 3.5, you're onsite-ready. If not, do 2 more mocks in Month 3 week 1 before the loops.

---

## Log

### YYYY-MM-DD · <type> · <topic> · <source>

- Score self 1-5:
- What I did well:
- What blew up:
- Most useful interviewer feedback:
- 1 thing to change before next mock:
- Updated files:

<!-- copy this block per session -->
