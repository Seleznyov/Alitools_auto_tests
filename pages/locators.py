from selenium.webdriver.common.by import By


class BasePageLocators:
    Possible_answer = (By.XPATH, "//div[contains(text(),'Друзья или коллеги')]")
    Greeting = "//div[contains(text(),'Alitools готов к работе')]"
    Starting_greeting = (By.XPATH, Greeting)
    #  Прод локатор
    Cross_start = "//div[@class ='_2GJWf']/div/*[1]"
    Cross_start_greeting = (By.XPATH, Cross_start)
    # Тестовый локатор
    # Cross_start_greeting = (By.XPATH, "//body/div[6]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/*[1]")
    #  Прод локатор
    Cross_rep_favor = "//div[@class ='_29Pkd _1bFZv']/div[@class ='_26mJL']/*[1]"
    Cross_repeated_favorites = (By.XPATH, Cross_rep_favor)
    # Тестовый локатор
    # Cross_repeated_favorites = (By.XPATH, "//body/div[6]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/*[1]")
    Slider = (By.XPATH, "//span[@id='nc_1_n1z']")
    Errloading = (By.XPATH, "//*[@class='errloading']")
    Warning_text_close = (By.XPATH, "//div[@class='warnning-text']")
    Dialog_close = (By.XPATH, "//div[@class='baxia-dialog-close']")
    Warning_text = (By.XPATH, "//div[contains(text(),'Пройдите проверку')]")
    # Взять курс USD для "aliexpress"
    Usd_course_aliExpress_global = (By.XPATH, "//div[@class='rate-value-value'][1]")
    # Установка firefox
    Setup_firefox = (By.XPATH, "//button[contains(text(),'Всё понятно, включить Alitools!')]")
    # Товар уже разобрали (текст на странице)
    Item_has_already_been_taken_apart_text = (By.XPATH, "//span[contains(text(),'Товар уже разобрали')]")


