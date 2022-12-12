import time
import pytest
from .pages.product_page import ProductPage
from .pages.setting_page import SettingsPage
from .pages.widget_page import WidgetPage
from .settings import profile, url_sku


@pytest.fixture(scope="function", autouse=True)
def setup(browser):
    url = "https://alitools.io/ru"
    browser.get(url)
    page = ProductPage(browser, browser.current_url)
    page.switch_to_window(1)
    if browser.name == "firefox":
        page = WidgetPage(browser, browser.current_url)
        page.setup_firefox()
        page.switch_to_window(1)


# Как показала практика целесообразно запускать несколько раз его, оставлю значение- 3
# @pytest.mark.parametrize('execution_number', range(3))
@pytest.mark.skip(reason="there is an error")
def test_exact_price_display(browser):
    page = WidgetPage(browser, browser.current_url)
    page.should_be_option_start()
    page.click_on_cross_start_greeting()
    page = ProductPage(browser, browser.current_url)
    # Получаем валюту страницы
    currency_page = page.get_currency_page()
    page = WidgetPage(browser, browser.current_url)
    page.open_price_widget()
    # открываем настройки
    page.open_price_settings()
    page = SettingsPage(browser, browser.current_url)
    # открываем список валют
    page.open_currency_list()
    # выбираем нужную валюту, передаем через параменты
    page.choose_currency(currency_page)
    page.close_settings()
    # Получаем цену от виджета
    page = WidgetPage(browser, browser.current_url)
    extension_price = page.exact_price()
    # Получаем цену со страницы
    page = ProductPage(browser, browser.current_url)
    product_page_price = page.product_price()
    # print(product_page_price, extension_price)
    assert extension_price == product_page_price, \
        f"Ошибка -> цена: {extension_price} не равна цене: {product_page_price} "


def test_open_dropdown(browser):
    page = WidgetPage(browser, browser.current_url)
    page.should_be_option_start()
    page.click_on_cross_start_greeting()
    page.open_price_widget()
    page.open_price_drop_down_for_3_months()
    # Отображаются ли значения drop-down
    page.should_be_price_drop_down_value()


def test_period_display(browser):
    page = WidgetPage(browser, browser.current_url)
    page.should_be_option_start()
    page.click_on_cross_start_greeting()
    page.open_price_widget()
    value_months_for_3_months = page.get_value_months()
    assert value_months_for_3_months in [3, 4], \
        f"Ошибка -> количество месяцев равно: {value_months_for_3_months} a не : '3 или 4' "
    page.open_price_drop_down_for_3_months()
    time.sleep(0.5)
    page.select_value_for_half_a_year()
    value_months_for_half_a_year = page.get_value_months()
    assert value_months_for_half_a_year in [6, 7], \
        f"Ошибка -> количество месяцев равно: {value_months_for_half_a_year} a не : '6 или 7' "


# @pytest.mark.skip(reason="there is an error")
def test_widget_course_usd_check(browser, directory_name="widget", email=profile["Email"], password=profile["Password"]):
    page = WidgetPage(browser, browser.current_url)
    page.should_be_option_start()
    page.click_on_cross_start_greeting()
    page = ProductPage(browser, browser.current_url)
    currency_page = page.get_currency_page()
    if currency_page == "RUB":
        price_page = page.product_price()
        page = WidgetPage(browser, browser.current_url)
        page.open_price_widget()
        price_widget = page.exact_price()
        course_used = round(price_page / price_widget, 2)
        page.screenshot_page(directory_name)
        aliexpress_global = page.get_usd_course()
        assert course_used == aliexpress_global, \
            f"Курс страницы:{course_used} не равен курсу 'AliExpress Global':{aliexpress_global} "
    else:
        time.sleep(2)
        page.log_in_aliexpress(email, password)
        page.click_on_cress_repeated_favorites()
        page.open_profile()
        page.open_regional_settings()
        page.country_check()
        page.open_regional_currency_list()
        page.select_currency("RUB")
        # Сохранение выбранной валюты
        page.save_settings()
        time.sleep(2)
        page.click_on_logo()
        page = WidgetPage(browser, browser.current_url)
        # Открываем товар из истории с новой уже валютой
        page.open_product_from_history_widget()
        page.switch_to_window(2)
        page = ProductPage(browser, browser.current_url)
        price_page = page.product_price()
        page = WidgetPage(browser, browser.current_url)
        page.open_price_widget()
        price_widget = page.exact_price()
        course_used = round(price_page / price_widget, 2)
        page.screenshot_page(directory_name)
        aliexpress_global = page.get_usd_course()
        assert course_used == aliexpress_global, \
            f"Курс страницы:{course_used} не равен курсу 'AliExpress Global':{aliexpress_global} "


# Готово проверить в новой сборке
def test_different_sku(browser, url=url_sku):
    browser.get(url[0])
    page = WidgetPage(browser, browser.current_url)
    page.should_be_option_start()
    page.click_on_cross_start_greeting()
    page_product = ProductPage(browser, browser.current_url)
    product_page_price = page_product.product_price()
    currency_page = page_product.get_currency_page()
    page.open_price_widget()
    page.open_price_settings()
    page_settings = SettingsPage(browser, browser.current_url)
    page_settings.open_currency_list()
    page_settings.choose_currency(currency_page)
    page_settings.close_settings()
    extension_price = page.exact_price()
    time.sleep(0.5)
    page.close_price_card()
    assert extension_price == int(product_page_price), \
        f"Ошибка -> цена: {extension_price} не равна цене: {int(product_page_price)} "
    time.sleep(1)
    index_active_sku = page_product.get_active_sku()
    page_product.select_next_sku(index_active_sku)
    product_page_price = page_product.product_price()
    page.open_price_widget()
    extension_price = page.exact_price()
    time.sleep(0.5)
    page.close_price_card()
    assert extension_price == int(product_page_price), \
        f"Ошибка -> цена: {extension_price} не равна цене: {int(product_page_price)} "
    time.sleep(1)
    index_active_sku = page_product.get_active_sku()
    page_product.select_next_sku(index_active_sku)
    product_page_price = page_product.product_price()
    page.open_price_widget()
    extension_price = page.exact_price()
    time.sleep(0.5)
    page.close_price_card()
    assert extension_price == int(product_page_price), \
        f"Ошибка -> цена: {extension_price} не равна цене: {int(product_page_price)} "
