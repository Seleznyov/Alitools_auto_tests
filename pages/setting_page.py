from .base_page import BasePage
from .locators import SettingsLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from ..settings import setting_tabs


class SettingsPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(SettingsPage, self).__init__(*args, **kwargs)

    def get_active_tab(self):
        tabs = self.browser.find_elements(*SettingsLocators.Tabs)
        for i in range(len(tabs)):
            page_tab = tabs[i]
            activ_tab = page_tab.get_attribute('class')
            if activ_tab == SettingsLocators.active_tab:
                return page_tab.text

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
        assert attr_value == SettingsLocators.theme_on, f"The light_theme is not switched on"

    def should_be_dark_theme(self):
        assert self.is_element_present(*SettingsLocators.Dark_theme), "Dark_theme is not presented"

    def should_be_extension_version(self, tab):
        tab_general = self.browser.find_element(*SettingsLocators.Tab_general)
        actions = ActionChains(self.browser)
        actions.move_to_element(tab_general).perform()
        scroll_origin = ScrollOrigin.from_element(tab_general)
        ActionChains(self.browser).scroll_from_origin(scroll_origin, 0, 300).perform()
        if tab == setting_tabs[0]:
            assert self.is_element_present(*SettingsLocators.Extension_version_general_tab), "Extension_version is not presented"
        if tab == setting_tabs[1]:
            assert self.is_element_present(
                *SettingsLocators.Extension_version_search_by_image_tab), "Extension_version is not presented"

    def open_search_by_image_tab(self):
        tab_search_by_image = self.browser.find_element(*SettingsLocators.Tab_search_by_image)
        tab_search_by_image.click()

    def should_be_button_on_the_picture(self):
        assert self.is_element_present(*SettingsLocators.Button_on_the_picture), "block button_on_the_picture is not presented"

    def checkbox_button_on_the_picture_should_be_on(self):
        checkbox = self.browser.find_element(*SettingsLocators.Checkbox_button_on_the_picture_value)
        attr_value = checkbox.get_attribute("class")
        assert attr_value == SettingsLocators.checkbox_on, f"The light_theme is not switched on"

    def should_be_sites_with_disabled_button(self):
        text = "САЙТЫ С ВЫКЛЮЧЕННОЙ КНОПКОЙ"
        sites_with_disabled_button = self.browser.find_element(*SettingsLocators.Sites_with_disabled_button).text
        assert sites_with_disabled_button == text, f"Отображается: '{sites_with_disabled_button}'текст, вместо: '{text}'"

    def get_list_disabled_site(self):
        disabled_site_list = []
        disabled_sites = self.browser.find_elements(*SettingsLocators.Disabled_site)
        for i in disabled_sites:
            disabled_site_list.append(i.text)
        return disabled_site_list



