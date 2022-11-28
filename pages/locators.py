from selenium.webdriver.common.by import By


class BasePageLocators:
    Possible_answer = (By.XPATH, "//div[contains(text(),'Друзья или коллеги')]")
    Starting_greeting = (By.XPATH, "//div[contains(text(),'Alitools готов к работе')]")
    #  Прод локатор
    Cross_start_greeting = (By.XPATH, "//div[@class ='_2GJWf']/div/*[1]")
    # Тестовый локатор
    # Cross_start_greeting = (By.XPATH, "//body/div[6]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/*[1]")
    #  Прод локатор
    Cross_repeated_favorites = (By.XPATH, "//div[@class ='_29Pkd _1bFZv']/div[@class ='_26mJL']/*[1]")
    # Тестовый локатор
    # Cross_repeated_favorites = (By.XPATH, "//body/div[6]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/*[1]")
    Slider = (By.XPATH, "//span[@id='nc_1_n1z']")
    Warning_text = (By.XPATH, "//div[@class='warnning-text']")
    # Взять курс USD для "aliexpress"
    Usd_course_aliExpress_global = (By.XPATH, "//div[@class='rate-value-value'][1]")
    # Установка firefox
    Setup_firefox = (By.XPATH, "//button[contains(text(),'Всё понятно, включить Alitools!')]")


class ProductPageLocators:
    Product_price = (By.XPATH, "//div[@class ='snow-price_SnowPrice__mainS__18x8np']")
    Order_quantity = (By.XPATH, "//div[@class ='SnowProductDescription_ExtraInfo__wrap__193uk']/*[4]")
    Icon_login = (By.CSS_SELECTOR, ".SnowHeaderProfileItem_SnowHeaderProfileItem__item__1vsjg")
    Email_input = (By.CSS_SELECTOR, "#email")
    Password_input = (By.CSS_SELECTOR, "#password")
    Button_login = (By.XPATH, "//button[contains(text(),'Войти')]")
    Regional_settings = (By.XPATH, "//div[@class ='SnowMenu_FlagBlock__wrapper__i513w']/a[1]")
    # Переписать этот локатор сделать три разных вместо одного
    Regional_country_currency_language = (By.XPATH, "//div[@class='RegionalSettings_RegionalSettings__select__ieug1']")
    Value_country = (By.XPATH, "//div[@class='RegionalSettings_RegionalSettings__select__ieug1']//input")
    Regional_currency_list = (By.CSS_SELECTOR, ".RegionalSettings_RegionalSettings__item__ieug1")
    Regional_country_BEL = (By.XPATH, "//li[@id='downshift-0-item-20']")
    Regional_currency_USD = (By.XPATH, "//li[@id='downshift-2-item-139']")
    Regional_currency_RUB = (By.XPATH, "//li[@id='downshift-2-item-68']")
    Regional_currency_EUR = (By.XPATH, "//li[@id='downshift-2-item-36']")
    # Написать лучше
    # Save_settings_button = (By.XPATH,
    #                         "//div[@class='snow-scrolling-header_SnowScrollingHeader__buttonGroup__16wax0']/button")
    Save_settings_button = (By.XPATH,
                            "//div[@id='__aer_root__']/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/button")
    # Logo_link = (By.XPATH, "//div[@class='SnowCommonHeader_SnowCommonHeader__logo__ih4vk']/a")
    Logo_link = (By.XPATH,
                 "//div[@id='__aer_root__']/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a")
    # Блок проверки продавца на странице товара
    Seller_trust_level_title = (By.CSS_SELECTOR, ".at-legacy-seller-check__title")
    # Доставка и возврат - текст
    Delivery_and_returns = (By.XPATH, "//h2[contains(text(),'Доставка и возврат')]")
    # Кнопка "Прекрасно"
    Button_wonderful = (By.XPATH, "//div[@class='snow-ali-kit_Informer__flexAligner__8lq3ka']/button")
    # Button_wonderful = (By.XPATH, "//button[contains(text(),'Прекрасно')]")


