"""Inspect Greenhouse form validation without submitting."""
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE = Path(__file__).parent


def inspect(job_id, folder):
    resume = BASE / folder / "resume.txt"
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"https://job-boards.greenhouse.io/figureai/jobs/{job_id}", wait_until="networkidle")

        page.locator("#first_name").fill("Ming")
        page.locator("#last_name").fill("Jia")
        page.locator("#email").fill("mailming@gmail.com")

        page.locator("#country").click(force=True)
        page.keyboard.type("United")
        page.wait_for_timeout(400)
        page.get_by_role("option", name="United States").first.click()
        page.wait_for_timeout(400)

        page.locator("#phone").fill("6263547866")
        page.get_by_role("button", name="Enter manually").click()
        page.locator('textarea[name="resume_text"]').fill(resume.read_text(encoding="utf-8"))

        for label in ("LinkedIn Profile", "Website"):
            loc = page.locator(f'input[aria-label="{label}"]')
            if loc.count():
                val = "https://www.linkedin.com/in/mailming" if "LinkedIn" in label else "https://github.com/mailming"
                loc.fill(val)

        if folder == "03-agentic-systems":
            cover = BASE / folder / "cover-letter.txt"
            manual_btns = page.get_by_role("button", name="Enter manually")
            if manual_btns.count() >= 2:
                manual_btns.nth(1).click()
                textareas = page.locator("textarea")
                if textareas.count() >= 2:
                    textareas.nth(1).fill(cover.read_text(encoding="utf-8"))

        country = page.locator("#country").input_value()
        captcha = page.locator('iframe[title*="reCAPTCHA"], iframe[src*="recaptcha"]').count()
        invalid = page.locator("[aria-invalid='true']")
        errors = page.locator(".field-error, .error-message, [class*='error']").all_text_contents()

        print(f"\n=== {job_id} / {folder} ===")
        print("country:", repr(country))
        print("recaptcha iframes:", captcha)
        print("invalid count:", invalid.count())
        for i in range(invalid.count()):
            el = invalid.nth(i)
            print(" invalid:", el.get_attribute("aria-label") or el.get_attribute("id") or el.get_attribute("name"))
        print("error texts:", [e.strip() for e in errors if e.strip()][:8])

        page.get_by_role("button", name="Submit application").click()
        page.wait_for_timeout(3000)
        body = page.inner_text("body").lower()
        print("after click url:", page.url)
        print("thank you:", "thank you" in body or "application submitted" in body)
        post_invalid = page.locator("[aria-invalid='true']").count()
        print("post-submit invalid:", post_invalid)
        post_errors = page.locator(".field-error, .error-message").all_text_contents()
        print("post-submit errors:", [e.strip() for e in post_errors if e.strip()][:8])
        browser.close()


if __name__ == "__main__":
    inspect("4662042006", "01-devtools-productivity")
    inspect("4659175006", "03-agentic-systems")
