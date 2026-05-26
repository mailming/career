"""Submit Figure AI Greenhouse applications with tailored materials.

Semi-automated: fills all fields, then pauses for you to complete
reCAPTCHA / email verification codes from Gmail before each submit.
"""
from pathlib import Path
import json
import sys
import time

from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout

BASE = Path(__file__).parent
RESUME_DOCX = BASE.parent / "Mingresume.docx"
APPLICANT = {
    "first": "Ming",
    "last": "Jia",
    "email": "mailming@gmail.com",
    "phone": "6263547866",
    "linkedin": "https://www.linkedin.com/in/mailming",
    "website_default": "https://github.com/mailming",
}

JOBS = [
    {
        "id": "4662042006",
        "folder": "01-devtools-productivity",
        "title": "Senior/Staff Software Engineer, Developer Tools and Productivity",
        "website": "https://github.com/mailming",
    },
    {
        "id": "4614747006",
        "folder": "02-staff-sre",
        "title": "Staff Site Reliability Engineer",
        "website": "https://github.com/mailming",
    },
    {
        "id": "4659175006",
        "folder": "03-agentic-systems",
        "title": "Helix AI Engineer, Agentic Systems",
        "website": "https://smarttuna.ai",
        "has_cover_letter": True,
    },
    {
        "id": "4431092006",
        "folder": "04-training-infrastructure",
        "title": "Helix AI Engineer, Training Infrastructure",
        "website": "https://github.com/mailming",
    },
    {
        "id": "4345915006",
        "folder": "05-data-infrastructure",
        "title": "Helix AI Engineer, Data Infrastructure",
        "website": "https://github.com/mailming",
    },
]


def fill_country(page):
    page.locator("#country").click(force=True)
    page.wait_for_timeout(300)
    page.get_by_role("option", name="United States +1").click()
    page.wait_for_timeout(500)


def fill_resume(page, resume_docx: Path, resume_txt: Path):
    file_input = page.locator('input[type="file"]').first
    if resume_docx.exists() and file_input.count() > 0:
        file_input.set_input_files(str(resume_docx))
        page.wait_for_timeout(2000)
        if page.locator("text=Mingresume.docx").count() > 0:
            print(f"  Resume attached: {resume_docx.name}")
            return
        # Some Greenhouse themes hide filename; treat upload as success if no manual prompt needed
        if page.locator("#resume_text").count() == 0:
            print(f"  Resume attached: {resume_docx.name}")
            return

    if not resume_txt.exists():
        raise FileNotFoundError(f"No resume found: {resume_docx} or {resume_txt}")

    enter_btn = page.get_by_role("button", name="Enter manually").first
    enter_btn.click()
    page.wait_for_timeout(800)
    page.locator("#resume_text").fill(resume_txt.read_text(encoding="utf-8"))
    print(f"  Resume pasted manually from {resume_txt.name}")


def fill_cover_letter(page, cover_path: Path):
    enter = page.get_by_role("button", name="Enter manually")
    if enter.count() >= 2:
        enter.nth(1).click()
    elif enter.count() == 1:
        enter.first.click()
    page.wait_for_timeout(800)
    page.locator("#cover_letter_text").fill(cover_path.read_text(encoding="utf-8"))


def collect_validation_errors(page) -> list[str]:
    errors = []
    invalid = page.locator("[aria-invalid='true']")
    for i in range(invalid.count()):
        el = invalid.nth(i)
        label = (
            el.get_attribute("aria-label")
            or el.get_attribute("id")
            or el.get_attribute("name")
            or "unknown field"
        )
        errors.append(label)
    for text in page.locator(".field-error, .error-message").all_text_contents():
        text = text.strip()
        if text:
            errors.append(text)
    return errors


def parse_wait_seconds() -> int:
    for arg in sys.argv:
        if arg.startswith("--wait="):
            return int(arg.split("=", 1)[1])
    return 600


def security_code_length(page) -> int:
    inputs = page.locator("input[maxlength='1']")
    count = inputs.count()
    if count == 0:
        return 0
    chars = min(count, 8)
    code = "".join(inputs.nth(i).input_value() for i in range(chars))
    return len(code.strip())


def submit_ready(page) -> bool:
    submit = page.get_by_role("button", name="Submit application")
    if submit.count() == 0:
        return False
    try:
        return submit.is_enabled()
    except Exception:
        return False


def wait_for_confirmation(page, timeout_s: int = 45) -> bool:
    for _ in range(timeout_s):
        if "/confirmation" in page.url:
            return True
        body = page.content().lower()
        if any(s in body for s in ("thank you for applying", "application has been received")):
            return True
        page.wait_for_timeout(1000)
    return False


def wait_for_manual_verification(page, job_title: str, wait_seconds: int, interactive: bool):
    print(f"\n{'=' * 60}")
    print(f"READY TO SUBMIT: {job_title}")
    print("In the browser window:")
    print("  1. Check Gmail (mailming@gmail.com) for the 8-character security code")
    print("  2. Enter all 8 characters in the form (Submit stays greyed out until done)")
    print("  3. Complete reCAPTCHA if shown")
    if interactive:
        print("  4. Press Enter in this terminal when the code is entered")
        print(f"{'=' * 60}")
        input(">>> Press Enter to submit (or Ctrl+C to skip this job)... ")
        return

    print(f"  4. Waiting up to {wait_seconds}s ({wait_seconds // 60} min), then until code is entered")
    print(f"{'=' * 60}")
    tick = 30 if wait_seconds >= 120 else 15
    elapsed = 0
    while elapsed < wait_seconds:
        code_len = security_code_length(page)
        ready = submit_ready(page)
        print(f"  ... {wait_seconds - elapsed}s left | security code: {code_len}/8 | submit enabled: {ready}")
        if ready and code_len >= 8:
            print("  Security code complete — submitting early.")
            return
        time.sleep(min(tick, wait_seconds - elapsed))
        elapsed += tick

    extra = 600
    while extra > 0 and not submit_ready(page):
        code_len = security_code_length(page)
        print(f"  Still waiting for 8-char Gmail code ({code_len}/8)... {extra}s left")
        time.sleep(30)
        extra -= 30


