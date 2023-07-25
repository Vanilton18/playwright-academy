from playwright.sync_api import sync_playwright, expect
import re

browser = sync_playwright().start().chromium.launch(headless=False)
page = browser.new_page()
page.goto('https://vanilton.net/web-test/todos/')
page.locator(".new-todo").fill("task1")
page.keyboard.press("Enter")
page.locator(".new-todo").fill("task2")
page.keyboard.press("Enter")
page.locator(".new-todo").fill("task3")
page.keyboard.press("Enter")
# Verifica se existem 3 na lista
expect(page.locator('.todo-list li')).to_have_count(3)
page.get_by_role("listitem").filter(has_text="task1").get_by_role("checkbox").check()
page.get_by_role("link", name="Active").click()
expect(page.get_by_role("listitem").filter(has_text="task1")).to_be_hidden()
expect(page).to_have_url(re.compile(".*active"))
page.get_by_role("link", name="Completed").click()
expect(page.locator('.todo-list li')).to_have_count(1)
