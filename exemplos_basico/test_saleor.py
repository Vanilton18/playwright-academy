from playwright.sync_api import sync_playwright, expect
import os

def test_saleor_auth():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://localhost:9000/dashboard/")
    playwright.selectors.set_test_id_attribute("data-test-id")
    # email = page.get_by_test_id('email')
    # email.fill('admin@example.com')
    # password = page.get_by_test_id("password")
    # password.fill("admin")
    # signin = page.get_by_role("button", name="SigN In")
    # signin.click()
    page.get_by_text("Hello there, admin@example.com").wait_for(timeout=5000)
    context.storage_state(path="../test/storage.json")
    expect(page.get_by_text("Hello there, admin@example.com"), "Não localizado email do admin").to_be_visible()

    expect(page.locator("data-test-id=menu-list-item")).to_have_text(["PRODUCTS", "Orders", "Discounts"],
                                                                     ignore_case=True)
    expect(page.get_by_test_id("menu-list").locator("a")).to_contain_text(["Home", "Products", "Orders",
                                                                           "Customers", "Discounts", "Content",
                                                                           "Translations", "Apps", "Configuration"])
    expect(page.locator("data-test-id=menu-list").locator("a")).to_have_count(9)
