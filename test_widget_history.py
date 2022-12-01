import time
import pytest
from .pages.widget_page import WidgetPage
from .pages.setting_page import SettingsPage
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
        time.sleep(0.5)
        page.should_be_option_start()
        time.sleep(1.5)
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
            time.sleep(0.5)
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
    page = WidgetPage(browser, browser.current_url)
    page.open_history_widget()
    page.open_history_widget_context_menu()
    page.open_history_settings()
    time.sleep(0.2)
    page = SettingsPage(browser, browser.current_url)
    active_tab = page.get_active_tab()
    assert active_tab == "История", f"Актиавна вкладка: {active_tab}, a не [История]"

