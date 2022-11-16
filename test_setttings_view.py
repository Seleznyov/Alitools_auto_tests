import time

import pytest
from .pages.setting_page import SettingsPage
from .settings import extension


@pytest.fixture(scope="function", autouse=True)
def setup(browser):
    url = "https://alitools.io/ru"
    browser.get(url)
    window1 = browser.window_handles
    browser.switch_to.window(window1[1])


def test_general_tab_view(browser, ID=extension["id"]):
    url = f"chrome-extension://{ID}/settings.html"
    browser.get(url)
    page = SettingsPage(browser, browser.current_url)
    page.should_be_languages_text()
    page.should_be_languages_list()
    page.should_be_currency_text()
    page.should_be_currency_list()
    page.should_be_button_cross()
    page.should_be_extension_text()
    page.should_be_checkbox_seller_verification()
    page.should_be_notifications_text()
    # Проверка активен ли чекбокс "Счетчик уведомлений на иконке расширения"
    page.checkbox_notification_counter_should_be_on()
    page.should_be_checkbox_notification_counter()
    # Проверка активен ли чекбокс "Пуш-уведомления о падении цен на товары"
    page.checkbox_push_notifications_should_be_on()
    page.should_be_checkbox_push_notifications()
    page.should_be_message_describing_the_fall()
    page.should_be_text_color_scheme()
    page.should_be_light_theme()
    # Проверка что светлая тема активна
    page.light_theme_should_be_on()
    page.should_be_dark_theme()
    page.should_be_extension_version()
    time.sleep(1)


def test_image_search_tab_view(browser):
    pass


def test_adviser_tab_view(browser):
    pass


def test_history_tab_view(browser):
    pass

def test_synchronization_tab_view(browser):
    pass
