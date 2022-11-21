import time

import pytest
from .pages.product_page import ProductPage
from .pages.setting_page import SettingsPage
from .pages.widget_page import WidgetPage


@pytest.fixture(scope="function", autouse=True)
def setup(browser):
    url = "https://alitools.io/ru"
    browser.get(url)
    window1 = browser.window_handles
    browser.switch_to.window(window1[1])


# Как показала практика целесообразно запускать несколько раз его, оставлю значение- 3
# @pytest.mark.parametrize('execution_number', range(3))
# Добавить проверку нужно ли менять валюту

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
    time.sleep(10)
    extension_price = page.exact_price()
    # Получаем цену со страницы
    page = ProductPage(browser, browser.current_url)
    product_page_price = page.product_price()
    print(product_page_price, extension_price)
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
    page.select_value_for_half_a_year()
    value_months_for_half_a_year = page.get_value_months()
    assert value_months_for_half_a_year in [6, 7], \
        f"Ошибка -> количество месяцев равно: {value_months_for_half_a_year} a не : '6 или 7' "


# Добработать тест
@pytest.mark.skip(reason="Есть ошибка")
def test_widget_course_usd_check(browser, directory_name="widget"):
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
