import time
import pytest
from .pages.widget_page import WidgetPage
from .pages.product_page import ProductPage
from .pages.setting_page import SettingsPage


url_global = []


@pytest.fixture(scope="function", autouse=True)
def setup(browser):
    url = "https://alitools.io/ru"
    global url_global
    browser.get(url)
    window1 = browser.window_handles
    browser.switch_to.window(window1[1])
    if browser.name == "firefox":
        page = WidgetPage(browser, browser.current_url)
        page.setup_firefox()
        time.sleep(3.5)
        window2 = browser.window_handles
        browser.switch_to.window(window2[1])
        time.sleep(1)
        url_page = browser.current_url
        url_global = url_page.split("/")
        page.should_be_option_start()
        # page_product = ProductPage(browser, browser.current_url)
        # page_product.click_on_button_wonderful()
        time.sleep(1)
        page.click_on_cross_start_greeting()
        time.sleep(0.3)
    else:
        page = WidgetPage(browser, browser.current_url)
        result_warning = page.check_warning_text()
        url_page = browser.current_url
        url_global = url_page.split("/")
        if result_warning is False:
            page.hold_and_move_section_to_down()
            page.should_be_option_start()
            # page_product = ProductPage(browser, browser.current_url)
            # page_product.click_on_button_wonderful()
            time.sleep(0.5)
            page.click_on_cross_start_greeting()
            time.sleep(0.5)
            page.close_warning()
            time.sleep(0.5)
            page.click_on_cress_repeated_favorites()
        else:
            page.should_be_option_start()
            # page_product = ProductPage(browser, browser.current_url)
            # page_product.click_on_button_wonderful()
            time.sleep(1)
            page.click_on_cross_start_greeting()


def test_icon_display_find_on_aliexpress(browser, directory_name="product_page"):
    name = "Icon_find_on_aliexpress"
    page = ProductPage(browser, browser.current_url)
    time.sleep(1)
    page.hover_on_product_main_image(url_global[2])
    page.should_be_icon_find_on_aliexpress()
    time.sleep(0.5)
    page.screenshot_page(directory_name, name)


def test_find_on_aliexpress(browser, directory_name="product_page"):
    name = "Find_on_aliexpress"
    page = ProductPage(browser, browser.current_url)
    time.sleep(1)
    page.hover_on_product_main_image(url_global[2])
    time.sleep(0.5)
    page.hover_on_icon_find_on_aliexpress()
    time.sleep(0.5)
    page.find_on_aliexpress()
    time.sleep(2)
    page.should_be_search_results()
    page.should_be_text_product_search_by_image()
    time.sleep(0.7)
    page.screenshot_page(directory_name, name)


def test_open_find_dropdown(browser, directory_name="product_page"):
    name = "Open_find_dropdown"
    page = ProductPage(browser, browser.current_url)
    time.sleep(1)
    page.hover_on_product_main_image(url_global[2])
    time.sleep(0.5)
    page.hover_on_icon_find_on_aliexpress()
    page.open_drop_down_find_on_aliexpress()
    page.should_be_text_do_not_show()
    page.should_be_text_configure_search()
    page.screenshot_page(directory_name, name)


def test_open_settings_history_from_icon(browser, directory_name="product_page"):
    name = "Open_settings_history_from_icon"
    page = ProductPage(browser, browser.current_url)
    time.sleep(1)
    page.hover_on_product_main_image(url_global[2])
    time.sleep(0.5)
    page.hover_on_icon_find_on_aliexpress()
    page.open_drop_down_find_on_aliexpress()
    page.open_settings_history_from_icon()
    time.sleep(0.2)
    page = SettingsPage(browser, browser.current_url)
    active_tab = page.get_active_tab()
    assert active_tab == "Поиск по картинке", f"Актиавна вкладка: {active_tab}, a не [Поиск по картинке]"
    page.screenshot_page(directory_name, name)

