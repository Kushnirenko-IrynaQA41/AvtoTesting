import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.zara.com/ua/")
    page.get_by_role("button", name="Дозволити всі файли cookie").click()
    page.get_by_role("button", name="ЖІНКИ").click()
    page.get_by_role("link", name="сукні").click()
    page.get_by_label("Натисніть Enter").click()
    page.get_by_placeholder("Пошук за товаром, кольором, колекцією").click()
    page.get_by_placeholder("Пошук за товаром, кольором, колекцією").fill("ljjjdkkskskallala")
    page.get_by_placeholder("Пошук за товаром, кольором, колекцією").press("Enter")
    expect(page.locator("text=Пошук не дав результатів")).to_be_visible()
    # ---------------------
    context.close()
    browser.close()
