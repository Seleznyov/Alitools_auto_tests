import time
import pytest
from .pages.widget_page import WidgetPage
from .pages.product_page import ProductPage
from .pages.setting_page import SettingsPage
from .settings import currency_list, language


@pytest.fixture(scope="function", autouse=True)
def setup(browser):
    url = "https://alitools.io/ru"
    browser.get(url)
    page_product = ProductPage(browser, browser.current_url)
    page_product.switch_to_window(1)
    if browser.name == "firefox":
        page = WidgetPage(browser, browser.current_url)
        page.setup_firefox()
        page_product.switch_to_window(1)
        time.sleep(1)


def test_displaying_a_list_of_languages(browser):
    page = WidgetPage(browser, browser.current_url)
    page.should_be_option_start()
    page.click_on_cross_start_greeting()
    page.open_price_widget()
    # открываем настройки
    page.open_price_settings()
    page = SettingsPage(browser, browser.current_url)
    list_of_extension = page.get_languages_list()
    # сравниваем списки
    assert list_of_extension == language, \
        f" 'Список расширения': {list_of_extension} не равен 'эталонному списку': {language}. "


def test_displaying_a_list_of_currency(browser):
    page = WidgetPage(browser, browser.current_url)
    page.should_be_option_start()
    page.click_on_cross_start_greeting()
    page.open_price_widget()
    # открываем настройки
    page.open_price_settings()
    page = SettingsPage(browser, browser.current_url)
    list_of_extension = page.get_currency_list()
    # сравниваем списки
    assert list_of_extension == currency_list, \
        f" 'Список расширения': {list_of_extension} не равен 'эталонному списку': {currency_list}. "


def test_theme_change(browser, directory_name="settings"):
    page = WidgetPage(browser, browser.current_url)
    page.should_be_option_start()
    page.click_on_cross_start_greeting()
    page.open_price_widget()
    page.open_price_settings()
    page = SettingsPage(browser, browser.current_url)
    page.choose_dark_theme()
    page.should_be_dark_theme_active()
    page.scroll_to_general_settings()
    time.sleep(0.5)
    page.screenshot_page(directory_name)


def test_turn_on_seller_trust_level(browser):
    page_widget = WidgetPage(browser, browser.current_url)
    page_widget.should_be_option_start()
    page_widget.click_on_cross_start_greeting()
    page_product = ProductPage(browser, browser.current_url)
    time.sleep(0.7)
    page_product.scroll_to_text_delivery_and_returns()
    page_product.should_not_be_seller_trust_level_title()
    time.sleep(0.7)
    page_widget.open_price_widget()
    page_widget.open_price_settings()
    page_settings = SettingsPage(browser, browser.current_url)
    page_settings.turn_on_widget_checkbox_seller_verification()
    page_settings.close_settings()
    time.sleep(1)
    page_widget.close_price_card()
    page_product.should_be_seller_trust_level_title()


@pytest.mark.parametrize('languages', language)
def test_language_change(browser, languages):
    page_widget = WidgetPage(browser, browser.current_url)
    page_widget.should_be_option_start()
    page_widget.click_on_cross_start_greeting()
    page_widget.open_price_widget()
    page_widget.open_price_settings()
    page = SettingsPage(browser, browser.current_url)
    page.open_language_list()
    page.choose_language(languages)
    page.translation_check_for_settings(languages)
    time.sleep(0.7)
    page.close_settings()
    time.sleep(0.5)
    page_widget.close_price_card()
    page_widget.translation_check_for_widget(languages)
    time.sleep(0.5)
