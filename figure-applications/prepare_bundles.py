"""Apply to Figure Greenhouse jobs via browser CDP file upload + form fill helpers."""
import json
from pathlib import Path

BASE = Path(__file__).parent
JOBS = [
    ("01-devtools-productivity", "4662042006", False),
    ("02-staff-sre", "4614747006", False),
    ("03-agentic-systems", "4659175006", True),
    ("04-training-infrastructure", "4431092006", False),
    ("05-data-infrastructure", "4345915006", False),
]

APPLICANT = {
    "first": "Ming",
    "last": "Jia",
    "email": "mailming@gmail.com",
    "phone": "6263547866",
    "website": "https://github.com/mailming",
}

for folder, job_id, has_cover in JOBS:
    d = BASE / folder
    resume = (d / "resume.txt").read_text(encoding="utf-8")
  cover = (d / "cover-letter.txt").read_text(encoding="utf-8") if has_cover else ""
    combined = resume
    if not has_cover:
        # prepend short note in resume manual field isn't ideal))
        pass
    (d / "application-bundle.txt").write_text(
        resume + ("\n\n--- COVER LETTER ---\n\n" + cover if cover and not has_cover else ""),
        encoding="utf-8",
    )
    print(f"Prepared {folder} -> job {job_id}")

print(json.dumps(APPLICANT))
