

def test_web_shop(page):
    page.goto('https://lukas-sweet.shop/')
    page.get_by_text('Каталог смаколиків').hover()
    page.wait_for_selector('#oct-menu-dropdown-menu')
    page.locator('.oct-menu-item-name').filter(has_text='Цукерки').click()
    page.locator('.us-cat-button-cart').nth(1).click()
    page.get_by_role('button', name='Продовжити покупки').click()

