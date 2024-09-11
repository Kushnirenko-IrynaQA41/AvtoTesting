# from playwright.sync_api import sync_playwright
# from pytest import fixture
#
# from models.lucas import Lucas
#
# @fixture()
# def get_test():
#     with sync_playwright() as playwright:
#         yield playwright
#
# @fixture()
# def test_lucas(get_test):
#     lucas = Lucas(get_test)
#     yield lucas
#     lucas.close()

import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # або p.firefox.launch(), p.webkit.launch()
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
