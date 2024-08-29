import re
from playwright.sync_api import Playwright, sync_playwright, expect


# Створення нового завдання
def test_todos():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://demo.playwright.dev/todomvc/")
        page.get_by_placeholder("What needs to be done?").click()
        page.get_by_placeholder("What needs to be done?").fill("Написати тест")
        page.get_by_placeholder("What needs to be done?").press("Enter")
        page.get_by_placeholder("What needs to be done?").fill("Написати ще один тест")
        page.get_by_placeholder("What needs to be done?").press("Enter")
        page.get_by_placeholder("What needs to be done?").fill("Та ще один тест)")
        page.get_by_placeholder("What needs to be done?").press("Enter")

        # Закриваємо браузер всередині контексту
        browser.close()

# Редагування завдання Цей тест падає на останньому кроці, чому я не знаю. Щось з активацією поля
def test_todos2():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://demo.playwright.dev/todomvc/")
        page.goto("https://demo.playwright.dev/todomvc/#/")
        page.get_by_placeholder("What needs to be done?").click()
        page.get_by_placeholder("What needs to be done?").fill("1")
        page.get_by_placeholder("What needs to be done?").press("Enter")
        page.get_by_placeholder("What needs to be done?").fill("2")
        page.get_by_placeholder("What needs to be done?").press("Enter")
        page.get_by_placeholder("What needs to be done?").fill("3")
        page.get_by_placeholder("What needs to be done?").press("Enter")
        page.get_by_text("1").click()
        page.get_by_role("textbox", name="Edit").fill("3")

        # Закриваємо браузер
        browser.close()

# Видалення завдання
def test_todos3():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://demo.playwright.dev/todomvc/")
        page.goto("https://demo.playwright.dev/todomvc/#/")
        page.get_by_placeholder("What needs to be done?").click()
        page.get_by_placeholder("What needs to be done?").fill("1")
        page.get_by_placeholder("What needs to be done?").press("Enter")
        page.get_by_placeholder("What needs to be done?").fill("2")
        page.get_by_placeholder("What needs to be done?").press("Enter")
        page.get_by_placeholder("What needs to be done?").fill("3")
        page.get_by_placeholder("What needs to be done?").press("Enter")
        page.get_by_role("button", name="Delete").click()

        # Закриваємо браузер
        browser.close()

# Позначення виконаних завдань
def test_todos4():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://demo.playwright.dev/todomvc/")
        page.goto("https://demo.playwright.dev/todomvc/#/")
        page.get_by_placeholder("What needs to be done?").click()
        page.get_by_placeholder("What needs to be done?").fill("1")
        page.get_by_placeholder("What needs to be done?").press("Enter")
        page.get_by_placeholder("What needs to be done?").fill("2")
        page.get_by_placeholder("What needs to be done?").press("Enter")
        page.get_by_placeholder("What needs to be done?").fill("3")
        page.get_by_placeholder("What needs to be done?").press("Enter")


        page.locator("li").filter(has_text="1").get_by_label("Toggle Todo").check()
        page.locator("li").filter(has_text="2").get_by_label("Toggle Todo").check()


        page.get_by_role("link", name="Completed").click()


        page.get_by_role("link", name="All").click()


        page.locator("li").filter(has_text="2").get_by_label("Toggle Todo").uncheck()
        page.locator("li").filter(has_text="1").get_by_label("Toggle Todo").uncheck()

        # Закриваємо браузер
        browser.close()

# Фільтрування завдань
def test_todos5():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://demo.playwright.dev/todomvc/")
        page.goto("https://demo.playwright.dev/todomvc/#/")
        page.get_by_placeholder("What needs to be done?").click()
        page.get_by_placeholder("What needs to be done?").fill("1")
        page.get_by_placeholder("What needs to be done?").press("Enter")
        page.get_by_placeholder("What needs to be done?").fill("2")
        page.get_by_placeholder("What needs to be done?").press("Enter")
        page.get_by_placeholder("What needs to be done?").fill("3")
        page.get_by_placeholder("What needs to be done?").press("Enter")
        page.get_by_placeholder("What needs to be done?").fill("4")
        page.get_by_placeholder("What needs to be done?").press("Enter")

        page.locator("li").filter(has_text="1").get_by_label("Toggle Todo").check()

        page.get_by_role("button", name="Delete").click()

        page.get_by_role("link", name="Active").click()
        page.get_by_role("link", name="Completed").click()

        page.get_by_role("link", name="All").click()

        # Закриваємо браузер
        browser.close()

# Видалення виконаних завдань (тут мені дпопоміг GPT)
def test_todos6():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://demo.playwright.dev/todomvc/")
        page.goto("https://demo.playwright.dev/todomvc/#/")

        # Додаємо завдання
        page.get_by_placeholder("What needs to be done?").click()
        page.get_by_placeholder("What needs to be done?").fill("1")
        page.get_by_placeholder("What needs to be done?").press("Enter")
        page.get_by_placeholder("What needs to be done?").fill("2")
        page.get_by_placeholder("What needs to be done?").press("Enter")
        page.get_by_placeholder("What needs to be done?").fill("3")
        page.get_by_placeholder("What needs to be done?").press("Enter")
        page.get_by_placeholder("What needs to be done?").fill("4")
        page.get_by_placeholder("What needs to be done?").press("Enter")

        # Відмічаємо завдання як виконані
        # Додаємо явне очікування для завдань
        task_1 = page.locator("li").filter(has_text="1").get_by_label("Toggle Todo")
        expect(task_1).to_be_visible()
        task_1.check()

        task_2 = page.locator("li").filter(has_text="2").get_by_label("Toggle Todo")
        expect(task_2).to_be_visible()
        task_2.check()

        task_3 = page.locator("li").filter(has_text="3").get_by_label("Toggle Todo")
        expect(task_3).to_be_visible()
        task_3.check()

        # Очікуємо, що кнопка "Clear completed" видима та натискаємо на неї
        clear_button = page.get_by_role("button", name="Clear completed")
        expect(clear_button).to_be_visible()
        clear_button.click()

        # Закриваємо браузер
        browser.close()

# Тест на пунк 7 чек-ліста не написаний. Не знаю чи можливо автотестом перевірити лічильник невиконанх завдань


# Перевірка збереження стану завдань після оновлення сторінки
def test_todos8():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://demo.playwright.dev/todomvc/")

        page.get_by_placeholder("What needs to be done?").click()
        page.get_by_placeholder("What needs to be done?").fill("1")
        page.get_by_placeholder("What needs to be done?").press("Enter")
        page.get_by_placeholder("What needs to be done?").fill("2")
        page.get_by_placeholder("What needs to be done?").press("Enter")
        page.get_by_placeholder("What needs to be done?").fill("3")
        page.get_by_placeholder("What needs to be done?").press("Enter")
        page.get_by_placeholder("What needs to be done?").fill("4")
        page.get_by_placeholder("What needs to be done?").press("Enter")

        page.locator("li").filter(has_text="4").get_by_label("Toggle Todo").check()
        page.locator("li").filter(has_text="3").get_by_label("Toggle Todo").check()

        page.goto("https://demo.playwright.dev/todomvc/#/")

        # Закриваємо браузер
        browser.close()
