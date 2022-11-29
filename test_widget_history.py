import time
import pytest
from .pages.widget_page import WidgetPage


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
        time.sleep(1)
        page.should_be_option_start()
        page.click_on_cross_start_greeting()
    else:
        page = WidgetPage(browser, browser.current_url)
        page.should_be_option_start()
        page.click_on_cross_start_greeting()


def test_collapse_and_expand_history(browser):
    page = WidgetPage(browser, browser.current_url)
    page.should_be_card_of_product()
    time.sleep(1)
    page.collapse_history()
    time.sleep(0.5)
    page.product_from_history_widget_not_displayed()
    page.expand_history()
    time.sleep(0.5)
    page.product_from_history_widget_displayed()

