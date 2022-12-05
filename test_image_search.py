import time
import pytest
from .pages.widget_page import WidgetPage
from .pages.product_page import ProductPage
# from .pages.setting_page import SettingsPage


@pytest.fixture(scope="function", autouse=True)
def setup(browser):
    url = "https://alitools.io/ru"
    browser.get(url)
    window1 = browser.window_handles
    browser.switch_to.window(window1[1])
    if browser.name == "firefox":
        page = WidgetPage(browser, browser.current_url)
        page.setup_firefox()
        window2 = browser.window_handles
        browser.switch_to.window(window2[1])
        time.sleep(2)
        page.should_be_option_start()
        time.sleep(1)
        page.click_on_cross_start_greeting()
        time.sleep(0.3)
    else:
        page = WidgetPage(browser, browser.current_url)
        result_warning = page.check_warning_text()
        if result_warning is False:
            page.hold_and_move_section_to_down()
            page.should_be_option_start()
            time.sleep(0.5)
            page.click_on_cross_start_greeting()
            time.sleep(0.5)
            page.close_warning()
            time.sleep(0.5)
            page.click_on_cress_repeated_favorites()
        else:
            page.should_be_option_start()
            time.sleep(1)
            page.click_on_cross_start_greeting()


def test_icon_display_find_on_aliexpress(browser, directory_name="widget"):
    name = "Icon_find_on_aliexpress"
    page = ProductPage(browser, browser.current_url)
    time.sleep(1)
    page.hover_on_product_main_image()
    page.should_be_icon_find_on_aliexpress()
    time.sleep(0.5)
    page.screenshot_page(directory_name, name)


def test_find_on_aliexpress(browser, directory_name="widget"):
    name = "Find_on_aliexpress"
    page = ProductPage(browser, browser.current_url)
    time.sleep(1)
    page.hover_on_product_main_image()
    time.sleep(0.5)
    page.hover_on_icon_find_on_aliexpress()
    time.sleep(0.5)
    page.find_on_aliexpress()
    time.sleep(2)
    page.should_be_search_results()
    page.should_be_text_product_search_by_image()
    time.sleep(0.5)
    page.screenshot_page(directory_name, name)

