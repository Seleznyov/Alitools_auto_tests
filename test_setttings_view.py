import time

import pytest
from .pages.setting_page import SettingsPage
from .settings import extension, disabled_site_list,setting_tabs

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
    active_tab = page.get_active_tab()
    assert active_tab == setting_tabs[0], f"Активна вкладка {active_tab}, а не {setting_tabs[0]}"
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
    page.should_be_extension_version(active_tab)
    time.sleep(1)


def test_image_search_tab_view(browser, ID=extension["id"]):
    url = f"chrome-extension://{ID}/settings.html"
    browser.get(url)
    page = SettingsPage(browser, browser.current_url)
    active_tab = page.get_active_tab()
    assert active_tab == setting_tabs[0], f"Активна вкладка {active_tab}, а не {setting_tabs[0]}"
    page.open_search_by_image_tab()
    time.sleep(1)
    active_tab = page.get_active_tab()
    assert active_tab == setting_tabs[1], f"Активна вкладка {active_tab}, а не {setting_tabs[1]}"
    active_tab = page.get_active_tab()
    page.should_be_button_on_the_picture()
    # Проверка активен ли чекбокс "Кнопка на картинках"
    page.checkbox_button_on_the_picture_should_be_on()
    page.should_be_sites_with_disabled_button()
    list_disabled_site = page.get_list_disabled_site()
    assert list_disabled_site == disabled_site_list, f" 'Список расширения': {list_disabled_site} не равен 'эталонному списку': {disabled_site_list}. "
    page.should_be_extension_version(active_tab)
    time.sleep(1)


def test_adviser_tab_view(browser, ID=extension["id"]):
    url = f"chrome-extension://{ID}/settings.html"
    browser.get(url)
    page = SettingsPage(browser, browser.current_url)
    active_tab = page.get_active_tab()
    assert active_tab == setting_tabs[0], f"Активна вкладка {active_tab}, а не {setting_tabs[0]}"
    page.open_adviser_tab()
    time.sleep(1)
    active_tab = page.get_active_tab()
    assert active_tab == setting_tabs[2], f"Активна вкладка {active_tab}, а не {setting_tabs[2]}"
    page.should_be_block_show_offers()
    # Проверка активен ли чекбокс "Показывать предложения с AliExpress на сайтах других магазинов"
    page.checkbox_show_offers_should_be_on()
    page.should_be_block_sites_with_disabled_adviser()
    page.should_be_block_text_if_you_disable_the_widget()
    page.should_be_extension_version(active_tab)
    time.sleep(1)


def test_history_tab_view(browser):
    pass

def test_synchronization_tab_view(browser):
    pass
