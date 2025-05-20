from playwright.sync_api import sync_playwright

with sync_playwright() as p_webkit:
    browser = p_webkit.webkit.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.guvi.in")
    print(page.title())
    print(page.url)
    browser.close()