class ProductPageLocators:
    Product_price = (By.XPATH, "//div[@class ='snow-price_SnowPrice__mainS__18x8np']")
    Product_sku_picture = (By.XPATH, "//div[@exp_page_area='sku_floor']/div[2]/div/div/div")
    Order_quantity = (By.XPATH, "//div[@class ='SnowProductDescription_ExtraInfo__wrap__193uk']/*[4]")
    Icon_login = (By.CSS_SELECTOR, ".SnowHeaderProfileItem_SnowHeaderProfileItem__item__1vsjg")
    Email_input = (By.CSS_SELECTOR, "#email")
    Password_input = (By.CSS_SELECTOR, "#password")
    Button_login = (By.XPATH, "//button[contains(text(),'Войти')]")
    Regional_settings = (By.XPATH, "//div[@class ='SnowMenu_FlagBlock__wrapper__i513w']/a[1]")
    # Переписать этот локатор сделать три разных вместо одного
    Regional_country_currency_language = (By.XPATH, "//div[@class='snow-ali-kit_Input__inputFieldWrapper__1aiyxh']")
    Value_country = (By.XPATH, "//div[@class='snow-ali-kit_Input__inputFieldWrapper__1aiyxh']//input")
    Regional_currency_list = (By.CSS_SELECTOR, ".snow-dropdown_ListElement__wrapper__ft25lq")
    Regional_country_BEL = (By.XPATH, "//li/div[2]/img[@alt='BY']")
    Regional_currency_USD = (By.XPATH, "//li/div[2]/img[@alt='USD']")
    Regional_currency_RUB = (By.XPATH, "//li/div[2]/img[@alt='RUB']")
    Regional_currency_EUR = (By.XPATH, "//li/div[2]/img[@alt='EUR']")

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
    Button_wond = "//div[@class='snow-ali-kit_Informer__flexAligner__8lq3ka']/button"
    Button_wonderful = (By.XPATH, Button_wond)
    # Button_wonderful = (By.XPATH, "//button[contains(text(),'Прекрасно')]")
    Product_image = (By.XPATH, "//div[@class='gallery_Gallery__picListWrapper__re6q0q']/div/div")
    Product_image_com = (By.XPATH, "//div[@class='video-container']/img")
    Find_on_aliexpress_icon = (By.XPATH, "//div[@class='_3Q0G5']")
    Find_on_aliexpress_button = (By.XPATH, "//div[@class='_2Nj_w VRH7i']")
    Find_on_aliexpress_drop_down = (By.XPATH, "//div[@class='_1pe-u VRH7i']")
    Product_search_by_image_text = (By.CSS_SELECTOR, ".ssdMT")
    Img_result = ".h1ISG"
    Image_search_result = (By.CSS_SELECTOR, Img_result)
    Find_on_aliexpress_drop_down_values = (By.CSS_SELECTOR, "._3vAZ7")
    # Локаторы продуктов
    # sportmaster
    Product_image_from_sportmaster = (By.XPATH, "//div/img[@data-selenium='image']")
    # svyaznoy
    Product_image_from_svyaznoy = (By.XPATH, "//div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/img[1]")
    # mvideo
    Product_image_from_mvideo = (By.XPATH, "//div/*[1]/button/picture")


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
    Widget_tab_general = (By.XPATH, widget + "//div[@class ='_2fg_j']/a[1]")
    Widget_tab_search_by_image = (By.XPATH, widget + "//div[@class ='_2fg_j']/a[2]")
    Widget_tab_adviser = (By.XPATH, widget + "//div[@class ='_2fg_j']/a[3]")
    Widget_tab_history = (By.XPATH, widget + "//div[@class ='_2fg_j']/a[4]")
    Widget_tab_synchronization = (By.XPATH, widget + "//div[@class ='_2fg_j']/a[5]")
    Widget_extension_text_dark = (By.XPATH, "//div[@class ='at-theme-dark'][2]//div[@class ='_1LiA_']")
    Widget_disabled_site = (By.XPATH, widget + "//div[@class ='JvDO_']//div[@class ='BTOq4']")
    Widget_checkbox_button_on_image = (By.XPATH, widget + "//label[@class ='_3g_v7']/span/div")
    Widget_cross_for_disabled_site = (By.XPATH, widget + "//div[@class ='JvDO_']/*[3]")
    Widget_text_for_empty_disabled_list = (By.CSS_SELECTOR, "._1T683")
    Site_names_dis_his = "._1k9Ks"
    Site_names_with_disabled_history = (By.CSS_SELECTOR, Site_names_dis_his)

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
    Tab_hist = "//div[@class ='_2fg_j']/a[4]"
    Tab_history = (By.XPATH, Tab_hist)
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
    # Price_button = ".at-widget-price__label"
    # Пробую через XPATH
    Price_button = "//div[@class ='at-widgets-panel']/div/div[2]/div[1]"
    Price_widget_button = (By.XPATH, Price_button)

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
    Exact_pr = "//div[@class ='_1aBUH']"
    Exact_price = (By.XPATH, Exact_pr)

    # --------------------------------------------------------------------------------------------------------------
    # продавец
    Seller_widget_button = (By.CSS_SELECTOR, ".at-widget-seller-check__percentage__label")
    Card_name_seller = (By.XPATH, "//div[contains(text(),'Рейтинг продавца')]")
    Seller_button_settings = (By.XPATH, "//div[@class ='at-body__controls']/*[1]")
    Seller_button_cross = (By.XPATH, "//div[@class ='at-body__controls']/*[2]")
    Percentage = "//div[@class ='at-widget-seller-check']/*[1]/*[1]"
    Percentage_value = (By.XPATH, Percentage)
    Value_inside_the_card = (By.XPATH, "//div[@class ='at-seller-check__main']/*[2]")

    # --------------------------------------------------------------------------------------------------------------
    # обзоры
    Reviews_widget_button = (By.CSS_SELECTOR, ".at-widget-reviews__label")
    Card_name_reviews = (By.XPATH, "//div[contains(text(),'Обзоры')]")
    Reviews_button_settings = (By.XPATH, "//div[@class ='at-body__controls']/*[1]")
    Reviews_button_cross = (By.XPATH, "//div[@class ='at-body__controls']/*[2]")
    Reviews_displayed_text = (By.CSS_SELECTOR, ".at-tab-empty__title")
    Value_Reviews = (By.XPATH, "//div[@class ='at-widget-reviews']/*[1]")
    Value_Reviews_Images = (By.CSS_SELECTOR, ".at-photo-reviews-list__item")
    Overview_is_displayed = (By.CSS_SELECTOR, ".at-gallery__current-image")

    # --------------------------------------------------------------------------------------------------------------
    # похожие
    Similar_button = ".at-widget-similars__label"
    Similar_widget_button = (By.CSS_SELECTOR, Similar_button)
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
    Similar_products_1 = "//div[@class ='at-similar-list']/div/a/div/*[2]/span"
    Similar_products_orders1 = (By.XPATH, Similar_products_1)
    Similar_products_2 = "//div[@class ='at-similar-list at-similar-list--small']/div/a/div/*[2]/span"
    Similar_products_orders2 = (By.XPATH, Similar_products_2)
    # + Дополнительный для функции
    Similar_message_displayed = (By.CSS_SELECTOR, ".at-similar-list__best-offer-message")

    # --------------------------------------------------------------------------------------------------------------
    # избранное
    favorites_button = (By.CSS_SELECTOR, ".at-favorites-panel-button")
    text_product_added_to_Alitools = (By.XPATH, "//div[@class ='_2QV79']/*[1]")

    # --------------------------------------------------------------------------------------------------------------
    # история
    History_button = ".at-widget-all-history__label"
    History_widget_button = (By.CSS_SELECTOR, History_button)
    History_widget_collapse_button = (
        By.XPATH, "//div[@class ='at-widgets-panel at-widgets-history']/div[@class ='at-widgets-panel__arrow-wrapper']")
    History_widget_expand_button = (By.XPATH,
                                    "//div[@class ='at-widgets-panel at-widgets-history']/div[@class ='at-widgets-panel__arrow-wrapper at-widgets-panel__arrow-wrapper--open']")
    Card_name_history = (By.XPATH, "//div[contains(text(),'История просмотров')]")
    History_widget_con_menu = "//div[@class ='at-body__controls']/a/div[@class ='at-body__controls-context-menu']"
    History_widget_control_context_menu = (By.XPATH, History_widget_con_menu)
    History_button_cross = (By.XPATH, "//a[@class ='at-body__controls-item']/*[1]")
    History_text_today = (By.XPATH, "//div[contains(text(),'Сегодня')]")
    Product_in_history = ".at-widgets-history__item"
    Product_in_history_for_widget = (By.CSS_SELECTOR, Product_in_history)
    Product_card_from_the_history = (By.CSS_SELECTOR, ".W92R1")
    Button_cross_for_history_card = (By.XPATH, "//div[@class ='W92R1']/*[1]")
    Empty_title_history_card = (By.CSS_SELECTOR, ".at-tab-empty__title")
    Customize_history_button = (By.XPATH, "//div[@class ='_2tt2W HRySV']/div[2]")
    Do_not_show_button = "//div[@class ='_2tt2W HRySV']/div[1]"
    Do_not_show_on_this_site_button = (By.XPATH, Do_not_show_button)

