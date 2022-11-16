from .base_page import BasePage
from .locators import SettingsLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin


class SettingsPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(SettingsPage, self).__init__(*args, **kwargs)

    def open_currency_list(self):
        currency_list = self.browser.find_element(*SettingsLocators.Widget_settings_currency_list)
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
        settings_button_cross = self.browser.find_element(*SettingsLocators.Widget_settings_button_cross)
        settings_button_cross.click()

    def should_be_languages_text(self):
        assert self.is_element_present(*SettingsLocators.Languages_text), "element is not presented"

    def should_be_languages_list(self):
        assert self.is_element_present(*SettingsLocators.Settings_languages_list), "list of languages is not presented"

    def should_be_currency_text(self):
        assert self.is_element_present(*SettingsLocators.Currency_text), "element is not presented"

    def should_be_currency_list(self):
        assert self.is_element_present(*SettingsLocators.Settings_currency_list), "Currency_list is not presented"

    def should_be_button_cross(self):
        assert self.is_element_present(*SettingsLocators.Settings_button_cross), "cross is not presented"

    def should_be_extension_text(self):
        assert self.is_element_present(*SettingsLocators.Extension_text), "Extension text is not presented"

    def should_be_checkbox_seller_verification(self):
        assert self.is_element_present(*SettingsLocators.Checkbox_seller_verification), "Checkbox seller verification is not presented"

    def should_be_notifications_text(self):
        assert self.is_element_present(*SettingsLocators.Notifications_text), "Notifications text is not presented"

    def should_be_checkbox_notification_counter(self):
        assert self.is_element_present(*SettingsLocators.Checkbox_notification_counter), "Checkbox_notification_counter is not presented"

    def checkbox_notification_counter_should_be_on(self):
        checkbox_notification_counter = self.browser.find_element(*SettingsLocators.Checkbox_notification_counter_value)
        attr_value = checkbox_notification_counter.get_attribute("class")
        assert attr_value == SettingsLocators.checkbox_on, f"checkbox is not active"

    def should_be_checkbox_push_notifications(self):
        assert self.is_element_present(*SettingsLocators.Checkbox_push_notifications), "Checkbox_push_notifications is not presented"

    def checkbox_push_notifications_should_be_on(self):
        checkbox_notification_counter = self.browser.find_element(*SettingsLocators.Checkbox_push_notifications_value)
        attr_value = checkbox_notification_counter.get_attribute("class")
        assert attr_value == SettingsLocators.checkbox_on, f"checkbox is not active"

    def should_be_message_describing_the_fall(self):
        assert self.is_element_present(*SettingsLocators.Message_describing_the_fall), "Message_describing_the_fall is not presented"

    def should_be_text_color_scheme(self):
        assert self.is_element_present(*SettingsLocators.Text_color_scheme), "Text_color_scheme is not presented"

    def should_be_light_theme(self):
        assert self.is_element_present(*SettingsLocators.Light_theme), "Light_theme is not presented"

    def light_theme_should_be_on(self):
        light_theme = self.browser.find_element(*SettingsLocators.Light_theme)
        attr_value = light_theme.get_attribute("class")
        assert attr_value == "_3hBHw CaRjS", f"The light_theme is not switched on"

    def should_be_dark_theme(self):
        assert self.is_element_present(*SettingsLocators.Dark_theme), "Dark_theme is not presented"

    def should_be_extension_version(self):
        color_scheme = self.browser.find_element(*SettingsLocators.Text_color_scheme)
        actions = ActionChains(self.browser)
        actions.move_to_element(color_scheme).perform()
        scroll_origin = ScrollOrigin.from_element(color_scheme)
        ActionChains(self.browser).scroll_from_origin(scroll_origin, 0, 300).perform()
        assert self.is_element_present(*SettingsLocators.Extension_version), "Extension_version is not presented"