def apply_job(page, job: dict, wait_seconds: int) -> dict:
    url = f"https://job-boards.greenhouse.io/figureai/jobs/{job['id']}"
    folder = BASE / job["folder"]
    resume_txt = folder / "resume.txt"
    cover_txt = folder / "cover-letter.txt"

    print(f"\n=== Applying: {job['title']} ===")
    page.goto(url, wait_until="networkidle", timeout=60000)

    page.locator("#first_name").fill(APPLICANT["first"])
    page.locator("#last_name").fill(APPLICANT["last"])
    page.locator("#email").fill(APPLICANT["email"])
    fill_country(page)
    page.locator("#phone").fill(APPLICANT["phone"])
    fill_resume(page, RESUME_DOCX, resume_txt)

    if job.get("has_cover_letter") and cover_txt.exists():
        fill_cover_letter(page, cover_txt)

    linkedin = page.locator('input[aria-label="LinkedIn Profile"]')
    if linkedin.count():
        linkedin.fill(APPLICANT["linkedin"])

    website = page.locator('input[aria-label="Website"]')
    if website.count():
        website.fill(job.get("website", APPLICANT["website_default"]))

    pre_errors = collect_validation_errors(page)
    country_display = page.locator(".select__single-value").first.inner_text() if page.locator(".select__single-value").count() else ""
    screenshot = BASE / f"prefill-{job['id']}.png"
    page.screenshot(path=str(screenshot), full_page=True)

    if pre_errors:
        print(f"  Pre-submit validation issues: {pre_errors}")
    print(f"  Country display: {country_display!r}")
    print(f"  Screenshot: {screenshot}")

    submit = page.get_by_role("button", name="Submit application")
    submit.scroll_into_view_if_needed()
    wait_for_manual_verification(page, job["title"], wait_seconds, interactive="--interactive" in sys.argv)

    if submit_ready(page):
        submit.click()
    else:
        print("  WARNING: Submit still disabled — security code may be missing.")

    confirmed = wait_for_confirmation(page)
    page.screenshot(path=str(BASE / f"result-{job['id']}.png"), full_page=True)

    result = {
        "job_id": job["id"],
        "title": job["title"],
        "url": url,
        "success": confirmed,
        "final_url": page.url,
        "validation_errors": collect_validation_errors(page) or None,
    }
    print(json.dumps(result, indent=2))
    return result


def main():
    wait_seconds = parse_wait_seconds()
    headless = "--headless" in sys.argv
    keep_open = "--keep-open" in sys.argv
    job_filter = next((a.split("=", 1)[1] for a in sys.argv if a.startswith("--only=")), None)
    retry_failed = "--retry-failed" in sys.argv
    jobs = [j for j in JOBS if not job_filter or j["id"] == job_filter]

    prev_results = []
    results_path = BASE / "application-results.json"
    if retry_failed and results_path.exists():
        prev_results = json.loads(results_path.read_text(encoding="utf-8"))
        ok_ids = {r["job_id"] for r in prev_results if r.get("success")}
        jobs = [j for j in jobs if j["id"] not in ok_ids]
        print(f"Retrying {len(jobs)} failed job(s); skipping {len(ok_ids)} already submitted.")

    if not RESUME_DOCX.exists():
        print(f"WARNING: {RESUME_DOCX} not found — will fall back to resume.txt")

    results = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless, slow_mo=150)
        context = browser.new_context()
        page = context.new_page()
        for job in jobs:
            try:
                results.append(apply_job(page, job, wait_seconds))
            except PWTimeout as e:
                results.append(
                    {"job_id": job["id"], "title": job["title"], "success": False, "error": str(e)}
                )
            except KeyboardInterrupt:
                results.append(
                    {"job_id": job["id"], "title": job["title"], "success": False, "error": "skipped by user"}
                )
                print("Skipped remaining jobs.")
                break
            except Exception as e:
                results.append(
                    {"job_id": job["id"], "title": job["title"], "success": False, "error": str(e)}
                )
            time.sleep(5)
        if keep_open:
            print("\nBrowser staying open for 5 minutes — close it manually when done.")
            time.sleep(300)
        browser.close()

    out = BASE / "application-results.json"
    if retry_failed and prev_results:
        merged = {r["job_id"]: r for r in prev_results}
        for r in results:
            merged[r["job_id"]] = r
        final = [merged[j["id"]] for j in JOBS if j["id"] in merged]
        out.write_text(json.dumps(final, indent=2), encoding="utf-8")
    else:
        out.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(f"\nResults saved to {out}")
    ok = sum(1 for r in results if r.get("success"))
    print(f"Submitted successfully: {ok}/{len(results)}")


if __name__ == "__main__":
    main()
