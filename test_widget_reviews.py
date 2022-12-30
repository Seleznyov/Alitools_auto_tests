import time
import pytest
from .pages.widget_page import WidgetPage
from .pages.product_page import ProductPage
from .settings import url_zero_reviews
import random


@pytest.fixture(scope="function", autouse=True)
def setup(browser):
    url = "https://alitools.io/ru"
    browser.get(url)
    page_product = ProductPage(browser, browser.current_url)
    page_product.switch_to_window(1)
    if browser.name == "firefox":
        page = WidgetPage(browser, browser.current_url)
        page.setup_firefox()
        time.sleep(2)
        page.switch_to_window(1)
        page_product.click_on_button_wonderful()
    else:
        page_product.click_on_button_wonderful()


def test_zero_reviews(browser):
    random_index = random.randrange(len(url_zero_reviews))
    url = url_zero_reviews[random_index]
    browser.get(url)
    page = WidgetPage(browser, browser.current_url)
    page.click_on_cross_start_greeting()
    val_reviews = page.value_reviews()
    assert val_reviews == 0, f"Ошибка -> количество обзоров равно : {val_reviews} a не : '0' "
    page.open_reviews_widget()
    page.should_be_displayed_text()


# Для firefox пока skip а так вроде работает
def test_number_of_reviews(browser):
    if browser.name == "firefox":
        pytest.skip("firefox browser is used")
    # url = "https://aliexpress.ru/item/32910454019.html"
    # url = "https://aliexpress.ru/item/32974708727.html"
    # browser.get(url)
    page = WidgetPage(browser, browser.current_url)
    page.click_on_cross_start_greeting()
    display_quantity_on_widget = page.value_reviews()
    page.open_reviews_widget()
    val_iterations = page.value_iterations()
    page.scroll_reviews(val_iterations)
    quantity_reviews_images = page.value_reviews_images()
    print(display_quantity_on_widget, quantity_reviews_images)
    assert display_quantity_on_widget == quantity_reviews_images, \
        f"Ошибка -> значение количества обзоров виджета : {display_quantity_on_widget} " \
        f"не равно количеству изображений: {quantity_reviews_images} "


def test_open_random_card_of_reviews(browser):
    if browser.name == "firefox":
        pytest.skip("firefox browser is used")
    page = WidgetPage(browser, browser.current_url)
    page.click_on_cross_start_greeting()
    page.open_reviews_widget()
    # Выбор случайного обзора
    random_review = page.choose_random_review()
    # Поиск обзора
    review = page.scroll_to_random_review(random_review)
    time.sleep(0.2)
    # Открыть случайным обзор
    page.open_random_review(review)
    # Проверка что обзор открыт и  отображается
    page.should_be_displayed_overview()
    time.sleep(0.7)
