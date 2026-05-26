"""Test fixed selectors."""
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE = Path(__file__).parent
resume = (BASE / "01-devtools-productivity" / "resume.txt").read_text(encoding="utf-8")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://job-boards.greenhouse.io/figureai/jobs/4662042006", wait_until="networkidle")

    page.locator("#first_name").fill("Ming")
    page.locator("#last_name").fill("Jia")
    page.locator("#email").fill("mailming@gmail.com")

    page.locator("#country").click(force=True)
    page.get_by_role("option", name="United States +1").click()
    page.wait_for_timeout(500)

    page.locator("#phone").fill("6263547866")
    page.get_by_role("button", name="Enter manually").click()
    page.wait_for_timeout(800)
    page.locator("#resume_text").fill(resume)

    page.locator('input[aria-label="LinkedIn Profile"]').fill("https://www.linkedin.com/in/mailming")
    page.locator('input[aria-label="Website"]').fill("https://github.com/mailming")

    print("resume len:", len(page.locator("#resume_text").input_value()))
    print("country val:", repr(page.locator("#country").input_value()))
    # Check selected country display
    country_display = page.locator("#country").inner_text() if page.locator("#country").count() else ""
    print("country text:", repr(country_display[:50] if country_display else ""))

    invalid = page.locator("[aria-invalid='true']")
    for i in range(invalid.count()):
        el = invalid.nth(i)
        print("invalid:", el.get_attribute("aria-label") or el.get_attribute("id"))

    browser.close()
