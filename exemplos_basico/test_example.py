from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()
browser = playwright.firefox.launch(headless=False)
page = browser.new_page()
page.goto("https://vanilton.net")
site_title = page.title()
page.screenshot(path=f'{site_title}.png')
browser.close()
playwright.stop()
