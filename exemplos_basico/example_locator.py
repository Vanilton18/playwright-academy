from playwright.sync_api import sync_playwright

browser = sync_playwright().start().chromium.launch(headless=False)
page = browser.new_page()
page.goto('http://vanilton.net/web-test/display/')
page.locator(".circle:visible")

page.locator("section", has=page.locator(".circle >> visible=true")).click()
