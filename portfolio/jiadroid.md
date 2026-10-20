# Jiadroid — career mapping

**Repo:** [github.com/mailming/jiadroid](https://github.com/mailming/jiadroid) · local: `~/Workspace/jiadroid`  
**Role in Outcome A:** Primary **Physical AI / embodied agent platform** portfolio artifact (2026–2027).  
**North star docs:** [CAREER-GOAL-5-YEARS.md](../CAREER-GOAL-5-YEARS.md) · [WEEKLY-OPERATING-SYSTEM.md](../WEEKLY-OPERATING-SYSTEM.md)  
**Last reviewed:** 2026-10-19

---

## One-line thesis

Phone = brain / eyes / ears / internet; robot = body; **Jiadroid protocol** = the USB-style contract between them — discovery, motion commands, telemetry, and safety (estop).

---

## What exists today (Oct 2026)

| Layer | Status |
|-------|--------|
| Protocol (JSON newline; session, devices, motion.velocity, stop/estop) | Spec + Python + mobile clients |
| Sims: kinematic Open Duck Mini, **2WD rover**, MuJoCo duck (+ train path) | Working |
| **ESP32-S3 firmware** for DIYables 2WD (L9110S + encoders) | Working — Wi-Fi on `main` |
| **USB-C serial + phone power + OTA flash** (Android OTG) | `feature/usb-c-link` |
| Save robot Wi-Fi to NVS from phone | Working |
| Android + iOS Follow Me (person / marker / QR), voice wake (“Vicky”), emotion eyes, manual pad | Working |
| Back-camera vision experiments (paper/screen) | In progress |

---

## Interview / Figure / Waymo pitch (90 sec)

> Most affordable robots are remote-controlled because cameras, compute, and connectivity are expensive to put in every body. Jiadroid treats the phone people already own as that stack, and defines a small open protocol so any body can announce its devices and accept motion commands with hard safety — stop and latched estop. I shipped Follow Me on Android and iOS, ESP32-S3 firmware for a real 2WD chassis with Wi-Fi and USB-C/OTA from the phone, and multi-body sims including a MuJoCo duck. Same pattern as production robotics platforms — perception and policy on a privileged brain, actuators behind a contract. Next milestone is docking a phone on Open Duck Mini so the phone replaces the game controller.

**Do not say:** "I built a robot toy."  
**Do say:** "I built a **multi-body agent/control plane** with a safety-aware device contract."

---

## Maps to Outcome A lanes

| Lane | How Jiadroid proves it |
|------|------------------------|
| A1 Embodied agent platform | Follow Me + voice = closed-loop perception → decision → actuator; apps as behaviors |
| A2 Simulation | Duck / rover / MuJoCo parity with production protocol path |
| A3 Fleet / reliability | Safety state machine; estop latch; body self-description → fleet onboarding pattern |

---

## Near-term milestones (career-visible)

1. **Public demo video** (phone Follow Me → real rover or sim) + LinkedIn Featured pin  
2. **Open Duck Mini dock** + ESP32 walk path replacing game controller  
3. **Multi-body proof** already started (rover + duck) — document second-body story in README  
4. Optional capstone: multi-body eval harness or Isaac if GRAD 58900 needs sim-heavy work  

---

## Resume / one-pager bullets (shipped)

- Founded **Jiadroid** — open phone-to-robot protocol (discovery, motion, estop) so a phone acts as brain/eyes for Open Duck Mini, a 2WD rover, and future bodies.
- Shipped **ESP32-S3 firmware** (Wi-Fi + USB-C serial/OTA) and **Follow Me** on Android/iOS with voice wake and emotion-driven eyes.
- Built multi-body sims (kinematic duck, rover, MuJoCo) behind one protocol client.

---

## Time budget

Wed 45–60 min + Sat 2 hrs deep work when stats/CNIT allow. Applications and LC still win during interview weeks.
