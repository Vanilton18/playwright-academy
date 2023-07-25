from playwright.sync_api import sync_playwright
import re

browser = sync_playwright().start().chromium.launch(headless=False)
page = browser.new_page()
page.goto('https://vanilton.net/web-test/input-types/')
locator = page.get_by_role("checkbox", name="Moto")
page.wait_for_timeout(5000)
locator.check()
page.wait_for_timeout(5000)
locator.uncheck()
page.wait_for_timeout(5000)
page.get_by_role("radio", name="M").check()
page.get_by_role("checkbox", name=re.compile("MOTO", re.IGNORECASE)).check()
