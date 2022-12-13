import time
from .base_page import BasePage
from .locators import ProductPageLocators
# import pytest
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from ..settings import currency_processing
import random


class ProductPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(ProductPage, self).__init__(*args, **kwargs)

    # цена продукта на странице магазина али
    def product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.Product_price).text
        product_price = product_price.translate({ord(i): None for i in ' руб.$€¥US'})
        product_price = product_price.replace(",", ".")
        return float(product_price)

    def open_profile(self):
        icon_login = self.browser.find_element(*ProductPageLocators.Icon_login)
        icon_login.click()

    def log_in_aliexpress(self, email, password):
        icon_login = self.browser.find_element(*ProductPageLocators.Icon_login)
        icon_login.click()
        email_input = self.browser.find_element(*ProductPageLocators.Email_input)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*ProductPageLocators.Password_input)
        password_input.send_keys(password)
        button_login = self.browser.find_element(*ProductPageLocators.Button_login)
        button_login.click()

    def open_regional_settings(self):
        regional_settings = self.browser.find_element(*ProductPageLocators.Regional_settings)
        regional_settings.click()

    # Изменить функицю и локатор -> [regional_country_currency_language]
    def open_regional_currency_list(self):
        regional_currency = self.browser.find_elements(*ProductPageLocators.Regional_country_currency_language)
        regional_currency = regional_currency[2]
        regional_currency.click()

    # Изменить функицю и локатор -> [regional_country_currency_language]
    def open_regional_language_list(self):
        regional_language = self.browser.find_elements(*ProductPageLocators.Regional_country_currency_language)
        regional_language = regional_language[1]
        regional_language.click()

    def country_check(self):
        values_country = self.browser.find_elements(*ProductPageLocators.Value_country)
        value_country = values_country[0].get_attribute("value")
        if value_country != "BY":
            regional_country = self.browser.find_elements(*ProductPageLocators.Regional_country_currency_language)
            regional_country = regional_country[0]
            regional_country.click()
            time.sleep(1)
            country_bel = self.browser.find_element(*ProductPageLocators.Regional_country_BEL)
            country_bel.click()
            time.sleep(1)

    # Подумать как улучшить эту функцию
    def select_currency(self, currency):
        get_regional_currency_list = self.browser.find_elements(*ProductPageLocators.Regional_currency_list)
        if currency == "USD":
            currency = get_regional_currency_list[139]
            # currency = self.browser.find_element(*ProductPageLocators.Regional_currency_USD)
            # actions = ActionChains(self.browser)
            # actions.move_to_element(currency).perform()
            currency.click()
        elif currency == "RUB":
            currency = get_regional_currency_list[68]
            # currency = self.browser.find_element(*ProductPageLocators.Regional_currency_RUB)
            # actions = ActionChains(self.browser)
            # actions.move_to_element(currency).perform()
            currency.click()
        elif currency == "EUR":
            currency = get_regional_currency_list[36]
            # currency = self.browser.find_element(*ProductPageLocators.Regional_currency_EUR)
            # actions = ActionChains(self.browser)
            # actions.move_to_element(currency).perform()
            currency.click()

    def save_settings(self):
        save_settings_button = self.browser.find_element(*ProductPageLocators.Save_settings_button)
        save_settings_button.click()

    def click_on_logo(self):
        logo = self.browser.find_element(*ProductPageLocators.Logo_link)
        logo.click()

    # Определяем валюту старницы
    def get_currency_page(self):
        product_price = self.browser.find_elements(*ProductPageLocators.Product_price)
        for currency in currency_processing:
            if currency in product_price[0].text:
                value = currency_processing[currency]
                return value

    # Возвращает активное  Sku страницы
    def get_active_sku(self):
        product_sku = self.browser.find_elements(*ProductPageLocators.Product_sku_picture)
        for i in range(len(product_sku)):
            if "active" in product_sku[i].get_attribute("class"):
                return i

    # Выбирает следущую sku
    def select_next_sku(self, index):
        product_sku = self.browser.find_elements(*ProductPageLocators.Product_sku_picture)
        next_sku = product_sku[index+1]
        next_sku.click()


    def should_be_seller_trust_level_title(self):
        title = self.browser.find_element(*ProductPageLocators.Seller_trust_level_title)
        assert title, "title is not presented "

    def should_not_be_seller_trust_level_title(self):
        assert self.is_not_element_present(*ProductPageLocators.Seller_trust_level_title), "title is presented"

    def scroll_to_text_delivery_and_returns(self):
        delivery_and_returns = self.browser.find_element(*ProductPageLocators.Delivery_and_returns)
        if self.browser.name == "firefox":
            self.browser.execute_script("arguments[0].scrollIntoView(true);", delivery_and_returns)
        else:
            scroll_origin = ScrollOrigin.from_element(delivery_and_returns)
            ActionChains(self.browser).scroll_from_origin(scroll_origin, 0, 500).perform()

    def click_on_button_wonderful(self):
        # try:
        #     WebDriverWait(self.browser, 20).until(
        #         EC.presence_of_element_located((By.XPATH, "//div[@class='snow-ali-kit_Informer__flexAligner__8lq3ka']/button")))
        # except TimeoutException:
        #     pytest.skip("Не успел отобразиться элемент")
        button_wonderful = self.browser.find_element(*ProductPageLocators.Button_wonderful)
        button_wonderful.click()

    def hover_on_product_main_image(self, url="ru"):
        for i in range(len(url)):
            if "aliexpress.com" in url[i] or "aliexpress.us" in url[i]:
                product_image = self.browser.find_element(*ProductPageLocators.Product_image_com)
                action = ActionChains(self.browser)
                action.move_to_element(product_image)
                action.perform()
                action.move_to_element(product_image)
                action.perform()
                break
            elif "sportmaster" in url[i]:
                product_image = self.browser.find_elements(*ProductPageLocators.Product_image_from_sportmaster)
                product_image = product_image[0]
                action = ActionChains(self.browser)
                action.move_to_element(product_image)
                action.perform()
                action.move_to_element(product_image)
                action.perform()
                break
            elif "svyaznoy" in url[i]:
                product_image = self.browser.find_element(*ProductPageLocators.Product_image_from_svyaznoy)
                self.browser.execute_script("arguments[0].scrollIntoView(true);", product_image)
                action = ActionChains(self.browser)
                action.move_to_element(product_image)
                action.perform()
                action.move_to_element(product_image)
                action.perform()
                break
            elif "mvideo" in url[i]:
                product_image = self.browser.find_element(*ProductPageLocators.Product_image_from_mvideo)
                action = ActionChains(self.browser)
                action.move_to_element(product_image)
                action.perform()
                action.move_to_element(product_image)
                action.perform()
                break
            else:
                if i == len(url) - 1:
                    product_image = self.browser.find_element(*ProductPageLocators.Product_image)
                    action = ActionChains(self.browser)
                    action.move_to_element(product_image)
                    action.perform()
                    action.move_to_element(product_image)
                    action.perform()

    def should_be_icon_find_on_aliexpress(self):
        icon = self.is_element_present(*ProductPageLocators.Find_on_aliexpress_icon)
        assert icon, f"Иконка не отображается"

    def should_not_be_icon_find_on_aliexpress(self):
        icon = self.is_not_element_present(*ProductPageLocators.Find_on_aliexpress_icon)
        assert icon, f"Иконка отображается"

    def hover_on_icon_find_on_aliexpress(self):
        icon = self.browser.find_element(*ProductPageLocators.Find_on_aliexpress_icon)
        action = ActionChains(self.browser)
        action.move_to_element(icon)
        action.perform()

    def find_on_aliexpress(self):
        find_on_aliexpress_button = self.browser.find_element(*ProductPageLocators.Find_on_aliexpress_button)
        find_on_aliexpress_button.click()

    def should_be_text_product_search_by_image(self):
        text = self.browser.find_element(*ProductPageLocators.Product_search_by_image_text).text
        assert text == "Поиск товара по картинке", f"Текст {text} не отображается"

    def should_be_search_results(self):
        result = self.is_element_present(*ProductPageLocators.Image_search_result)
        assert result, f"Результат поиска не отображается"

    def open_drop_down_find_on_aliexpress(self):
        drop_down = self.browser.find_element(*ProductPageLocators.Find_on_aliexpress_drop_down)
        drop_down.click()

    def should_be_text_do_not_show(self):
        texts = self.browser.find_elements(*ProductPageLocators.Find_on_aliexpress_drop_down_values)
        text_do_not_show = texts[0].text
        assert text_do_not_show == "Не показывать на этом сайте", f"Отображается текст: {text_do_not_show} "

    def should_be_text_configure_search(self):
        texts = self.browser.find_elements(*ProductPageLocators.Find_on_aliexpress_drop_down_values)
        text_configure_search = texts[1].text
        assert text_configure_search == "Настроить поиск по картинке", f"Отображается текст: {text_configure_search} "

    def open_settings_history_from_icon(self):
        buttons = self.browser.find_elements(*ProductPageLocators.Find_on_aliexpress_drop_down_values)
        configure_search_button = buttons[1]
        configure_search_button.click()

    def disable_image_search_from_the_page(self):
        buttons = self.browser.find_elements(*ProductPageLocators.Find_on_aliexpress_drop_down_values)
        disable_image_search_button = buttons[0]
        disable_image_search_button.click()

    def open_randon_site(self, random_list):
        random_list = list(random_list.values())
        random_index = random.randrange(len(random_list))
        random_site = random_list[random_index]
        self.browser.get(random_site)

