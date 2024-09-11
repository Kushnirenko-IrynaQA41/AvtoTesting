import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.zara.com/ua/")
    page.get_by_role("button", name="Дозволити всі файли cookie").click()
    page.get_by_label("Натисніть Enter").click()
    page.get_by_role("button", name="Жінки").click()
    page.get_by_role("link", name="RED TEMPTATION 80 МЛ - - Zara").click()
    page.get_by_label("Додати RED TEMPTATION 80 МЛ").click()
    page.get_by_role("button", name="Переглянути кошик").click()
    page.get_by_role("button", name="ПРОДОВЖИТИ").click()
    page.get_by_role("button", name="Продовжити без реєстрації").click()
    page.get_by_label("Ім'я").click()
    page.get_by_label("Ім'я").fill("Марина")
    page.get_by_label("Прізвище").click()
    page.get_by_label("Прізвище").fill("Василенко")
    page.locator("div").filter(has_text=re.compile(r"^Адреса$")).nth(3).click()
    page.get_by_label("Адреса").click()
    page.get_by_label("Адреса").fill("місто Кременчук вулиця Ткаченка")
    page.get_by_label("Поштовий індекс").click()
    page.get_by_label("Поштовий індекс").fill("39605")
    page.get_by_label("Область").select_option("UAPL")
    page.get_by_label("Район").select_option("UAPLD06")
    page.get_by_label("Місто").select_option("UAPLD06C74")
    page.get_by_label("Електронна пошта").click()
    page.get_by_label("Електронна пошта").fill("")
    page.get_by_label("Електронна пошта").press("CapsLock")
    page.get_by_label("Електронна пошта").fill("iradzerj@rambler.com")
    page.get_by_label("Телефон").click()
    page.get_by_label("Телефон").fill("677676859")
    page.get_by_role("button", name="ПРОДОВЖИТИ").click()
    page.get_by_role("link", name="у пункті видачі у пункті видачі").click()
    page.locator("label").filter(has_text="КременчукВідділення №20").locator("div").first.click()
    page.get_by_role("button", name="Зберегти").click()
    page.get_by_role("button", name="ПРОДОВЖИТИ").click()
    page.get_by_role("img", name="VISA").click()
    page.get_by_role("button", name="ПРОДОВЖИТИ").click()
    page.get_by_role("link", name="Перейти на головну сторінку").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_run(playwright)
