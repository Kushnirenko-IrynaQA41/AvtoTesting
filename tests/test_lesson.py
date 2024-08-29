import math

import playwright
from playwright.sync_api import sync_playwright


def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5

def testsquare():
    num = 7
    assert  (7 * 7) == 40

def testequality():
    assert 10 == 11

def test_para():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.pause()
        page. goto('https://www.sinsay.com/ua/uk')
        page.locator('#cookiebotDialogOkButton').click() #прийняття куків
        page.locator('[alt="Школа"]').nth(1).click()
        page.locator('ul.categories a.category-link').nth(8).click()
        page.locator('.outline-close').wait_for()
        page.locator('.outline-close').click()
        page.locator('#categoryFilters').get_by_text('Ціна', exact=True).click()
        page.locator('pricespriceFrom').wait_for()
        page.locator('pricespriceFrom').fill('150')
        page.locator('pricespriceTo').fill('1000')
        page.locator('[type="submint"]').get_by_text('Фільтр').nth(1).click()


# Закриття браузера
    browser.close()

