# Figure AI Application Package — Ming Jia

Tailored resumes and cover letters for 5 Figure roles (May 2026 apply wave).

## Status (`application-results.json`)

| Role | Result |
|------|--------|
| Developer Tools and Productivity | Submitted |
| Staff Site Reliability Engineer | Submitted |
| Helix AI Engineer, Agentic Systems | Failed (browser closed mid-run) |
| Helix AI Engineer, Training Infrastructure | Failed |
| Helix AI Engineer, Data Infrastructure | Failed |

Re-apply Helix roles manually or with `apply_figure.py` if still open. Use current resumes from repo root (`resume-ai-infra.md` / `Mingresume-ai-infra.docx`) rather than the May `resume.txt` snapshots if content has drifted.

## Per-role folders

Each of `01`–`05` contains `resume.txt` + `cover-letter.txt` (historical May packages).

## Applicant info

- **Name:** Ming Jia · **Email:** mailming@gmail.com · **Phone:** (626) 354-7866
- **LinkedIn:** https://www.linkedin.com/in/mailming
- **GitHub / Jiadroid:** https://github.com/mailming · https://github.com/mailming/jiadroid

## Semi-automated apply

```bash
python figure-applications/apply_figure.py --wait=600 --keep-open
# or: --retry-failed
```

Greenhouse may require an 8-character email security code; enter it when the form prompts.
