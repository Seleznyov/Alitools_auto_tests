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

    def open_language_list(self):
        language_list = self.browser.find_element(*SettingsLocators.Widget_settings_language_list)
        language_list.click()

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

    def choose_language(self, language):
        Languages_list_option = self.browser.find_elements(*SettingsLocators.Languages_list_option)
        r = 1
        for value in Languages_list_option:
            if value.get_attribute('value') == language:
                currency = self.browser.find_element(By.XPATH, SettingsLocators.option_languages + str([r]))
                currency.click()
            r += 1

    def translation_check_for_settings(self, language):
        if language == "ru":
            text_settings = self.browser.find_element(*SettingsLocators.Widget_text_settings).text
            assert text_settings == "Настройки", f"Ошибка, вернулось название настроек {text_settings}, для {language}"
        if language == "en":
            text_settings = self.browser.find_element(*SettingsLocators.Widget_text_settings).text
            assert text_settings == "Settings", f"Ошибка, вернулось название настроек {text_settings}, для {language}"
            tab_general = self.browser.find_element(*SettingsLocators.Widget_tab_general).text
            assert tab_general == "General", f"Ошибка, в названии вкладки {tab_general}, для {language}"
            tab_search_by_image = self.browser.find_element(*SettingsLocators.Widget_tab_search_by_image).text
            assert tab_search_by_image == "Search by image",\
                f"Ошибка, в названии вкладки {tab_search_by_image}, для {language}"
            tab_adviser = self.browser.find_element(*SettingsLocators.Widget_tab_adviser).text
            assert tab_adviser == "Adviser", f"Ошибка, в названии вкладки {tab_adviser}, для {language}"
            tab_history = self.browser.find_element(*SettingsLocators.Widget_tab_history).text
            assert tab_history == "History", f"Ошибка, в названии вкладки {tab_history}, для {language}"
            tab_synchronization = self.browser.find_element(*SettingsLocators.Widget_tab_synchronization).text
            assert tab_synchronization == "Synchronization", \
                f"Ошибка, в названии вкладки {tab_synchronization}, для {language}"
        if language == "pl":
            text_settings = self.browser.find_element(*SettingsLocators.Widget_text_settings).text
            assert text_settings == "Ustawienia", f"Ошибка, вернулось название настроек {text_settings}, для {language}"
            tab_general = self.browser.find_element(*SettingsLocators.Widget_tab_general).text
            assert tab_general == "Ogólne", f"Ошибка, в названии вкладки {tab_general}, для {language}"
            tab_search_by_image = self.browser.find_element(*SettingsLocators.Widget_tab_search_by_image).text
            assert tab_search_by_image == "Search by image", \
                f"Ошибка, в названии вкладки {tab_search_by_image}, для {language} "
            tab_adviser = self.browser.find_element(*SettingsLocators.Widget_tab_adviser).text
            assert tab_adviser == "Adviser", f"Ошибка, в названии вкладки {tab_adviser}, для {language}"
            tab_history = self.browser.find_element(*SettingsLocators.Widget_tab_history).text
            assert tab_history == "History", f"Ошибка, в названии вкладки {tab_history}, для {language}"
            tab_synchronization = self.browser.find_element(*SettingsLocators.Widget_tab_synchronization).text
            assert tab_synchronization == "Synchronization", \
                f"Ошибка, в названии вкладки {tab_synchronization}, для {language}"
        if language == "es":
            text_settings = self.browser.find_element(*SettingsLocators.Widget_text_settings).text
            assert text_settings == "Ajustes", f"Ошибка, вернулось название настроек {text_settings}, для {language}"
            tab_general = self.browser.find_element(*SettingsLocators.Widget_tab_general).text
            assert tab_general == "General", f"Ошибка, в названии вкладки {tab_general}, для {language}"
            tab_search_by_image = self.browser.find_element(*SettingsLocators.Widget_tab_search_by_image).text
            assert tab_search_by_image == "Search by image", \
                f"Ошибка, в названии вкладки {tab_search_by_image}, для {language} "
            tab_adviser = self.browser.find_element(*SettingsLocators.Widget_tab_adviser).text
            assert tab_adviser == "Adviser", f"Ошибка, в названии вкладки {tab_adviser}, для {language}"
            tab_history = self.browser.find_element(*SettingsLocators.Widget_tab_history).text
            assert tab_history == "History", f"Ошибка, в названии вкладки {tab_history}, для {language}"
            tab_synchronization = self.browser.find_element(*SettingsLocators.Widget_tab_synchronization).text
            assert tab_synchronization == "Synchronization", \
                f"Ошибка, в названии вкладки {tab_synchronization}, для {language}"
        if language == "fr":
            text_settings = self.browser.find_element(*SettingsLocators.Widget_text_settings).text
            assert text_settings == "Paramètres", f"Ошибка, вернулось название настроек {text_settings}, для {language}"
            tab_general = self.browser.find_element(*SettingsLocators.Widget_tab_general).text
            assert tab_general == "Général", f"Ошибка, в названии вкладки {tab_general}, для {language}"
            tab_search_by_image = self.browser.find_element(*SettingsLocators.Widget_tab_search_by_image).text
            assert tab_search_by_image == "Search by image", \
                f"Ошибка, в названии вкладки {tab_search_by_image}, для {language}"
            tab_adviser = self.browser.find_element(*SettingsLocators.Widget_tab_adviser).text
            assert tab_adviser == "Adviser", f"Ошибка, в названии вкладки {tab_adviser}, для {language}"
            tab_history = self.browser.find_element(*SettingsLocators.Widget_tab_history).text
            assert tab_history == "History", f"Ошибка, в названии вкладки {tab_history}, для {language}"
            tab_synchronization = self.browser.find_element(*SettingsLocators.Widget_tab_synchronization).text
            assert tab_synchronization == "Synchronization", \
                f"Ошибка, в названии вкладки {tab_synchronization}, для {language}"
        if language == "pt":
            text_settings = self.browser.find_element(*SettingsLocators.Widget_text_settings).text
            assert text_settings == "Configurações", \
                f"Ошибка, вернулось название настроек {text_settings}, для {language} "
            tab_general = self.browser.find_element(*SettingsLocators.Widget_tab_general).text
            assert tab_general == "Gerais", f"Ошибка, в названии вкладки {tab_general}, для {language}"
            tab_search_by_image = self.browser.find_element(*SettingsLocators.Widget_tab_search_by_image).text
            assert tab_search_by_image == "Buscar por imagem", \
                f"Ошибка, в названии вкладки {tab_search_by_image}, для {language} "
            tab_adviser = self.browser.find_element(*SettingsLocators.Widget_tab_adviser).text
            assert tab_adviser == "Consultor", f"Ошибка, в названии вкладки {tab_adviser}, для {language}"
            tab_history = self.browser.find_element(*SettingsLocators.Widget_tab_history).text
            assert tab_history == "Histórico", f"Ошибка, в названии вкладки {tab_history}, для {language}"
            tab_synchronization = self.browser.find_element(*SettingsLocators.Widget_tab_synchronization).text
            assert tab_synchronization == "Sincronização", \
                f"Ошибка, в названии вкладки {tab_synchronization}, для {language}"

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
        assert self.is_element_present(*SettingsLocators.Checkbox_seller_verification), \
            "Checkbox seller verification is not presented"

    def should_be_notifications_text(self):
        assert self.is_element_present(*SettingsLocators.Notifications_text), "Notifications text is not presented"

    def should_be_checkbox_notification_counter(self):
        assert self.is_element_present(*SettingsLocators.Checkbox_notification_counter), \
            "Checkbox_notification_counter is not presented"

    def checkbox_notification_counter_should_be_on(self):
        checkbox_notification_counter = self.browser.find_element(*SettingsLocators.Checkbox_notification_counter_value)
        attr_value = checkbox_notification_counter.get_attribute("class")
        assert attr_value == SettingsLocators.checkbox_on, f"checkbox is not active"

    def should_be_checkbox_push_notifications(self):
        assert self.is_element_present(*SettingsLocators.Checkbox_push_notifications), \
            "Checkbox_push_notifications is not presented"

    def checkbox_push_notifications_should_be_on(self):
        checkbox_notification_counter = self.browser.find_element(*SettingsLocators.Checkbox_push_notifications_value)
        attr_value = checkbox_notification_counter.get_attribute("class")
        assert attr_value == SettingsLocators.checkbox_on, f"checkbox is not active"

    def should_be_message_describing_the_fall(self):
        assert self.is_element_present(*SettingsLocators.Message_describing_the_fall), \
            "Message_describing_the_fall is not presented"

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
            assert self.is_element_present(*SettingsLocators.Extension_version_general_tab), \
                "Extension_version is not presented"
        if tab == setting_tabs[1]:
            assert self.is_element_present(
                *SettingsLocators.Extension_version_search_by_image_tab), "Extension_version is not presented"
        if tab == setting_tabs[2]:
            assert self.is_element_present(
                *SettingsLocators.Extension_version_adviser_tab), "Extension_version is not presented"
        if tab == setting_tabs[3]:
            assert self.is_element_present(
                *SettingsLocators.Extension_version_history_tab), "Extension_version is not presented"

    def open_search_by_image_tab(self):
        tab_search_by_image = self.browser.find_element(*SettingsLocators.Tab_search_by_image)
        tab_search_by_image.click()

    def should_be_button_on_the_picture(self):
        assert self.is_element_present(*SettingsLocators.Button_on_the_picture), \
            "block button_on_the_picture is not presented"

    def checkbox_button_on_the_picture_should_be_on(self):
        checkbox = self.browser.find_element(*SettingsLocators.Checkbox_button_on_the_picture_value)
        attr_value = checkbox.get_attribute("class")
        assert attr_value == SettingsLocators.checkbox_on, f"The light_theme is not switched on"

    def should_be_sites_with_disabled_button(self):
        text = "САЙТЫ С ВЫКЛЮЧЕННОЙ КНОПКОЙ"
        sites_with_disabled_button = self.browser.find_element(*SettingsLocators.Sites_with_disabled_button).text
        assert sites_with_disabled_button == text, f"Отображается:'{sites_with_disabled_button}'текст, вместо:'{text}'"

    def get_list_disabled_site(self):
        disabled_site_list = []
        disabled_sites = self.browser.find_elements(*SettingsLocators.Disabled_site)
        for i in disabled_sites:
            disabled_site_list.append(i.text)
        return disabled_site_list

    def open_adviser_tab(self):
        tab_adviser = self.browser.find_element(*SettingsLocators.Tab_adviser)
        tab_adviser.click()

    def should_be_block_show_offers(self):
        assert self.is_element_present(*SettingsLocators.Block_show_offers), "Block_show_offers is not presented"

    def checkbox_show_offers_should_be_on(self):
        checkbox = self.browser.find_element(*SettingsLocators.Checkbox_show_offers_value)
        attr_value = checkbox.get_attribute("class")
        assert attr_value == SettingsLocators.checkbox_on, f"checkbox show_offers is not switched on"

    def should_be_block_sites_with_disabled_adviser(self):
        assert self.is_element_present(*SettingsLocators.Block_sites_with_disabled_adviser), "block  is not presented"

    def should_be_block_text_if_you_disable_the_widget(self):
        assert self.is_element_present(*SettingsLocators.Block_text_if_you_disable_the_widget), "block is not presented"

    def should_be_image_adviser(self):
        image_adviser = self.browser.find_element(*SettingsLocators.Image_adviser)
        src = image_adviser.get_attribute("src")
        assert src == "https://alitools-static.s3-eu-west-1.amazonaws.com/extension/sovetnik-widget-light-ru.png", \
            f"image_adviser is not presented"

    def open_tab_history(self):
        tab_history = self.browser.find_element(*SettingsLocators.Tab_history)
        tab_history.click()

    def should_be_block_sites_with_history_enabled(self):
        assert self.is_element_present(*SettingsLocators.Block_sites_with_history_enabled), "block  is not presented"

    def should_be_block_text_disable_the_widget(self):
        assert self.is_element_present(*SettingsLocators.Block_text_disable_the_widget), "block  is not presented"

    def should_be_image_history(self):
        image_history = self.browser.find_element(*SettingsLocators.Image_history)
        src = image_history.get_attribute("src")
        assert src == "https://alitools-static.s3-eu-west-1.amazonaws.com/extension/history_settings_light_empty_ru.png", \
            f"image_history is not presented"

    def open_tab_synchronization(self):
        tab_synchronization = self.browser.find_element(*SettingsLocators.Tab_synchronization)
        tab_synchronization.click()

    def should_be_icon_cloud(self):
        assert self.is_element_present(*SettingsLocators.Icon_cloud), "Icon_cloud is not presented"

    def should_be_text_create_or_sign_in_account(self):
        assert self.is_element_present(*SettingsLocators.Text_create_or_sign_in_account), "Text is not presented"

    def should_be_create_account_button(self):
        assert self.is_element_present(*SettingsLocators.Create_account_button), \
            "Create_account_button is not presented"

    def should_be_log_in_button(self):
        assert self.is_element_present(*SettingsLocators.Log_in_button), "Log_in_button is not presented"

    def choose_dark_theme(self):
        dark_theme = self.browser.find_element(*SettingsLocators.Widget_dark_theme)
        dark_theme.click()

    def should_be_dark_theme_active(self):
        dark_theme = self.browser.find_element(*SettingsLocators.Dark_theme)
        attr_value = dark_theme.get_attribute("class")
        assert attr_value == SettingsLocators.theme_on, f"The dark_theme is not switched on"

    def turn_on_widget_checkbox_seller_verification(self):
        checkbox_seller_verification = self.browser.find_element(*SettingsLocators.Widget_checkbox_seller_verification)
        checkbox_seller_verification.click()

    def scroll_to_general_settings(self):
        text_color_scheme = self.browser.find_element(*SettingsLocators.Widget_extension_text_dark)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", text_color_scheme)
