import time
import pytest
from .pages.widget_page import WidgetPage
from .pages.product_page import ProductPage
from .pages.setting_page import SettingsPage
from .settings import sites_active


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
            page.click_on_cross_start_greeting()
            time.sleep(0.5)
            page.close_warning()
            time.sleep(0.5)
            page.click_on_cress_repeated_favorites()
        else:
            page_product.click_on_button_wonderful()
            page_product.click_on_cross_start_greeting()


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


def test_disable_image_search_for_aliexpress(browser):
    page_product = ProductPage(browser, browser.current_url)
    time.sleep(1)
    page_product.hover_on_product_main_image(url_global[2])
    time.sleep(0.5)
    page_product.hover_on_icon_find_on_aliexpress()
    page_product.open_drop_down_find_on_aliexpress()
    page_product.disable_image_search_from_the_page()
    page_product.hover_on_product_main_image(url_global[2])
    page_product.should_not_be_icon_find_on_aliexpress()
    page_widget = WidgetPage(browser, browser.current_url)
    page_widget.open_history_widget()
    page_widget.open_history_widget_context_menu()
    page_widget.open_history_settings()
    page_settings = SettingsPage(browser, browser.current_url)
    time.sleep(0.2)
    page_settings.open_search_by_image_tab_from_widget()
    time.sleep(0.2)
    list_disabled_site = page_settings.get_list_disabled_site_from_widget()
    list_without_dots = page_widget.cleared_list(list_disabled_site)
    assert "aliexpress" in list_without_dots, f"Сайт: 'aliexpress' не был добавлен в исключение"


def test_image_search_on_a_random_site(browser, sites_act=sites_active):
    if browser.name == "firefox":
        pytest.skip(reason="For browser firefox this test skip")
    page = ProductPage(browser, browser.current_url)
    page.open_randon_site(sites_act)
    time.sleep(1)
    url = page.page_domain()
    page.hover_on_product_main_image(url)
    time.sleep(0.5)
    page.hover_on_icon_find_on_aliexpress()
    time.sleep(0.5)
    page.find_on_aliexpress()
    page.should_be_search_results()
    page.should_be_text_product_search_by_image()
