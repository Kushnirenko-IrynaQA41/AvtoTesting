import re

from playwright.sync_api import Playwright, expect


class ZaraTest:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def open_site(self):
        self.page.goto("https://www.zara.com/ua/")
        self.page.get_by_role("button", name="Дозволити всі файли cookie").click()
        expect(self.page.get_by_role("button", name="ЖІНКИ")).to_be_visible()

    def select_women_dresses(self, page=None):
        self.page.get_by_role("button", name="ЖІНКИ").click()
        self.page.get_by_role("link", name="сукні").click()

        # Вибір фільтрів
        self.page.get_by_role("button", name="КОЛІР").click()
        self.page.locator("label").filter(has_text="ANIMAL PRINT").locator("span").first.click()

        # Вибір колекції
        self.page.get_by_role("button", name="КОЛЕКЦІЯ").click()
        self.page.get_by_text("БІЛИЗНА").click()

        # Оберіть правильний текст
        self.page.get_by_text("CRLR").click()

        # Вибір товару
        self.page.get_by_role("link", name="ТЮЛЕВА СУКНЯ-СЛІП З ТВАРИННИМ ПРИНТОМ - Леопардовий Zara").click()

        # Вибір розміру
        self.page.get_by_role("option", name="S").click()

        # Додавання до кошика
        self.page.get_by_label("Додати ТЮЛЕВА СУКНЯ-СЛІП З ТВАРИННИМ ПРИНТОМ").click()

        # Закриття вікна
        self.page.get_by_label("Закрити").click()

    def add_mens_chinos_to_cart(self):
        # Відкрити меню та вибрати "чоловіки"
        self.page.get_by_label("Відкрити меню").click()
        self.page.get_by_role("button", name="чоловіки").first.click()
        expect(self.page.get_by_role("button", name="чоловіки").first).to_be_visible()

        # Вибір категорії "штани"
        self.page.locator("a").filter(has_text="штани").nth(1).click()

        # Фільтрація за кольором
        self.page.get_by_role("button", name="КОЛІР").click()
        self.page.locator("label").filter(has_text="Коричневий").locator("span").first.click()

        # Вибір продукту
        self.page.get_by_role("link", name="Чіно", exact=True).click()
        self.page.get_by_role("link", name="ШИРОКІ ШТАНИ-ЧІНО - бежево-коричневий Zara").click()

        # Вибір розміру
        self.page.get_by_role("option", name="40").click()

        # Додавання до кошика
        self.page.get_by_label("Додати ШИРОКІ ШТАНИ-ЧІНО").click()

        # Закриття вікна
        self.page.get_by_label("Закрити").click()

    def select_newborn_items(self):
        # Відкриваємо меню і вибираємо секцію для дітей
        self.page.get_by_label("Відкрити меню").click()
        self.page.get_by_role("button", name="діти").first.click()

        # Вибір категорії "до 6 місяців"
        self.page.get_by_role("button", name="–6 місяців").click()
        self.page.get_by_role("link", name="/// новинки").click()

        # Фільтр за кольором
        self.page.get_by_role("button", name="КОЛІР").click()
        self.page.locator("label").filter(has_text="Червоний").locator("span").first.click()

        # Вибір типу товару
        self.page.get_by_role("button", name="ТИП ТОВАРУ").click()
        self.page.get_by_role("button", name="ТИП ТОВАРУ").click()

        # Вибір конкретного товару
        self.page.get_by_role("link", name="ТРИКОТАЖНИЙ КОМБІНЕЗОН ОБОРОТНОГО ПЕРЕПЛЕТЕННЯ - Червонуватий Zara").click()

        # Переходимо до іншої сторінки для подальших дій
        self.page.goto("https://www.zara.com/ua/uk/kids-newborn-new-l6843.html?v1=2434926")

        # Фільтр по кольору
        self.page.get_by_role("button", name="КОЛІР (1)").click()
        self.page.locator("label").filter(has_text="З принтом").locator("span").first.click()
        self.page.locator("label").filter(has_text="Зелений").locator("span").first.click()

        # Вибір товару "ОДНОТОННИЙ КРЕПОВИЙ ЧЕПЧИК"
        self.page.get_by_role("link", name="ОДНОТОННИЙ КРЕПОВИЙ ЧЕПЧИК - Морський зелений Zara").click()
        self.page.get_by_role("option", name="-3 місяці(-в) (38 cm)").click()

        # Додаємо товар до кошика
        self.page.get_by_label("Додати ОДНОТОННИЙ КРЕПОВИЙ ЧЕПЧИК").click()
        self.page.get_by_label("Закрити").click()

        self.page.get_by_label("Товари в кошику: 3").click()
        self.page.get_by_label("Додати ще одну одиницю товару - ОДНОТОННИЙ КРЕПОВИЙ ЧЕПЧИК").click()
        self.page.get_by_label("Додати ще одну одиницю товару - ОДНОТОННИЙ КРЕПОВИЙ ЧЕПЧИК").click()

    def fill_delivery_form(self, user_data):
        self.page.get_by_role("button", name="ПРОДОВЖИТИ").click()
        self.page.get_by_role("button", name="Продовжити без реєстрації").click()
        self.page.locator("#main div").filter(has_text="Ім'яПрізвищеАдресаДодаткова інформаціяПоштовий індекс--КиївХарківська областьОде").nth(2).click()
        self.page.get_by_label("Ім'я").click()
        self.page.get_by_label("Ім'я").fill("")
        self.page.get_by_label("Ім'я").press("CapsLock")
        self.page.get_by_label("Ім'я").fill("Катерина")
        self.page.get_by_label("Ім'я").press("Tab")
        self.page.get_by_label("Прізвище").fill("Іванченко")
        self.page.get_by_label("Адреса").click()
        self.page.get_by_label("Адреса").fill("Ткаченка 5")
        self.page.get_by_label("Поштовий індекс").click()
        self.page.get_by_label("Поштовий індекс").fill("39605")
        self.page.get_by_label("Область").select_option("UAPL")
        self.page.get_by_label("Район").select_option("UAPLD06")
        self.page.get_by_label("Місто").select_option("UAPLD06C74")
        self.page.get_by_label("Електронна пошта").click()
        self.page.get_by_label("Електронна пошта").press("CapsLock")
        self.page.get_by_label("Електронна пошта").fill("iradzerj@gmail.com")
        self.page.get_by_label("Телефон").click()
        self.page.get_by_label("Телефон").fill("677676859")
        self.page.get_by_role("button", name="ПРОДОВЖИТИ").click()
        self.page.get_by_role("link", name="у пункті видачі у пункті видачі").click()
        self.page.get_by_placeholder(" ").click()
        self.page.get_by_placeholder(" ").fill("")
        self.page.get_by_placeholder(" ").press("CapsLock")
        self.page.get_by_placeholder(" ").fill("кременчук")
        self.page.get_by_role("button", name="Пошук").click()
        self.page.locator("label").filter(has_text=re.compile(r"^КременчукВідділення №2$")).click()
        self.page.get_by_role("button", name="Зберегти").click()
        self.page.get_by_role("button", name="ПРОДОВЖИТИ").click()
        self.page.get_by_role("img", name="VISA").click()
        self.page.locator("div").filter(has_text=re.compile(r"^VISA$")).click()
        self.page.get_by_role("button", name="ПРОДОВЖИТИ").click()
        self.page.get_by_role("link", name="Перейти на головну сторінку").click()

    def navigate_to_help(self):
        self.page.get_by_role("link", name="ДОПОМОГА").click()

    def view_return_info(self):
        self.page.get_by_role("button", name="ЯК ЗДІЙСНИТИ ПОВЕРНЕННЯ").click()
        self.page.get_by_role("link", name="Показати всі теми довідника").click()
        self.page.get_by_role("link", name="ЯК ЗДІЙСНИТИ ПОВЕРНЕННЯ").click()
        self.page.get_by_role("button", name="ЯК ПІДГОТУВАТИ ПАКУНОК ІЗ ПОВЕРНЕННЯМ?").click()
        self.page.get_by_role("button", name="Я ПОДАВ(-ЛА) ЗАПИТ НА ЗАБІР ЗАМОВЛЕННЯ, АЛЕ ЙОГО НЕ БУЛО ВИКОНАНО. ЩО Я МОЖУ ЗРО").click()
        self.page.get_by_role("button", name="ОСОБЛИВІ УМОВИ ПОВЕРНЕННЯ").click()

    def search_for_hair_accessories_and_store(self, city):
        self.page.get_by_text("Аксесуари для волосся").click()
        self.page.get_by_label("Відкрити меню").click()
        self.page.get_by_role("link", name="магазини").nth(2).click()
        self.page.get_by_placeholder(" ").fill(city)
        self.page.get_by_placeholder(" ").press("Enter")

    def close(self):
        self.context.close()
        self.browser.close()