class SettingsLocators:
    # Локаторы из виджета
    widget = "//div[@class ='at-theme-light'][2]"
    button_cross = "//a[@class ='_1OWT-']"
    languages_list = "//div[@class ='_1mJSj']/*[1]/div[@class ='_36pFQ']/*/select"
    currency_list = "//div[@class ='_1mJSj']/*[2]/div[@class ='_36pFQ']/*/select"
    option_languages = widget + "//div[@class ='_1mJSj']/*[1]/div[@class ='_36pFQ']/div[1]/select[1]/option"
    option_currency = widget + "//div[@class ='_1mJSj']/*[2]/div[@class ='_36pFQ']/div[1]/select[1]/option"
    checkbox_on = "at-checkbox__control at-checkbox__control--checked"
    theme_on = "_3hBHw CaRjS"
    Tabs = (By.XPATH, "//div[@class ='_2fg_j']/a/div")
    active_tab = "h0isI _3DJWM"

    Widget_settings_currency_list = (By.XPATH, widget + currency_list)
    Widget_settings_language_list = (By.XPATH, widget + languages_list)
    Currency_list_option = (By.XPATH, option_currency)
    Languages_list_option = (By.XPATH, option_languages)
    Widget_settings_button_cross = (By.XPATH, widget + button_cross)
    Widget_dark_theme = (By.XPATH, widget + "//div[@class ='aXt0T']/label[2]")
    Widget_value_theme = (By.XPATH, "//body/div[6]/div[2]")
    Widget_checkbox_seller_verification = (By.XPATH, widget+"//label[@class ='_2eD5O']/span")
    Widget_text_settings = (By.XPATH, widget + "//div[@class ='_8cmLo']")
    Widget_extension_text_dark = (By.XPATH, "//div[@class ='at-theme-dark'][2]//div[@class ='_1LiA_']")

    # Локаторы для настроек
    # Вкладка "Общее"
    Tab_general = (By.XPATH, "//div[@class ='_2fg_j']/a[1]")
    Languages_text = (By.XPATH, "//div[@class ='_1mJSj']/*[1]/div[@class ='_2s2Fd']")
    Settings_languages_list = (By.XPATH, languages_list)
    Currency_text = (By.XPATH, "//div[@class ='_1mJSj']/*[2]/div[@class ='_2s2Fd']")
    Settings_currency_list = (By.XPATH, currency_list)
    Settings_button_cross = (By.XPATH, button_cross)
    Extension_text = (By.XPATH, "//div[@class ='_1LiA_']")
    Checkbox_seller_verification = (By.XPATH, "//label[@class ='_2eD5O']")
    Notifications_text = (By.XPATH, "//div[@class ='_2OVEo']")
    Checkbox_notification_counter = (By.XPATH, "//label[@class ='_3ou1_'][1]")
    Checkbox_notification_counter_value = (By.XPATH, "//label[@class ='_3ou1_'][1]/span/div")
    Checkbox_push_notifications = (By.XPATH, "//label[@class ='_3ou1_'][2]")
    Checkbox_push_notifications_value = (By.XPATH, "//label[@class ='_3ou1_'][2]/span/div")
    Message_describing_the_fall = (By.XPATH, "//div[@class ='_1bxEt']")
    Text_color_scheme = (By.XPATH, "//div[@class ='_3s4F_']")
    Light_theme = (By.XPATH, "//div[@class ='aXt0T']/label[1]")
    Dark_theme = (By.XPATH, "//div[@class ='aXt0T']/label[2]")
    Extension_version_general_tab = (By.XPATH, "//div[@class ='UxYkK']")

    # Вкладка "Поиск по картинке"
    Tab_search_by_image = (By.XPATH, "//div[@class ='_2fg_j']/a[2]")
    Button_on_the_picture = (By.XPATH, "//label[@class ='_3g_v7']")
    Checkbox_button_on_the_picture_value = (By.XPATH, "//label[@class ='_3g_v7']/span/div")
    Sites_with_disabled_button = (By.XPATH, "//div[@class ='_327b9']")
    Disabled_site = (By.XPATH, "//div[@class ='JvDO_']//div[@class ='BTOq4']")
    Extension_version_search_by_image_tab = (By.XPATH, "//div[@class ='zcp1e']")

    # Вкладка "Советник"
    Tab_adviser = (By.XPATH, "//div[@class ='_2fg_j']/a[3]")
    Block_show_offers = (By.XPATH, "//label[@class ='_1v2vb']")
    Checkbox_show_offers_value = (By.XPATH, "//label[@class ='_1v2vb']/span/div")
    Block_sites_with_disabled_adviser = (By.XPATH, "//div[@class ='_2u4Wd']")
    Block_text_if_you_disable_the_widget = (By.XPATH, "//div[@class ='tbPpP']")
    Extension_version_adviser_tab = (By.XPATH, "//div[@class ='_2WEHj']")
    Image_adviser = (By.XPATH, "//img")

    # Вкладка "История"
    Tab_history = (By.XPATH, "//div[@class ='_2fg_j']/a[4]")
    Block_sites_with_history_enabled = (By.XPATH, "//div[@class ='_2u4Wd']")
    Block_text_disable_the_widget = (By.XPATH, "//div[@class ='_9EXxv']")
    Extension_version_history_tab = (By.XPATH, "//div[@class ='_3MMFq']")
    Image_history = (By.XPATH, "//img")

    # Вкладка "Синхронизация"
    Tab_synchronization = (By.XPATH, "//div[@class ='_2fg_j']/a[5]")
    Icon_cloud = (By.XPATH, "//div[@class ='KMEiY']/*[1]/*[1]")
    Text_create_or_sign_in_account = (By.XPATH, "//div[@class ='fi3Dt']")
    Create_account_button = (By.XPATH, "//button[1]")
    Log_in_button = (By.XPATH, "//button[2]")


