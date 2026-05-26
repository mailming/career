# Finish the remaining 4 Figure applications

## Current state (2026-05-25)

| Job ID | Role | Status |
|--------|------|--------|
| 4614747006 | Staff Site Reliability Engineer | **submitted (confirmed)** |
| 4662042006 | Senior/Staff Software Engineer, Developer Tools and Productivity | needs retry |
| 4659175006 | Helix AI Engineer, Agentic Systems | needs retry (includes cover letter) |
| 4431092006 | Helix AI Engineer, Training Infrastructure | needs retry |
| 4345915006 | Helix AI Engineer, Data Infrastructure | needs retry |

## The blocker

Greenhouse sends an **8-character security code** to `mailming@gmail.com` when the form loads. Submit stays greyed out until all 8 characters are entered. The script `apply_figure.py` now:

- Auto-fills every field (incl. `Mingresume.docx` upload + Country + LinkedIn + Website + cover letter where applicable)
- Polls the security-code inputs and the Submit button state
- Waits up to 10 minutes per job plus an additional 10-minute grace until the code is entered
- Confirms the `/confirmation` thank-you page before recording a submission

The only thing it cannot do is read your Gmail.

## How to finish (single command)

Open a **Cursor terminal** (or PowerShell) so the visible Chrome window stays in front of you, then run:

```powershell
$env:PYTHONUNBUFFERED=1
python c:\Users\USER\Workspace\career\figure-applications\apply_figure.py --retry-failed --wait=600 --keep-open
```

- `--retry-failed` skips the Staff SRE that's already submitted.
- `--wait=600` gives you 10 minutes per job to read Gmail and type the code.
- `--keep-open` leaves Chrome up for 5 minutes after the last submission for verification.

## For each of the 4 jobs

1. Wait for the script to pre-fill and print `READY TO SUBMIT: <role>`.
2. Open `mail.google.com` and grab the 8-char "Figure / Greenhouse" code (subject usually starts with "Verify").
3. Type all 8 characters into the boxes in Chrome.
4. The script polls every 30 seconds — once Submit is enabled, it auto-clicks and records the result.
5. Move on to the next job's pause.

## After the run

The script writes the merged result to `application-results.json`. Each role should show:

```json
{
  "job_id": "...",
  "success": true,
  "final_url": "https://job-boards.greenhouse.io/figureai/jobs/.../confirmation"
}
```

If any still fail, screenshot `result-<job_id>.png` in this folder and check whether the security-code panel even appeared (sometimes Greenhouse skips it on retry after you've recently verified). In that case set `--wait=120` to move faster.

## Backup plan

If the script blows up on a single job, finish that one manually using the corresponding folder:

- `01-devtools-productivity/resume.txt` + `cover-letter.txt`
- `03-agentic-systems/resume.txt` + `cover-letter.txt`
- `04-training-infrastructure/resume.txt` + `cover-letter.txt`
- `05-data-infrastructure/resume.txt` + `cover-letter.txt`

Resume to attach: `c:\Users\USER\Workspace\career\Mingresume.docx`.

Form values:

- First name: Ming · Last name: Jia
- Email: mailming@gmail.com · Phone: (626) 354-7866 · Country: United States
- LinkedIn: https://www.linkedin.com/in/mailming
- Website: https://github.com/mailming (use https://smarttuna.ai for the Agentic Systems role)
