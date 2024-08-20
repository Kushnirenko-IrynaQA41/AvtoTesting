import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://novaposhta.ua/")
    page.locator("#popup_info").get_by_text("закрыть").click()
    page.get_by_role("link", name="Вхід").click()
    page.get_by_role("button", name="Увійти").click()
    page.get_by_role("menuitem", name="як приватна").click()
    page.get_by_label("Введіть мобільний телефон *").fill("+380 96 584 83 95")
    page.get_by_label("Введіть мобільний телефон *").press("Tab")
    page.get_by_role("button", name="Далі").click()
    page.get_by_role("button", name="Продовжити").click()

    # ---------------------
    context.close()
    browser.close()



def test_zarabuy():
    with sync_playwright() as playwright:
        run(playwright)