class WidgetLocators:
    # цена
    # Проблемы с поиском этого локатора есть задрежка попробую через CSS
    Price_widget_button = (By.CSS_SELECTOR, ".at-widget-price__label")

    Card_name_price = (By.XPATH, "//div[contains(text(),'История цены')]")
    Price_drop_down_for_3_months = (
        By.XPATH, "//div[@class ='at-drop-down__open-button']/div[contains(text(), 'за 3 месяца')]")
    Value_months = (By.XPATH,
                    "//div[@class ='_2UY5W _31scG']/div[@class ='_3mN4L']/div[@class ='_14xnt']/div[@class ='_1QkN1']/div[@class ='_1BnRS']/*[1]")
    Drop_down_value_for_3_months = (By.XPATH, "//div[@class ='at-drop-down__menu']/*[1]/*[1]")
    Drop_down_value_for_half_a_year = (By.XPATH, "//div[@class ='at-drop-down__menu']/*[2]/*[1]")
    Price_button_accurate = (By.XPATH, "//div[contains(text(),'Точная')]")
    Price_button_average = (By.XPATH, "//div[contains(text(),'Средняя')]")
    Price_button_Follow_the_item = (By.XPATH, "//span[contains(text(), 'Следить за товаром')]")
    Price_button_info = (By.XPATH, "//div[@class ='at-body__controls']/*[1]")
    Price_button_settings = (By.XPATH, "//div[@class ='at-body__controls']/*[3]")
    Price_button_cross = (By.XPATH, "//div[@class ='at-body__controls']/a[2]/*[1]")
    Exact_price = (By.XPATH, "//div[@class ='_1aBUH']")

    # --------------------------------------------------------------------------------------------------------------
    # продавец
    Seller_widget_button = (By.XPATH, "//div[contains(text(),'продавец')]")
    Card_name_seller = (By.XPATH, "//div[contains(text(),'Рейтинг продавца')]")
    Seller_button_settings = (By.XPATH, "//div[@class ='at-body__controls']/*[1]")
    Seller_button_cross = (By.XPATH, "//div[@class ='at-body__controls']/*[2]")
    Percentage_value = (By.XPATH, "//div[@class ='at-widget-seller-check']/*[1]/*[1]")
    Value_inside_the_card = (By.XPATH, "//div[@class ='at-seller-check__main']/*[2]")

    # --------------------------------------------------------------------------------------------------------------
    # обзоры
    Reviews_widget_button = (By.XPATH, "//div[contains(text(),'обзоры')]")
    Card_name_reviews = (By.XPATH, "//div[contains(text(),'Обзоры')]")
    Reviews_button_settings = (By.XPATH, "//div[@class ='at-body__controls']/*[1]")
    Reviews_button_cross = (By.XPATH, "//div[@class ='at-body__controls']/*[2]")
    Reviews_displayed_text = (By.CSS_SELECTOR, ".at-tab-empty__title")
    Value_Reviews = (By.XPATH, "//div[@class ='at-widget-reviews']/*[1]")
    Value_Reviews_Images = (By.CSS_SELECTOR, ".at-photo-reviews-list__item")
    Overview_is_displayed = (By.CSS_SELECTOR, ".at-gallery__current-image")

    # --------------------------------------------------------------------------------------------------------------
    # похожие
    Similar_widget_button = (By.XPATH, "//div[contains(text(),'похожие')]")
    Card_name_similar = (By.XPATH, "//div[contains(text(),'Похожие')]")
    Similar_drop_down_sort = (By.CSS_SELECTOR, ".at-drop-down__label")
    Drop_down_values_1_2_3 = (By.XPATH, "//div[@class ='at-drop-down__menu']/div[@class ='at-drop-down__item']")
    Similar_button_settings = (By.XPATH, "//div[@class ='at-body__controls']/*[1]")
    Similar_button_cross = (By.XPATH, "//div[@class ='at-body__controls']/*[2]")
    Value_similar_products = (By.XPATH, "//div[@class ='at-widget-similars']/*[1]")
    Similar_products = (By.XPATH, "//div[@class ='at-similar-list']/div")
    Similar_products_for_url = (By.XPATH, "//div[@class ='at-similar-list']/div/a")
    Similar_products_price = (By.XPATH, "//div[@class ='at-similar-list']/div/a/div/*[1]")
    Products_price_sorted_by_price = (By.XPATH, "//div[@class ='at-similar-list__item-wrap']/a/div[2]/div[1]")
    # Для заказов надо два локатора
    Similar_products_orders1 = (By.XPATH, "//div[@class ='at-similar-list']/div/a/div/*[2]/span")
    Similar_products_orders2 = (By.XPATH, "//div[@class ='at-similar-list at-similar-list--small']/div/a/div/*[2]/span")
    # + Дополнительный для функции
    Similar_message_displayed = (By.CSS_SELECTOR, ".at-similar-list__best-offer-message")


    # --------------------------------------------------------------------------------------------------------------
    # история
    History_widget_button = (By.CSS_SELECTOR, ".at-widget-all-history__label")
    History_widget_collapse_button = (
        By.XPATH, "//div[@class ='at-widgets-panel at-widgets-history']/div[@class ='at-widgets-panel__arrow-wrapper']")
    History_widget_expand_button = (By.XPATH,
                                    "//div[@class ='at-widgets-panel at-widgets-history']/div[@class ='at-widgets-panel__arrow-wrapper at-widgets-panel__arrow-wrapper--open']")
    Card_name_history = (By.XPATH, "//div[contains(text(),'История просмотров')]")
    History_widget_control_context_menu = (
        By.XPATH, "//div[@class ='at-body__controls']/a/div[@class ='at-body__controls-context-menu']")
    History_button_cross = (By.XPATH, "//a[@class ='at-body__controls-item']/*[1]")
    History_text_today = (By.XPATH, "//div[contains(text(),'Сегодня')]")
    Product_in_history_for_widget = (By.CSS_SELECTOR, ".at-widgets-history-mask")
