import time
import pytest
from .pages.widget_page import WidgetPage
from .pages.product_page import ProductPage
from .pages.setting_page import SettingsPage
from .settings import sites_active, extension

warning = False
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
        page_product.switch_to_window(1)
        page_product.click_on_button_wonderful()
        page.click_on_cross_start_greeting()
        url_global = page.page_domain()
    else:
        page = WidgetPage(browser, browser.current_url)
        result_warning = page.check_warning_text()
        url_global = page.page_domain()
        if result_warning is False:
            global warning
            warning = True
            page.hold_and_move_section_to_down()
            page.click_on_cross_start_greeting()
            time.sleep(0.5)
            page.close_warning()
            page.click_on_cress_repeated_favorites()
        else:
            page_product.click_on_button_wonderful()
            page_product.click_on_cross_start_greeting()


def test_add_aliexpress_to_exclusions(browser):
    page_widget = WidgetPage(browser, browser.current_url)
    page_widget.open_history_widget()
    page_widget.open_history_widget_context_menu()
    page_widget.do_not_show_history_on_this_site()
    page_widget.open_price_widget()
    page_widget.open_price_settings()
    page_settings = SettingsPage(browser, browser.current_url)
    page_settings.open_tab_history()
    site_name = page_settings.get_list_site_names_with_disabled_history()
    assert "aliexpress" in site_name, f"aliexpress не был добавлен в исключение, вернулся: {site_name}"


#Нужно знать extension_id подкидывать его на лету - нужно обойти cloudflare
@pytest.mark.skip(reason="В проде скипать")
def test_add_random_site_to_exclusions(browser, sites_act=sites_active, ID=extension["id"]):
    if browser.name == "firefox":
        pytest.skip(reason="For browser firefox this test skip")
    name_site = "mvideo"
    browser.get(sites_act[name_site])
    page_widget = WidgetPage(browser, browser.current_url)
    # Ждем загрузку страницы
    page_widget.page_loading()
    page_widget.open_history_widget()
    page_widget.open_history_widget_context_menu()
    page_widget.do_not_show_history_on_this_site()
    url = f"chrome-extension://{ID}/settings.html"
    browser.get(url)
    page_settings = SettingsPage(browser, browser.current_url)
    page_settings.open_tab_history()
    site_name = page_settings.get_list_site_names_with_disabled_history()
    assert name_site in site_name, f"{name_site} не был добавлен в исключение, вернулся: {site_name}"
