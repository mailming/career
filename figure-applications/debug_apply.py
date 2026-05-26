"""Debug a single Greenhouse application submission."""
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE = Path(__file__).parent
JOB_ID = "4662042006"
RESUME = BASE / "01-devtools-productivity" / "resume.txt"


def fill_country(page):
    page.locator("#country").click(force=True)
    page.wait_for_timeout(300)
    page.keyboard.type("United States")
    page.wait_for_timeout(300)
    page.get_by_role("option", name="United States").first.click()
    page.wait_for_timeout(500)


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=200)
        page = browser.new_page()
        page.goto(
            f"https://job-boards.greenhouse.io/figureai/jobs/{JOB_ID}",
            wait_until="networkidle",
            timeout=60000,
        )

        page.locator("#first_name").fill("Ming")
        page.locator("#last_name").fill("Jia")
        page.locator("#email").fill("mailming@gmail.com")
        fill_country(page)
        page.locator("#phone").fill("6263547866")

        page.get_by_role("button", name="Enter manually").click()
        page.locator('textarea[name="resume_text"]').fill(RESUME.read_text(encoding="utf-8"))

        linkedin = page.locator('input[aria-label="LinkedIn Profile"]')
        if linkedin.count():
            linkedin.fill("https://www.linkedin.com/in/mailming")

        website = page.locator('input[aria-label="Website"]')
        if website.count():
            website.fill("https://github.com/mailming")

        country_val = page.locator("#country").input_value()
        print("country value:", repr(country_val))

        invalid = page.locator("[aria-invalid='true']").all()
        print("invalid fields:", len(invalid))
        for el in invalid:
            label = el.get_attribute("aria-label") or el.get_attribute("name") or el.get_attribute("id")
            print("  -", label)

        page.screenshot(path=str(BASE / "debug-before-submit.png"), full_page=True)
        print("\n>>> Complete reCAPTCHA in the browser, then press Enter here...")
        input()

        page.get_by_role("button", name="Submit application").click()
        page.wait_for_timeout(8000)
        page.screenshot(path=str(BASE / "debug-after-submit.png"), full_page=True)
        print("final url:", page.url)
        body = page.inner_text("body")
        for phrase in ("thank you", "application submitted", "received your application", "required"):
            if phrase in body.lower():
                idx = body.lower().index(phrase)
                print("found:", phrase, "->", body[max(0, idx - 40) : idx + 80])

        browser.close()


if __name__ == "__main__":
    main()
