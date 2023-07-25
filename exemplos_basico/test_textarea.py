from playwright.sync_api import sync_playwright, expect


def test_run():
    playwright = sync_playwright().start()
    playwright.selectors.set_test_id_attribute('id')
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://vanilton.net/web-test/textarea/")
    expect(page.get_by_test_id("story")).to_be_editable()
    expect(page.get_by_test_id("story")).to_be_focused()
    page.get_by_text("Encerrar história").click()
    expect(page.get_by_test_id("story").and_(page.locator("[name='story']"))).is_visible()
    expect(page.get_by_test_id("story")).not_to_be_focused()
    expect(page.get_by_test_id("story")).not_to_be_editable()
    expect(page.get_by_test_id('story')).to_have_css('background-color', 'rgb(220, 20, 60)')
    expect(page.get_by_test_id("story")).to_have_css("padding", "10px")
    page.get_by_role("button", name="Reabrir história").click()
    expect(page.get_by_test_id('story')).to_have_css('background-color', 'rgb(255, 255, 255)')
    expect(page.get_by_test_id('story')).not_to_have_css('background-color', 'rgb(220, 20, 60)')

    page.get_by_test_id("story").is_hidden()
    expect(page.get_by_test_id("story")).to_be_editable()
    page.get_by_test_id("toggle_button_story").click()

    page.get_by_role("button", name="Reabrir história").click()
    page.get_by_test_id("story").clear()
    expect(page.get_by_test_id("story")).to_be_empty()

    page.get_by_test_id("story").fill("minha historia")
    expect(page.get_by_test_id("story")).not_to_be_empty()

    expect(page.get_by_test_id("toggle_button_story")).to_be_enabled()
    page.get_by_test_id("checkbox").check()
    expect(page.get_by_test_id("toggle_button_story")).not_to_be_enabled()
