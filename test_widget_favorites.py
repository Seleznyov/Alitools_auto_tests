import time
import pytest
from .pages.widget_page import WidgetPage
from .pages.product_page import ProductPage


@pytest.fixture(scope="function", autouse=True)
def setup(browser):
    url = "https://www.google.com/"
    browser.get(url)
    page_product = ProductPage(browser, browser.current_url)
    page_product.switch_to_window(1)
    if browser.name == "firefox":
        page = WidgetPage(browser, browser.current_url)
        page.setup_firefox()
        page.switch_to_window(1)
        page_product.click_on_button_wonderful()
        page_product.click_on_cross_start_greeting()
    else:
        page_product.click_on_button_wonderful()
        page_product.click_on_cross_start_greeting()


def test_adding_product_to_favorites_first_time(browser, directory_name="widget"):
    name = "first_time_adding_product_to_favorites"
    page = WidgetPage(browser, browser.current_url)
    page.add_product_to_favorites()
    page.should_be_text_product_added_to_Alitools()
    time.sleep(0.5)
    page.screenshot_page(directory_name, name)


def test_first_adding_to_favorites_through_the_price_widget(browser, directory_name="widget"):
    name = "first_adding_to_favorites_through_the_price_widget"
    page = WidgetPage(browser, browser.current_url)
    page.open_price_widget()
    page.click_on_price_button_follow_the_item()
    page.should_be_text_product_added_to_Alitools()
    time.sleep(0.5)
    page.screenshot_page(directory_name, name)
