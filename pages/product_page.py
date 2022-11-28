import time
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from ..settings import currency_processing


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
        if value_country != "Беларусь":
            regional_country = self.browser.find_elements(*ProductPageLocators.Regional_country_currency_language)
            regional_country = regional_country[0]
            regional_country.click()
            time.sleep(1)
            country_bel = self.browser.find_element(*ProductPageLocators.Regional_country_BEL)
            country_bel.click()
            time.sleep(1)

    def select_currency(self, currency):
        # Подумать как улучшить эту функцию
        # get_regional_currency_list = self.browser.find_elements(*ProductPageLocators.Regional_currency_list)
        if currency == "USD":
            currency = self.browser.find_element(*ProductPageLocators.Regional_currency_USD)
            actions = ActionChains(self.browser)
            actions.move_to_element(currency).perform()
            currency.click()
        elif currency == "RUB":
            currency = self.browser.find_element(*ProductPageLocators.Regional_currency_RUB)
            actions = ActionChains(self.browser)
            actions.move_to_element(currency).perform()
            currency.click()
        elif currency == "EUR":
            currency = self.browser.find_element(*ProductPageLocators.Regional_currency_EUR)
            actions = ActionChains(self.browser)
            actions.move_to_element(currency).perform()
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
        button_wonderful = self.browser.find_element(*ProductPageLocators.Button_wonderful)
        button_wonderful.click()
