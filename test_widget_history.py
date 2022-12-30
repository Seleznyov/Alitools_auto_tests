import time
import pytest
from .pages.widget_page import WidgetPage
from .pages.setting_page import SettingsPage
from .pages.product_page import ProductPage
from .settings import url_random_four_product

warning = False
url_global = []


@pytest.fixture(scope="function", autouse=True)
def setup(browser):
    url = "https://alitools.io/ru"
    global url_global
    browser.get(url)
    page_product = ProductPage(browser, browser.current_url)
    page_product.switch_to_window(1)
    if browser.name == "firefox":
        page = WidgetPage(browser, browser.current_url)
        page.setup_firefox()
        time.sleep(2)
        page_product.switch_to_window(1)
        page_product.click_on_button_wonderful()
        page.click_on_cross_start_greeting()
        url_global = page.page_domain()
        time.sleep(1)
    else:
        page = WidgetPage(browser, browser.current_url)
        result_warning = page.check_warning_text()
        url_global = page.page_domain()
        if result_warning is False:
            global warning
            warning = True
            page.hold_and_move_section_to_down()
            time.sleep(0.5)
            page.click_on_cross_start_greeting()
            time.sleep(0.5)
            page.close_warning()
            time.sleep(0.5)
            page.click_on_cress_repeated_favorites()
        else:
            page_product.click_on_button_wonderful()
            page.click_on_cross_start_greeting()


# @pytest.mark.parametrize('execution_number', range(3))
def test_collapse_and_expand_history(browser):
    page = WidgetPage(browser, browser.current_url)
    page.should_be_card_of_product()
    page.collapse_history()
    time.sleep(0.3)
    page.product_from_history_widget_not_displayed()
    page.expand_history()
    time.sleep(0.3)
    page.product_from_history_widget_displayed()


def test_maximum_number_of_products_in_the_history_widget(browser, list_product=url_random_four_product):
    page = WidgetPage(browser, browser.current_url)
    first_product = page.list_products_from_history_widget()
    page.open_product_list(list_product)
    product_list = page.list_products_from_history_widget()
    page.max_number_of_products_in_history_widget(product_list)
    assert first_product not in product_list, f"Отображаются не последние карточки товаров в истории"


def test_deleting_product_card_from_the_history(browser):
    page = WidgetPage(browser, browser.current_url)
    page.open_history_widget()
    page.hover_on_product_card()
    page.should_be_button_cross()
    page.remove_product_card_from_history()
    page.should_be_empty_text()


def test_open_settings_history(browser):
    page_widget = WidgetPage(browser, browser.current_url)
    page_widget.open_history_widget()
    page_widget.open_history_widget_context_menu()
    page_widget.open_history_settings()
    time.sleep(0.2)
    page_setting = SettingsPage(browser, browser.current_url)
    active_tab = page_setting.get_active_tab()
    assert active_tab == "История", f"Актиавна вкладка: {active_tab}, a не [История]"


def test_do_not_show_on_this_site(browser):
    page = WidgetPage(browser, browser.current_url)
    page.open_history_widget()
    page.open_history_widget_context_menu()
    page.do_not_show_history_on_this_site()
    page.not_should_be_history_widget_button()


def test_open_product_card_from_widget_history(browser):
    if "com" in url_global[2] or "us" in url_global[2]:
        pytest.skip("For com. and us. this test skip")
    page = WidgetPage(browser, browser.current_url)
    time.sleep(0.5)
    page.open_product_from_history_widget()
    time.sleep(0.5)
    page.switch_to_window(2)
    if warning is False:
        page.click_on_cress_repeated_favorites()
    product_url_from_widget = page.list_products_from_history_widget()
    product_url_from_current_page = browser.current_url
    # Тут проверка, что наш товар открылся
    assert product_url_from_current_page.split('?')[0] == product_url_from_widget[0], f"URL не совподает"
    time.sleep(0.2)
    page.open_history_widget()
    time.sleep(0.2)
    page.open_product_from_card_of_widget_history()
    time.sleep(0.5)
    window2 = browser.window_handles
    browser.switch_to.window(window2[3])
    # Тут проверка, что наш товар открылся
    assert product_url_from_current_page.split('?')[0] == product_url_from_widget[0], f"URL не совподает"
