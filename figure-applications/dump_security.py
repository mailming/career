from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://job-boards.greenhouse.io/figureai/jobs/4662042006", wait_until="networkidle")
    # trigger security code by filling email maybe on submit - just inspect page
    for sel in ["input[name*='security']", "input[name*='verification']", "input[maxlength='1']", "[data-testid*='security']"]:
        n = page.locator(sel).count()
        if n:
            print(sel, n)
            for i in range(min(n, 3)):
                el = page.locator(sel).nth(i)
                print(" ", el.get_attribute("name"), el.get_attribute("id"), el.get_attribute("aria-label"))
    browser.close()
