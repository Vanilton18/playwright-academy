from playwright.sync_api import expect, BrowserContext
import re
import pytest
import os


# Segundo autentica na primeira vez e cria o token via storage
@pytest.fixture(scope="session")
def setup(browser_context_args, playwright):
    context = playwright.chromium.launch().new_context()
    page = context.new_page()
    page.goto("http://localhost:9000/dashboard/")
    email = page.get_by_test_id('email')
    email.fill('email@example.com')
    password = page.get_by_test_id("password")
    password.fill("senha")
    signin = page.get_by_role("button", name="SigN In")
    signin.click()
    page.get_by_text("Hello there, email@example.com").wait_for(timeout=5000)
    context.storage_state(path="storage.json")


def test_saleor_user(context: BrowserContext, setup):
    page = context.new_page()
    page.goto("/")
    page.get_by_text("Hello there, email@example.com").wait_for(timeout=5000)
    expect(page.get_by_text("Hello there, email@example.com")).to_be_visible()


def test_saleor_auth(setup, context: BrowserContext):
    page = context.new_page()
    page.goto("/dashboard/")
    page.get_by_text("Hello there, email@example.com").wait_for(timeout=5000)
    expect(page.locator("ul.MuiList-root > li")).to_have_count(1)
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
    page2.goto("/dashboard/orders?asc=false&sort=number")

    total = 0
    for order in orders:
        page2.get_by_test_id("search-input").fill(order)
        expect(page2.locator('//td[@aria-colindex="2"]')).to_have_text(order)
        total += float(page2.locator("id=glide-cell-6-0").text_content())

    # 5. Por fim somar todos os valores das ordens pesquisadas
    assert total == 3000.0
