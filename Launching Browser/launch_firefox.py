from playwright.sync_api import sync_playwright

with sync_playwright() as p_firefox:
    browser = p_firefox.firefox.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.guvi.in")
    print(page.title())
    browser.close()