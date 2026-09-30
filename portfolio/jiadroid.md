# Jiadroid — career mapping

**Repo:** [github.com/mailming/jiadroid](https://github.com/mailming/jiadroid) · local: `~/Workspace/jiadroid`  
**Role in Outcome A:** Primary **Physical AI / embodied agent platform** portfolio artifact (2026–2027).  
**North star docs:** [CAREER-GOAL-5-YEARS.md](../CAREER-GOAL-5-YEARS.md) · [WEEKLY-OPERATING-SYSTEM.md](../WEEKLY-OPERATING-SYSTEM.md)

---

## One-line thesis

Phone = brain / eyes / ears / internet; robot = body; **Jiadroid protocol** = the USB-style contract between them — discovery, commands, telemetry, and safety (estop).

---

## What exists (as of 2026-09-30)

| Layer | Status |
|-------|--------|
| Protocol 0.1 (JSON newline, session, devices, walk.velocity, stop/estop) | Spec + Python |
| Open Duck Mini simulator + laptop Follow Me demo | Working |
| Android + iOS Follow Me (person / printed marker / QR), eyes UI, voice listen/reply | Working |
| Phone → laptop sim over Wi-Fi | Working |
| ESP32 firmware + real Open Duck Mini | Not yet |
| Bluetooth / USB transports | Spec only (TCP implemented) |
| Second body (vacuum / dog) | Not yet |

---

## Interview / Figure / Waymo pitch (90 sec)

> Most affordable robots are remote-controlled because cameras, compute, and connectivity are expensive to put in every body. Jiadroid treats the phone people already own as that stack, and defines a small open protocol so any body can announce its devices and accept walk commands with hard safety — stop and latched estop. I shipped Follow Me on Android and iOS against an Open Duck Mini simulator: the phone decides where to go; the body keeps its own gait/reflexes. Same pattern as production robotics platforms — perception and policy off-board or on a privileged brain, actuators behind a contract. Next milestone is ESP32 on a real duck so the phone replaces the game controller.

**Do not say:** "I built a robot toy."  
**Do say:** "I built a **multi-body agent/control plane** with a safety-aware device contract."

---

## Maps to Outcome A lanes

| Lane | How Jiadroid proves it |
|------|------------------------|
| A1 Embodied agent platform | Follow Me = closed-loop perception → decision → actuator command; apps as behaviors |
| A2 Simulation | Duck sim + protocol parity with production path (train later if needed) |
| A3 Fleet / reliability | Safety state machine; estop latch; "body introduces itself" → fleet onboarding pattern |

---

## Near-term milestones (career-visible)

1. **Public:** short demo video (phone Follow Me → sim) + pin on LinkedIn Featured.
2. **Hardware:** ESP32 speaking protocol 0.1 + real Open Duck Mini walk path.
3. **Multi-body proof:** second body type (even a wheeled stub) accepting the same `walk.velocity`.
4. **Optional capstone:** multi-body eval harness or Isaac only if GRAD 58900 needs a sim-heavy project.

---

## Resume / one-pager bullets (draft)

- Founded **Jiadroid** — open phone-to-robot protocol (discovery, walk commands, estop) so a phone can act as brain/eyes for Open Duck Mini and other bodies.
- Shipped **Follow Me** on Android and iOS (camera person/marker tracking, voice I/O) driving a protocol-compatible duck simulator over Wi-Fi.
- Designed safety into the control plane: `robot.stop`, latched `safety.estop`, and blocked motion until clear.

---

## Time budget

Wed 45–60 min + Sat 2 hrs deep work (see weekly OS). Applications and LC still win if interview week is live; do not starve Jiadroid for two consecutive weeks unless screens are booked.
