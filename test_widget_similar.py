import time
import pytest
from .pages.widget_page import WidgetPage
from .pages.product_page import ProductPage
from .settings import profile, currencies


@pytest.fixture(scope="function", autouse=True)
def setup(browser):
    url = "https://alitools.io/ru"
    browser.get(url)
    window1 = browser.window_handles
    browser.switch_to.window(window1[1])
    time.sleep(1)
    if browser.name == "firefox":
        page = WidgetPage(browser, browser.current_url)
        page.setup_firefox()
        window2 = browser.window_handles
        browser.switch_to.window(window2[1])


def test_number_of_similar_products(browser):
    page = WidgetPage(browser, browser.current_url)
    page.should_be_option_start()
    page.click_on_cross_start_greeting()
    value_widget_similar_products = page.value_similar_products()
    page.open_similar_widget()
    value_similar_product_in_the_card = page.get_value_similar_products()
    assert value_widget_similar_products == value_similar_product_in_the_card, \
        f"Ошибка -> значение похожих товаров для виджета: {value_widget_similar_products}" \
        f" не равно значению в карточке: {value_similar_product_in_the_card} "


@pytest.mark.parametrize('currency', currencies)
# @pytest.mark.skip(reason="Есть ошибка")
def test_open_random_product_card(browser, currency, email=profile["Email"], password=profile["Password"]):
    if browser.name == "firefox":
        pytest.skip("firefox browser is used")
    page = WidgetPage(browser, browser.current_url)
    page.should_be_option_start()
    page.click_on_cross_start_greeting()
    # Получаем количество похожих продуктов
    value_widget_products = page.value_similar_products()
    page = ProductPage(browser, browser.current_url)
    # Получаем валюту страницы
    currency_page = page.get_currency_page()
    if currency_page == currency:
        pass
    else:
        # Выполням логин
        time.sleep(0.7)
        page.log_in_aliexpress(email, password)
        time.sleep(1)
        page.click_on_cress_repeated_favorites()
        page.open_profile()
        page.open_regional_settings()
        page.country_check()
        page.open_regional_currency_list()
        time.sleep(0.5)
        page.select_currency(currency)
        # Сохранение настроек
        page.save_settings()
        time.sleep(1)
        page.click_on_logo()
        page = WidgetPage(browser, browser.current_url)
        time.sleep(0.5)
        # Открываем товар из истории с новой уже валютой
        page.open_product_from_history_widget()
        time.sleep(0.5)
        window2 = browser.window_handles
        browser.switch_to.window(window2[2])
    if value_widget_products > 0:
        page = WidgetPage(browser, browser.current_url)
        page.open_similar_widget()
        # Выбрать случайный продукт
        choose_rand_prod = page.choose_random_product()
        # Взять url случайного продукта
        url_random_product = page.get_url_random_product(choose_rand_prod)
        # Взять цену случайного продукта
        price_random_product = page.get_price_random_product(choose_rand_prod)
        # Открыть случайный продукт
        page.open_random_product(choose_rand_prod)
        time.sleep(0.5)
        window3 = browser.window_handles
        if len(window3) == 3:
            browser.switch_to.window(window3[2])
            page.click_on_cress_repeated_favorites()
            time.sleep(0.5)
        else:
            browser.switch_to.window(window3[3])
        url_new = browser.current_url.split('.html')[0]
        # Проверям что Url который выбрали и открылся совпадают
        assert url_new == url_random_product,\
            f"Ошибка -> Url новой стараницы: {url_new} не равен выбранному: {url_random_product} "
        # Сравнить значения цен, в карточке [похожие] и на странице
        page = ProductPage(browser, browser.current_url)
        product_price_on_page = page.product_price()
        # print(price_random_product, product_price_on_page)
        assert price_random_product == product_price_on_page, \
            f"Ошибка -> цена в карточке: {price_random_product} не равен на странице: {product_price_on_page} "
        # Сранить количество заказов (Пока стоп- есть ошибка)
    else:
        assert value_widget_products == 0, f"У продукта нет похожих товаров: {value_widget_products}"


def test_sort_by_price(browser):
    page = WidgetPage(browser, browser.current_url)
    page.should_be_option_start()
    page.click_on_cross_start_greeting()
    page.open_similar_widget()
    page.open_drop_down_for_similar()
    page.select_drop_down_values_price()
    # Проверяем сортировку, что каждый следующий товар будет дороже
    page.check_sorting_by_price()


def test_sort_by_orders(browser):
    # url = "https://www.aliexpress.com/item/4001294911152.html"
    # url = "https://www.aliexpress.com/item/4000203522848.html"
    # browser.get(url)
    page = WidgetPage(browser, browser.current_url)
    page.should_be_option_start()
    page.click_on_cross_start_greeting()
    page.open_similar_widget()
    page.open_drop_down_for_similar()
    page.select_drop_down_values_orders()
    # Проверяем сортировку, что у каждого следующего товара меньше заказов
    page.check_sorting_by_orders()
