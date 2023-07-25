from playwright.sync_api import sync_playwright, expect
import re

playwright = sync_playwright().start()
playwright.selectors.set_test_id_attribute('id')
browser = playwright.chromium.launch(headless=False).new_page()
browser.goto('https://vanilton.net/web-test/triangulo_v2/')

browser.locator('[id="sideA"]').fill('2')
browser.locator('[id="sideB"]').fill('2')
browser.locator('[id="sideC"]').fill('2')
browser.locator('[type="submit"]').click()
browser.get_by_text('Triângulo Equilátero', exact=True).wait_for(timeout=1000)
expect(browser.get_by_text('Triângulo Equilátero', exact=True)).to_be_visible()

expect(browser.get_by_test_id('triangleImage')) \
    .to_have_attribute("src", re.compile(".*equilatero.png"))
expect(browser.get_by_test_id('triangleImage')).to_have_id('triangleImage')

browser.locator('[id="sideA"]').fill('2')
browser.locator('[id="sideB"]').fill('3')
browser.locator('[id="sideC"]').fill('4')
browser.locator('[type="submit"]').click()
browser.get_by_text('Triângulo Escaleno', exact=True).wait_for(timeout=1000)
print(browser.get_by_text('Triângulo Escaleno', exact=True).is_visible())
expect(browser.get_by_test_id('triangleImage')) \
    .to_have_attribute("src", "https://vanilton.net/web-test/triangulo/escaleno.png")
expect(browser.get_by_test_id('triangleImage')).to_have_id('triangleImage')

browser.locator('[id="sideA"]').fill('5')
browser.locator('[id="sideB"]').fill('5')
browser.locator('[id="sideC"]').fill('2')
browser.locator('[type="submit"]').click()
browser.get_by_text('Triângulo Isósceles', exact=True).wait_for(timeout=1000)
print(browser.get_by_text('Triângulo Isósceles', exact=True).is_visible())
expect(browser.get_by_test_id('triangleImage')) \
    .to_have_attribute("src", "https://vanilton.net/web-test/triangulo/isosceles.png")

browser.locator('[id="sideA"]').fill('10')
browser.locator('[id="sideB"]').fill('2')
browser.locator('[id="sideC"]').fill('3')
browser.locator('[type="submit"]').click()
print(browser.get_by_text('Os lados não formam um triângulo válido.').is_visible())
# print('Os lados não formam um triângulo válido.')
