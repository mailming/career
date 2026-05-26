# Figure AI Application Package — Ming Jia

Tailored resumes and cover letters for 5 recommended Figure roles.

## Application Links

| # | Role | Greenhouse URL |
|---|------|----------------|
| 1 | Senior/Staff Software Engineer, Developer Tools and Productivity | https://job-boards.greenhouse.io/figureai/jobs/4662042006 |
| 2 | Staff Site Reliability Engineer | https://job-boards.greenhouse.io/figureai/jobs/4614747006 |
| 3 | Helix AI Engineer, Agentic Systems | https://job-boards.greenhouse.io/figureai/jobs/4659175006 |
| 4 | Helix AI Engineer, Training Infrastructure | https://job-boards.greenhouse.io/figureai/jobs/4431092006 |
| 5 | Helix AI Engineer, Data Infrastructure | https://job-boards.greenhouse.io/figureai/jobs/4345915006 |

## Files Per Role

Each folder contains:
- `resume.txt` — role-tailored resume (paste via "Enter manually" or upload as .txt)
- `cover-letter.txt` — role-tailored cover letter

## Applicant Info (use for all forms)

- **Name:** Ming Jia
- **Email:** mailming@gmail.com
- **Phone:** (626) 354-7866
- **Country:** United States
- **LinkedIn:** https://www.linkedin.com/in/mailming
- **Website:** https://github.com/mailming (use https://smarttuna.ai for Agentic Systems role)

## Semi-Automated Apply (recommended)

Greenhouse may require **reCAPTCHA** and/or an **email security code** sent to `mailming@gmail.com`. This environment cannot read your Gmail inbox, so verification is a manual step.

Run from a terminal (opens a visible browser):

```powershell
python c:\Users\USER\Workspace\career\figure-applications\apply_figure.py --wait=600 --keep-open
```

- Attaches **`Mingresume.docx`** as resume (falls back to role `resume.txt` if upload fails)
- Default wait is **10 minutes** per job (`--wait=600`)
- Use `--interactive` to press Enter yourself when ready (best if running in your own terminal)
- Use `--keep-open` to leave the browser open 5 extra minutes at the end

Screenshots are saved as `prefill-<job_id>.png` and `result-<job_id>.png`.

## Manual Apply Steps

1. Open the Greenhouse link for the role
2. Fill: First Name, Last Name, Email, **Country (required — select United States)**, Phone
3. Resume: click **Enter manually** → paste contents of `resume.txt`
4. Cover letter: paste `cover-letter.txt` if the form has a Cover Letter field (Agentic Systems does)
5. LinkedIn + Website as above
6. Complete CAPTCHA / email verification from Gmail, then Submit

## Tailoring Summary

| Role | Resume emphasis |
|------|-------------------|
| DevTools & Productivity | Jenkins HA, CI/CD migration engine, GitHub Actions, developer tooling |
| Staff SRE | 99.99% SLO, incident response, SaaS migration, runbooks, Terraform |
| Agentic Systems | OpenClaw, SmartTuna, Claude Agent SDK, MCP, LangGraph |
| Training Infrastructure | Large-scale infra, JFrog load test, K8s, EMR clusters, ML platform CI |
| Data Infrastructure | Artifact data platform, pipeline stages, Hadoop/MongoDB, storage at scale |
