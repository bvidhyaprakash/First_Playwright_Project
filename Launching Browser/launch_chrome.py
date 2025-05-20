#import all necessary dependencies

from playwright.sync_api import sync_playwright
from time import sleep


#using sync_playwright as an playwright object 'p'
with sync_playwright() as p:
    # choose any channel if needed(chrome, msedge, other beta version which need to be installed)
    # browser = p.chromium.launch(headless=False)
    # browser = p.chromium.launch(channel="chrome", headless=False)
    browser = p.chromium.launch(channel="msedge", headless=False)
    page = browser.new_page()
    page.goto("https://www.guvi.in")
    print(page.title())
    # print(page.url)
    browser.close()
