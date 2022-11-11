from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from ..settings import currency_processing


class ProductPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(ProductPage, self).__init__(*args, **kwargs)

    # цена продукта на странице магазина али
    def product_price(self):
        # Нужно придумать проверку на валюту товара на странице, передавать в функцию
        product_price = self.browser.find_element(*ProductPageLocators.Product_price).text
        product_price = product_price.partition(',')[0]
        product_price = "".join(c for c in product_price if c.isdecimal())
        return int(product_price)

    def product_price_full(self):
        product_price = self.browser.find_element(*ProductPageLocators.Product_price).text
        product_price = "".join(c for c in product_price if c.isdecimal())
        return int(product_price)

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
        x = 1
        for currency in regional_currency:
            if x == 3:
                regional_currency = currency
                regional_currency.click()
            x += 1

    # Изменить функицю и локатор -> [regional_country_currency_language]
    def open_regional_language_list(self):
        regional_language = self.browser.find_elements(*ProductPageLocators.Regional_country_currency_language)
        x = 1
        for language in regional_language:
            if x == 2:
                regional_currency = language
                regional_currency.click()
            x += 1

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
        product_price = self.browser.find_element(*ProductPageLocators.Product_price).text
        for currency in currency_processing:
            if currency in product_price:
                value = currency_processing[currency]
                return value
