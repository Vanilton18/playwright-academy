import pytest

from pages.pages import AuthPage
from playwright.sync_api import Page

# Chamado antes da execução do conftest.py
@pytest.fixture(scope="session")
def setup(browser_context_args, playwright):
    context = playwright.chromium.launch().new_context()
    page = context.new_page()
    page.goto("http://localhost:9000/dashboard/")
    email = page.get_by_test_id('email')
    email.fill('email@gmail.com')
    password = page.get_by_test_id("password")
    password.fill("")
    signin = page.get_by_role("button", name="SigN In")
    signin.click()
    page.get_by_text("Hello there, email@gmail.com").wait_for(timeout=5000)
    context.storage_state(path="storage.json")


class TestAuth:

    def test_login_valid(self, page: Page, setup):
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

    @pytest.mark.skip
    def test_login_invalid2(self, setup_tear_down):
        page = setup_tear_down
        auth = AuthPage(page)
        auth.navigate()
        auth.login("admiasd", "admi")
        auth.check_login_fail()

    @pytest.mark.skip
    def test_login_invalid3(self, setup_tear_down):
        page = setup_tear_down
        auth = AuthPage(page)
        auth.navigate()
        auth.login("admiasd", "admi")
        auth.check_login_fail()

    @pytest.mark.skip
    def test_login_invalid4(self, setup_tear_down):
        page = setup_tear_down
        auth = AuthPage(page)
        auth.navigate()
        auth.login("admiasd", "admi")
        auth.check_login_fail()
