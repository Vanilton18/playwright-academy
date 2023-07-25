from playwright.sync_api import Page


def test_basic_test(page: Page):
    assert 1 == 1
