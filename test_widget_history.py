import time
import pytest
from .pages.widget_page import WidgetPage
from .settings import url_random_four_product


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
        time.sleep(0.5)
        page.click_on_cross_start_greeting()
    else:
        page = WidgetPage(browser, browser.current_url)
        page.should_be_option_start()
        time.sleep(0.5)
        page.click_on_cross_start_greeting()


@pytest.mark.parametrize('execution_number', range(3))
def test_collapse_and_expand_history(browser, execution_number):
    page = WidgetPage(browser, browser.current_url)
    page.should_be_card_of_product()
    time.sleep(1)
    page.collapse_history()
    time.sleep(0.5)
    page.product_from_history_widget_not_displayed()
    page.expand_history()
    time.sleep(0.5)
    page.product_from_history_widget_displayed()


def test_maximum_number_of_products_in_the_history_widget(browser, list_product=url_random_four_product):
    page = WidgetPage(browser, browser.current_url)
    first_product = page.list_products_from_history_widget()
    page.open_product_list(list_product)
    product_list = page.list_products_from_history_widget()
    page.max_number_of_products_in_history_widget(product_list)
    assert first_product not in product_list, f"Отображаются не последние карточки товаров в истории"

