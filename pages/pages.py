from playwright.sync_api import expect


class HomePage:
    def __init__(self, page):
        self.page = page

    def check_email_in_screen(self, email):
        expect(self.welcome_message_in_screen).to_have_text(email)

    @property
    def welcome_message_in_screen(self):
        return self.page.get_by_text("Hello there")


class AuthPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("/dashboard/")

    def login(self, email, password):
        page = self.page
        page.get_by_test_id('email').fill(email)
        page.get_by_test_id("password").fill(password)
        signin = page.get_by_role("button", name="SigN In")
        signin.click()

    def check_login_success(self):
        expect(self.page.get_by_role("button", name="SigN In")).not_to_be_visible()

    def check_login_fail(self):
        expect(self.page.get_by_text("Login went wrong. Please try again.")).to_be_visible()
