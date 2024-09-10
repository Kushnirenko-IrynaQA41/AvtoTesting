import re
from playwright.sync_api import Playwright, sync_playwright, expect


class TodoApp:
    def __init__(self, headless=True):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=headless)
        self.page = self.browser.new_page()

    def open_todo_app(self):
        self.page.goto("https://demo.playwright.dev/todomvc/")

    # Створення нового завдання
    def create_task(self, task_name):
        self.page.get_by_placeholder("What needs to be done?").click()
        self.page.get_by_placeholder("What needs to be done?").fill(task_name)
        self.page.get_by_placeholder("What needs to be done?").press("Enter")

    # Редагування завдання
    def edit_task(self, old_text, new_text):
        self.page.get_by_text(old_text).click()
        self.page.get_by_role("textbox", name="Edit").fill(new_text)

    # Видалення завдання
    def delete_task(self, task_name):
        self.page.locator("li").filter(has_text=task_name).hover()
        self.page.get_by_role("button", name="Delete").click()

    # Позначення виконаних завдань
    def toggle_task(self, task_name, mark_completed=True):
        task_locator = self.page.locator("li").filter(has_text=task_name).get_by_label("Toggle Todo")
        if mark_completed:
            task_locator.check()
        else:
            task_locator.uncheck()

    # Фільтрування завдань
    def filter_tasks(self, filter_name):
        self.page.get_by_role("link", name=filter_name).click()

    # Видалення виконаних завдань
    def clear_completed_tasks(self):
        clear_button = self.page.get_by_role("button", name="Clear completed")
        expect(clear_button).to_be_visible()
        clear_button.click()

    # Закриття браузера
    def close_browser(self):
        self.browser.close()
        self.playwright.stop()


