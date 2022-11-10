from .base_page import BasePage
from .locators import SettingsLocators
from selenium.webdriver.common.by import By


class SettingsPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(SettingsPage, self).__init__(*args, **kwargs)

    def open_currency_list(self):
        currency_list = self.browser.find_element(*SettingsLocators.Currency_list)
        currency_list.click()

    def get_languages_list(self):
        languages_list = []
        Languages_list_option = self.browser.find_elements(*SettingsLocators.Languages_list_option)
        for language in Languages_list_option:
            languages_list.append(language.get_attribute('value'))
        return languages_list

    def get_currency_list(self):
        currency_list = []
        Currency_list_option = self.browser.find_elements(*SettingsLocators.Currency_list_option)
        for currency in Currency_list_option:
            currency_list.append(currency.get_attribute('value'))
        return currency_list

    def choose_currency(self, curr):
        Currency_list_option = self.browser.find_elements(*SettingsLocators.Currency_list_option)
        r = 1
        for value in Currency_list_option:
            if value.get_attribute('value') == curr:
                currency = self.browser.find_element(By.XPATH, SettingsLocators.option_currency + str([r]))
                currency.click()
            r += 1

    def close_settings(self):
        settings_button_cross = self.browser.find_element(*SettingsLocators.Settings_button_cross)
        settings_button_cross.click()
