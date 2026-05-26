from playwright.sync_api import sync_playwright

STRATEGIES = [
    "option_exact",
    "type_enter",
    "arrow_enter",
]

def try_strategy(page, name):
    page.reload(wait_until="networkidle")
    page.wait_for_timeout(500)
    print(f"\n--- {name} ---")
    country = page.locator("#country")

    if name == "option_exact":
        country.click(force=True)
        page.get_by_role("option", name="United States +1").click()
    elif name == "type_enter":
        country.click(force=True)
        page.keyboard.type("United States")
        page.wait_for_timeout(300)
        page.keyboard.press("Enter")
    elif name == "arrow_enter":
        country.click(force=True)
        page.keyboard.press("ArrowDown")
        page.keyboard.press("Enter")

    page.wait_for_timeout(800)
    sv = page.locator(".select__single-value").first
    sv_text = sv.inner_text() if sv.count() else "NONE"
    print("single-value:", sv_text)
    print("input val:", repr(country.input_value()))
    invalid = page.locator("#country[aria-invalid='true']").count()
    print("country invalid:", invalid)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://job-boards.greenhouse.io/figureai/jobs/4662042006", wait_until="networkidle")
    for s in STRATEGIES:
        try_strategy(page, s)
    browser.close()
