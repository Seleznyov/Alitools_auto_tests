import time

import pytest
from .pages.widget_page import WidgetPage
from .pages.setting_page import SettingsPage
from .settings import currency_list, language


@pytest.fixture(scope="function", autouse=True)
def setup(browser):
    url = "https://alitools.io/ru"
    browser.get(url)
    window1 = browser.window_handles
    browser.switch_to.window(window1[1])


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
    assert list_of_extension == language, f" 'Список расширения': {list_of_extension} не равен 'эталонному списку': {language}. "


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
    assert list_of_extension == currency_list, f" 'Список расширения': {list_of_extension} не равен 'эталонному списку': {currency_list}. "