"""Dump Greenhouse form structure for debugging."""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://job-boards.greenhouse.io/figureai/jobs/4662042006", wait_until="networkidle", timeout=60000)

    # Country
    page.locator("#country").click(force=True)
    page.wait_for_timeout(500)
    options = page.get_by_role("option").all_text_contents()
    print("OPTIONS (first 10):", options[:10])
    page.get_by_role("option", name="United States").first.click()
    page.wait_for_timeout(500)
    print("country after select:", page.locator("#country").input_value())

    # Resume section
    print("\n--- Resume section ---")
    for sel in [
        'input[type="file"]',
        'button:has-text("Enter manually")',
        'textarea',
        '[data-testid*="resume"]',
        '.application--questions',
    ]:
        n = page.locator(sel).count()
        print(f"{sel}: {n}")

    btns = page.locator("button").all_text_contents()
    print("buttons:", [b.strip() for b in btns if b.strip()][:15])

    page.get_by_role("button", name="Enter manually").click()
    page.wait_for_timeout(1000)
    print("textareas after click:", page.locator("textarea").count())
    for i in range(page.locator("textarea").count()):
        ta = page.locator("textarea").nth(i)
        print(f"  ta[{i}] name={ta.get_attribute('name')} id={ta.get_attribute('id')}")

    # LinkedIn / Website
    inputs = page.locator("input").all()
    print("\n--- Custom inputs ---")
    for inp in inputs:
        label = inp.get_attribute("aria-label") or inp.get_attribute("name") or inp.get_attribute("id")
        if label and any(x in (label or "").lower() for x in ("linkedin", "website", "cover")):
            print(f"  {label}")

    browser.close()
