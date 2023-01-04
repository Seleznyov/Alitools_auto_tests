import time
import pytest
from .pages.product_page import ProductPage
from .pages.setting_page import SettingsPage
from .pages.widget_page import WidgetPage
from .settings import profile, url_sku


@pytest.fixture(scope="function", autouse=True)
def setup(browser):
    url = "https://www.google.com/"
    browser.get(url)
    page_product = ProductPage(browser, browser.current_url)
    page_product.switch_to_window(1)
    if browser.name == "firefox":
        page = WidgetPage(browser, browser.current_url)
        page.setup_firefox()
        time.sleep(2)
        page.switch_to_window(1)
        page_product.click_on_button_wonderful()
    else:
        page_product.click_on_button_wonderful()


# Как показала практика целесообразно запускать несколько раз его, оставлю значение- 3
# @pytest.mark.parametrize('execution_number', range(3))
@pytest.mark.skip(reason="there is an error")
def test_exact_price_display(browser):
    page_widget = WidgetPage(browser, browser.current_url)
    page_widget.click_on_cross_start_greeting()
    page_product = ProductPage(browser, browser.current_url)
    # Получаем валюту страницы
    currency_page = page_product.get_currency_page()
    page_widget.open_price_widget()
    # открываем настройки
    page_widget.open_price_settings()
    page_setting = SettingsPage(browser, browser.current_url)
    # открываем список валют
    page_setting.open_currency_list()
    # выбираем нужную валюту, передаем через параменты
    page_setting.choose_currency(currency_page)
    page_setting.close_settings()
    time.sleep(0.5)
    # Получаем цену от виджета
    extension_price = page_widget.exact_price()
    # Получаем цену со страницы
    product_page_price = page_product.product_price()
    # print(product_page_price, extension_price)
    assert extension_price == product_page_price, \
        f"Ошибка -> цена: {extension_price} не равна цене: {product_page_price} "


def test_open_dropdown(browser):
    page = WidgetPage(browser, browser.current_url)
    page.click_on_cross_start_greeting()
    page.open_price_widget()
    page.open_price_drop_down_for_3_months()
    # Отображаются ли значения drop-down
    page.should_be_price_drop_down_value()


def test_period_display(browser):
    page = WidgetPage(browser, browser.current_url)
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


@pytest.mark.skip(reason="there is an error")
def test_widget_course_usd_check(browser, directory_name="widget", email=profile["Email"], password=profile["Password"]):
    page_widget = WidgetPage(browser, browser.current_url)
    page_widget.click_on_cross_start_greeting()
    page_product = ProductPage(browser, browser.current_url)
    currency_page = page_product.get_currency_page()
    if currency_page == "RUB":
        price_page = page_product.product_price()
        page_widget.open_price_widget()
        price_widget = page_widget.exact_price()
        course_used = round(price_page / price_widget, 2)
        page_widget.screenshot_page(directory_name)
        aliexpress_global = page_widget.get_usd_course()
        assert course_used == aliexpress_global, \
            f"Курс страницы:{course_used} не равен курсу 'AliExpress Global':{aliexpress_global} "
    else:
        time.sleep(2)
        page_product.log_in_aliexpress(email, password)
        page_product.click_on_cress_repeated_favorites()
        page_product.open_profile()
        page_product.open_regional_settings()
        page_product.country_check()
        page_product.open_regional_currency_list()
        page_product.select_currency("RUB")
        # Сохранение выбранной валюты
        page_product.save_settings()
        time.sleep(2)
        page_product.click_on_logo()
        # Открываем товар из истории с новой уже валютой
        page_widget.open_product_from_history_widget()
        page_widget.switch_to_window(2)
        price_page = page_product.product_price()
        page_widget.open_price_widget()
        price_widget = page_widget.exact_price()
        course_used = round(price_page / price_widget, 2)
        page_widget.screenshot_page(directory_name)
        aliexpress_global = page_widget.get_usd_course()
        assert course_used == aliexpress_global, \
            f"Курс страницы:{course_used} не равен курсу 'AliExpress Global':{aliexpress_global} "


# Готово проверить в новой сборке
def test_different_sku(browser, url=url_sku):
    browser.get(url[0])
    page = WidgetPage(browser, browser.current_url)
    page.page_loading()
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
