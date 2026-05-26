from pathlib import Path
from playwright.sync_api import sync_playwright

BASE = Path(__file__).parent
DOCX = BASE.parent / "Mingresume.docx"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://job-boards.greenhouse.io/figureai/jobs/4662042006", wait_until="networkidle")
    page.locator('input[type="file"]').first.set_input_files(str(DOCX))
    page.wait_for_timeout(2000)
    print("docx exists:", DOCX.exists())
    print("filename visible:", page.locator("text=Mingresume.docx").count())
    print("body snippet:", "Mingresume" in page.content())
    browser.close()
