import time
import pytest
from .pages.widget_page import WidgetPage
from .pages.product_page import ProductPage
from .pages.setting_page import SettingsPage
from .settings import currency_list, languages, currency_symbol


@pytest.fixture(scope="function", autouse=True)
def setup(browser):
    url = "https://www.google.com/"
    browser.get(url)
    page_product = ProductPage(browser, browser.current_url)
    page_product.switch_to_window(1)
    if browser.name == "firefox":
        page = WidgetPage(browser, browser.current_url)
        page.setup_firefox()
        page_product.switch_to_window(1)
        page_product.click_on_button_wonderful()
    else:
        page_product.click_on_button_wonderful()
        

def test_displaying_a_list_of_languages(browser):
    page_widget = WidgetPage(browser, browser.current_url)
    page_widget.click_on_cross_start_greeting()
    page_widget.open_price_widget()
    # открываем настройки
    page_widget.open_price_settings()
    page_settings = SettingsPage(browser, browser.current_url)
    list_of_extension = page_settings.get_languages_list()
    # сравниваем списки
    assert list_of_extension == languages, \
        f" 'Список расширения': {list_of_extension} не равен 'эталонному списку': {languages}. "


def test_displaying_a_list_of_currency(browser):
    page_widget = WidgetPage(browser, browser.current_url)
    page_widget.click_on_cross_start_greeting()
    page_widget.open_price_widget()
    # открываем настройки
    page_widget.open_price_settings()
    page_settings = SettingsPage(browser, browser.current_url)
    list_of_extension = page_settings.get_currency_list()
    # сравниваем списки
    assert list_of_extension == currency_list, \
        f" 'Список расширения': {list_of_extension} не равен 'эталонному списку': {currency_list}. "


def test_theme_change(browser, directory_name="settings"):
    page_widget = WidgetPage(browser, browser.current_url)
    page_widget.click_on_cross_start_greeting()
    page_widget.open_price_widget()
    page_widget.open_price_settings()
    page_settings = SettingsPage(browser, browser.current_url)
    page_settings.choose_dark_theme()
    page_settings.should_be_dark_theme_active()
    page_settings.scroll_to_general_settings()
    time.sleep(0.5)
    page_settings.screenshot_page(directory_name)


def test_turn_on_seller_trust_level(browser):
    page_widget = WidgetPage(browser, browser.current_url)
    page_widget.click_on_cross_start_greeting()
    page_product = ProductPage(browser, browser.current_url)
    time.sleep(0.7)
    page_product.scroll_to_text_delivery_and_returns()
    page_product.should_not_be_seller_trust_level_title()
    page_widget.open_price_widget()
    page_widget.open_price_settings()
    page_settings = SettingsPage(browser, browser.current_url)
    page_settings.turn_on_widget_checkbox_seller_verification()
    page_settings.close_settings()
    page_widget.close_price_card()
    page_product.should_be_seller_trust_level_title()


@pytest.mark.parametrize('language', languages)
def test_language_change(browser, language):
    page_widget = WidgetPage(browser, browser.current_url)
    page_widget.click_on_cross_start_greeting()
    page_widget.open_price_widget()
    page_widget.open_price_settings()
    page_settings = SettingsPage(browser, browser.current_url)
    page_settings.open_language_list()
    page_settings.choose_language(language)
    page_settings.translation_check_for_settings(language)
    page_settings.close_settings()
    time.sleep(0.5)
    page_widget.close_price_card()
    page_widget.translation_check_for_widget(language)


@pytest.mark.parametrize('currency', ["USD", "EUR", "RUB", "UAH", "PLN", "GBP", "BRL", "CAD", "SGD",
                                      pytest.param("NZD", marks=pytest.mark.skip), "AUD", "INR", "JPY",
                         pytest.param("MXN", marks=pytest.mark.skip),
                         pytest.param("IDR", marks=pytest.mark.skip), "TRY", "KRW", "SEK",
                         pytest.param("CLP", marks=pytest.mark.skip), "CHF"])
def test_currency_change(browser, currency):
    page_widget = WidgetPage(browser, browser.current_url)
    page_widget.click_on_cross_start_greeting()
    page_widget.open_price_widget()
    page_widget.open_price_settings()
    page_settings = SettingsPage(browser, browser.current_url)
    page_settings.choose_currency(currency)
    page_settings.close_settings()
    symbol_from_page = page_widget.get_value_symbol()
    # Проверить, что символ действительно соответствует валюте
    page_widget.check_currency_symbol(currency_symbol, currency, symbol_from_page)

