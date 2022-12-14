import pytest
from .pages.widget_page import WidgetPage
from .pages.product_page import ProductPage
from .settings import url_seller_rating


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
    else:
        page_product.click_on_button_wonderful()


def test_seller_display_the_same_rating(browser):
    page = WidgetPage(browser, browser.current_url)
    page.click_on_cross_start_greeting()
    percentage_value_widget = page.get_percentage_value()
    page.open_seller_widget()
    percentage_value_inside_the_card = page.get_percentage_value_inside_the_card()
    # print(percentage_value_widget, percentage_value_inside_the_card)
    assert percentage_value_widget == percentage_value_inside_the_card, \
        f"Ошибка значение % виджета{percentage_value_widget} не равно значению % {percentage_value_inside_the_card} "


@pytest.mark.parametrize('url_test', url_seller_rating)
def test_seller_rating(browser, url_test):
    url = url_seller_rating[url_test]
    browser.get("https://www.aliexpress.com/item/" + url)
    page = WidgetPage(browser, browser.current_url)
    page.click_on_cross_start_greeting()
    page.open_seller_widget()
    # Проверка рейтинга продавца на соответствие критериям %
    page.check_rating_seller()
