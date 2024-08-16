import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.facebook.com/")
    page.get_by_test_id("open-registration-form-button").click()
    page.get_by_placeholder("Ім'я").fill("Derk")
    page.get_by_placeholder("Ім'я").press("Tab")
    page.get_by_label("Прізвище").fill("Gun")
    page.get_by_label("Прізвище").press("Tab")
    page.get_by_label("Номер мобільного телефону або ел. пошта").fill("gugun@gmail.com")
    page.get_by_label("Номер мобільного телефону або ел. пошта").press("Tab")
    page.get_by_label("Номер мобільного телефону або ел. пошта").click()
    page.get_by_label("Введіть електронну адресу ще раз").click()
    page.get_by_label("Введіть електронну адресу ще раз").fill("gungun@gmail.com")
    page.get_by_label("Введіть електронну адресу ще раз").press("Tab")
    page.get_by_label("Новий пароль").click()
    page.get_by_label("Новий пароль").fill("w0eknjhhhhhhh")
    page.get_by_label("Рік").select_option("2008")
    page.get_by_label("жінка").check()
    page.get_by_role("button", name="Зареєструватися").click()
    page.get_by_label("Введіть електронну адресу ще раз").click()
    page.get_by_label("Введіть електронну адресу ще раз").press("ArrowLeft")
    page.get_by_label("Введіть електронну адресу ще раз").press("ArrowLeft")
    page.get_by_label("Введіть електронну адресу ще раз").press("ArrowLeft")
    page.get_by_label("Введіть електронну адресу ще раз").press("ArrowLeft")
    page.get_by_label("Введіть електронну адресу ще раз").press("ArrowLeft")
    page.get_by_label("Введіть електронну адресу ще раз").press("ArrowLeft")
    page.get_by_label("Введіть електронну адресу ще раз").press("ArrowLeft")
    page.get_by_label("Введіть електронну адресу ще раз").press("ArrowLeft")
    page.get_by_label("Введіть електронну адресу ще раз").press("ArrowLeft")
    page.get_by_label("Введіть електронну адресу ще раз").press("ArrowLeft")
    page.get_by_label("Введіть електронну адресу ще раз").press("ArrowLeft")
    page.get_by_label("Введіть електронну адресу ще раз").press("ArrowLeft")
    page.get_by_label("Введіть електронну адресу ще раз").press("ArrowLeft")
    page.get_by_label("Введіть електронну адресу ще раз").fill("gugun@gmail.com")
    page.get_by_role("button", name="Зареєструватися").click()
    page.locator("img").nth(2).click()

    # ---------------------
    context.close()
    browser.close()



def test_new ():
    with sync_playwright() as playwright:
        run(playwright)