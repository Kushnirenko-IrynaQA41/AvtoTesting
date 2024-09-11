from playwright.sync_api import Playwright, sync_playwright, expect


def test_invalid_url(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # перехід на неіснуючу адресу
    invalid_url = "https://www.zara.com/ua/nonexistentpage"
    page.goto(invalid_url, wait_until="domcontentloaded")

    page.wait_for_timeout(3000)  # Затримка в 3 секунди

    error_message = page.locator('.page-not-found-view__title')
    expect(error_message).to_be_visible(timeout=10000)  # Збільшений тайм-аут до 10 секунд

    # Закриття контексту і браузера
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_invalid_url(playwright)
