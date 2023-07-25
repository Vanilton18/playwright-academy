from playwright.sync_api import sync_playwright


browser = sync_playwright().start().chromium.launch(headless=False)
page = browser.new_page()
page.goto("https://vanilton.net/web-test/text/")
# page.locator("id=password").fill("as")
page.get_by_text("Autenticar").click()
# page.get_by_text("First name:", exact=True).fill("admin")
page.get_by_label("First name:").fill("britinho")
page.get_by_text("Password:", exact=True).fill("1234567")
page.get_by_text("Credenciais inválidas. Tente novamente.").is_visible()
page.get_by_title("message-area").is_visible()
