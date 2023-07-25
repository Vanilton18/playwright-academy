from pages.pages import AuthPage
from playwright.sync_api import Page


class TestAuth:

    def test_login_valid(self, page: Page):
        auth = AuthPage(page)
        auth.navigate()
        auth.login("admin@example2.com", "admin")
        auth.check_login_success()
        assert 3 == 4

    def test_login_invalid(self, page: Page):
        auth = AuthPage(page)
        auth.navigate()
        auth.login("admiasd", "admi")
        auth.check_login_fail()

    def test_login_invalid2(self, page: Page):
        auth = AuthPage(page)
        auth.navigate()
        auth.login("admiasd", "admi")
        auth.check_login_fail()

    def test_login_invalid3(self, page: Page):
        auth = AuthPage(page)
        auth.navigate()
        auth.login("admiasd", "admi")
        auth.check_login_fail()
