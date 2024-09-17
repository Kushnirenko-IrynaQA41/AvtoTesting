from playwright.sync_api import sync_playwright
from zara_test import ZaraTest  # Імпорт класу із файлу 'zara_test.py'

def test_run():
    with sync_playwright() as playwright:
        zara_test = ZaraTest(playwright)
        zara_test.open_site()
        zara_test.select_women_dresses()
        zara_test.add_mens_chinos_to_cart()
        zara_test.select_newborn_items ()
        user_data = {
            'first_name': 'Катерина',
            'last_name': 'Іванченко',
            'address': 'Ткаченка 5',
            'postal_code': '39605',
            'region': 'UAPL',
            'city': 'UAPLD06C74',
            'email': 'iradzerj@gmail.com',
            'phone': '677676859'
        }
        zara_test.fill_delivery_form(user_data)
        zara_test.navigate_to_help()
        zara_test.view_return_info()
        zara_test.search_for_hair_accessories_and_store("київ")
        zara_test.close()
