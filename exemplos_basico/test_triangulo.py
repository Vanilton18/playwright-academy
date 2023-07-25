from playwright.sync_api import sync_playwright


browser = sync_playwright().start().chromium.launch(headless=False)
page = browser.new_page()
page.goto("https://vanilton.net/web-test/triangulo")


def preenche_triangulo(v1, v2, v3):
    page.get_by_label('Vértice 1').fill("2")
    page.locator("input[name=V1]").fill(v1)
    page.locator("input[name=V2]").fill(v2)
    page.locator("input[name=V3]").fill(v3)


preenche_triangulo("2", "2", "2")
page.get_by_text("Identificar").click()
page.get_by_alt_text("triângulo equilátero").wait_for(timeout=1000)
print(page.get_by_alt_text("triângulo equilátero").is_visible())
page.get_by_label("")

preenche_triangulo("5", "5", "2")
page.get_by_text("Identificar").click()
page.get_by_alt_text("triângulo isósceles").wait_for(timeout=1000)
print(page.get_by_alt_text("triângulo isósceles").is_visible())

preenche_triangulo("10", "6", "5")
page.get_by_text("Identificar").click()
page.get_by_alt_text("triângulo escaleno").wait_for(timeout=1000)
print(page.get_by_alt_text("triângulo escaleno").is_visible())

preenche_triangulo("5", "2", "1")
page.get_by_text("Identificar").click()
print(page.get_by_text("Triangulo inválido").is_visible())
