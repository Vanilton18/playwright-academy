import pytest


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    playwright.selectors.set_test_id_attribute("data-test-id")
    return {
        **browser_context_args,
        # "storage_state": "storage.json",
        "viewport": {
            "width": 1920,
            "height": 1080,
        },
        # "locale": "it-IT"
    }
