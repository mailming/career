# Career site — Ming Jia

Public-facing career materials. **Last refreshed: 2026-10-19** (covers GEICO + personal work since June 2025, with a deep pass on Jun–Oct 2026).

## Apply with these

| Asset | File | Use |
|-------|------|-----|
| **Default resume (AI infra)** | [resume-ai-Infra](resume-ai-infra.md) → `Mingresume-ai-infra.docx` | Anthropic, Cursor, Modal, Databricks, Figure agent/platform |
| **Platform / SRE resume** | [resume.md](resume.md) → `Mingresume.docx` | Broad Staff platform / AMP narrative |
| **Release platform resume** | [resume-release-platform.md](resume-release-platform.md) → `Mingresume-release-platform.docx` | Classic DevOps / release platform roles |
| **One-pager** | [portfolio/one-pager.md](portfolio/one-pager.md) | Attach to referrals + thank-yous |
| **LinkedIn copy** | [linkedin-rewrite.md](linkedin-rewrite.md) | Headline / About / Featured — paste to profile |

## Evidence & direction

| Asset | File |
|-------|------|
| Work evidence (source of truth) | [portfolio/work-evidence.md](portfolio/work-evidence.md) |
| Jiadroid career map | [portfolio/jiadroid.md](portfolio/jiadroid.md) |
| 5-year north star | [CAREER-GOAL-5-YEARS.md](CAREER-GOAL-5-YEARS.md) |
| Weekly OS | [WEEKLY-OPERATING-SYSTEM.md](WEEKLY-OPERATING-SYSTEM.md) |
| Target companies | [target-companies.md](target-companies.md) |

## Jun–Oct 2026 headline wins (on resume)

1. **Load Healer Reactive** — OUTAGE → HTTP 429 on Artifactory NP + PD2  
2. **Martech-off cutover program** — channels + MAP/CDP/Billing/Payments kickoffs; `amp-migrate`  
3. **CoEs** — NOCIM-13154, NOCIM-13213 (+ earlier 11695, 12455)  
4. **Artifactory 7.161.15** upgrade  
5. **Jiadroid** — ESP32-S3, USB-C/OTA, Follow Me, multi-body sims  

## Rebuild Word docs

```bash
python3 build_resume_docx.py -i resume.md -o Mingresume.docx
python3 build_resume_docx.py -i resume-ai-infra.md -o Mingresume-ai-infra.docx
python3 build_resume_docx.py -i resume-release-platform.md -o Mingresume-release-platform.docx
```
