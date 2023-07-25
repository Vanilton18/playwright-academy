from playwright.sync_api import expect, BrowserContext
import re
import pytest


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    playwright.selectors.set_test_id_attribute("data-test-id")
    playwright.chromium.launch(headless=False)
    return {
        **browser_context_args,
        "storage_state": "storage.json",
        "viewport": {
            "width": 1920,
            "height": 1080,
        },
        "locale": "it-IT"
    }


def test_saleor_auth(context: BrowserContext):
    page = context.new_page()
    page.goto("https://demo.saleor.io/dashboard/")
    page.get_by_text("Hello there, admin@example.com").wait_for(timeout=5000)
    expect(page.locator("ul.MuiList-root > li")).to_have_count(10)
    activity_list = page.locator("ul.MuiList-root > li").all()
    # 1. Criar um localizador para identificar a lista de atividades
    orders = []
    # 2. Deve ser possível iterar nos itens da lista
    # 3. Criar uma lista de Ordens extraída da lista de atividades, considerar apenas o números das ordens, pode-se
    # utilizar regex
    for item in activity_list:
        orders.append(re.search(r'#(\d+)', item.inner_text()).group(1))
    # 4. Abrir uma página nova e na tela de pesquisa de ordens, consultar os números das ordens contidas na lista
    page2 = context.new_page()
    page2.goto("https://demo.saleor.io/dashboard/orders?asc=false&sort=number")

    total = 0
    for order in orders:
        page2.get_by_test_id("search-input").fill(order)
        expect(page2.locator('//td[@aria-colindex="2"]')).to_have_text(order)
        total += float(page2.locator("id=glide-cell-6-0").text_content())

    # 5. Por fim somar todos os valores das ordens pesquisadas
    assert total == 1714.20
