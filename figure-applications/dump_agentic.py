from pathlib import Path
from playwright.sync_api import sync_playwright

BASE = Path(__file__).parent
resume = BASE / "03-agentic-systems" / "resume.txt"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://job-boards.greenhouse.io/figureai/jobs/4659175006", wait_until="networkidle")

    # simulate file upload path (like apply script)
    page.locator('input[type="file"]').first.set_input_files(str(resume))
    page.wait_for_timeout(1000)

    enter = page.get_by_role("button", name="Enter manually")
    print("enter manually count after file resume:", enter.count())

    if enter.count() >= 1:
        enter.last.click()
        page.wait_for_timeout(800)
    print("cover_letter_text count:", page.locator("#cover_letter_text").count())
    browser.close()
