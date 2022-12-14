import time
import pytest
from .pages.widget_page import WidgetPage
from .pages.product_page import ProductPage
from .pages.setting_page import SettingsPage


url_global = []


@pytest.fixture(scope="function", autouse=True)
def setup(browser):
    url = "https://www.google.com/"
    global url_global
    browser.get(url)
    page_product = ProductPage(browser, browser.current_url)
    page_product.switch_to_window(1)
    if browser.name == "firefox":
        page = WidgetPage(browser, browser.current_url)
        page.setup_firefox()
        page.switch_to_window(1)
        page_product.click_on_button_wonderful()
        page.click_on_cross_start_greeting()
        url_global = page.page_domain()
    else:
        page = WidgetPage(browser, browser.current_url)
        result_warning = page.check_warning_text()
        url_global = page.page_domain()
        if result_warning is False:
            page.hold_and_move_section_to_down()
            # page_product = ProductPage(browser, browser.current_url)
            # page_product.click_on_button_wonderful()
            time.sleep(0.5)
            page.click_on_cross_start_greeting()
            time.sleep(0.5)
            page.close_warning()
            page.click_on_cress_repeated_favorites()
        else:
            page_product.click_on_button_wonderful()
            page_product.click_on_cross_start_greeting()


def test_turn_off_button_on_image(browser):
    page_product = ProductPage(browser, browser.current_url)
    time.sleep(1)
    page_product.hover_on_product_main_image(url_global[2])
    page_product.should_be_icon_find_on_aliexpress()
    time.sleep(0.5)
    page_widget = WidgetPage(browser, browser.current_url)
    page_widget.open_price_widget()
    page_widget.open_price_settings()
    page_settings = SettingsPage(browser, browser.current_url)
    page_settings.open_search_by_image_tab_from_widget()
    page_settings.click_on_checkbox_button_on_image()
    page_settings.close_settings()
    time.sleep(1)
    page_widget.close_price_card()
    time.sleep(0.5)
    page_product.hover_on_product_main_image(url_global[2])
    page_product.should_not_be_icon_find_on_aliexpress()


def test_empty_disabled_list_display(browser):
    page_widget = WidgetPage(browser, browser.current_url)
    page_widget.open_price_widget()
    page_widget.open_price_settings()
    page_settings = SettingsPage(browser, browser.current_url)
    page_settings.open_search_by_image_tab_from_widget()
    page_settings.delete_all_site_from_disabled_list()
    page_settings.should_be_text_for_empty_disabled_list()
