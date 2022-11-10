from selenium.webdriver.common.by import By


class BasePageLocators:
    Possible_answer = (By.XPATH, "//div[contains(text(),'Друзья или коллеги')]")
    Starting_greeting = (By.XPATH, "//div[contains(text(),'Alitools готов к работе')]")
    Cross_start_greeting = (By.XPATH, "//div[@class ='_2GJWf']/div[@class ='_2CcGF']/*[1]")
    Cross_repeated_favorites = (By.XPATH, "//div[@class ='_29Pkd _1bFZv']/div[@class ='_26mJL']/*[1]")


class ProductPageLocators:
    Product_price = (By.XPATH, "//div[@class ='snow-price_SnowPrice__mainS__18x8np']")
    Order_quantity = (By.XPATH, "//div[@class ='SnowProductDescription_ExtraInfo__wrap__193uk']/*[4]")
    icon_login = (By.CSS_SELECTOR, ".SnowHeaderProfileItem_SnowHeaderProfileItem__item__1vsjg")
    email_input = (By.CSS_SELECTOR, "#email")
    password_input = (By.CSS_SELECTOR, "#password")
    button_login = (By.XPATH, "//button[contains(text(),'Войти')]")
    regional_settings = (By.XPATH, "//div[@class ='SnowMenu_FlagBlock__wrapper__i513w']/a[1]")
    # Переписать этот локатор сделать три разных вместо одного
    regional_country_currency_language = (By.XPATH, "//div[@class='RegionalSettings_RegionalSettings__select__ieug1']")
    regional_currency_list = (By.CSS_SELECTOR, ".RegionalSettings_RegionalSettings__item__ieug1")
    regional_currency_USD = (By.XPATH, "//li[@id='downshift-2-item-139']")
    regional_currency_RUB = (By.XPATH, "//li[@id='downshift-2-item-68']")
    regional_currency_EUR = (By.XPATH, "//li[@id='downshift-2-item-36']")
    save_settings_button = (By.XPATH, "//div[@class='snow-scrolling-header_SnowScrollingHeader__buttonGroup__1uifpm']")
    logo_link = (By.XPATH, "//div[@class='SnowCommonHeader_SnowCommonHeader__logo__okk9w']/a")


class SettingsLocators:
    # Почему-то поменялся локатор с div[6] на div[5] когда стал смотреть тестовую сборку
    Currency_list = (By.XPATH, "//div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/select[1]")
    option_currency = ("//div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/select[contains(@class, 'at-select__control')]/option")
    option_languages = ("//div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/select[contains(@class, 'at-select__control')]/option")
    Currency_list_option = (By.XPATH, option_currency)
    Languages_list_option = (By.XPATH, option_languages)
    Settings_button_cross = (By.XPATH, "//div[2]/div[1]/div[2]/div[1]/div[1]/a[1]")


class WidgetLocators:
    # цена
    # Проблемы с поиском этого локатора есть задрежка попробую через CSS
    Price_widget_button = (By.CSS_SELECTOR, ".at-widget-price__label")

    Card_name_price = (By.XPATH, "//div[contains(text(),'История цены')]")
    Price_drop_down_for_3_months = (By.XPATH, "//div[@class ='at-drop-down__open-button']/div[contains(text(), 'за 3 месяца')]")
    Value_months = (By.XPATH, "//div[@class ='_2UY5W _31scG']/div[@class ='_3mN4L']/div[@class ='_14xnt']/div[@class ='_1QkN1']/div[@class ='_1BnRS']/*[1]")
    Drop_down_value_for_3_months = (By.XPATH, "//div[@class ='at-drop-down__menu']/*[1]/*[1]")
    Drop_down_value_for_half_a_year = (By.XPATH, "//div[@class ='at-drop-down__menu']/*[2]/*[1]")
    Price_button_accurate = (By.XPATH, "//div[contains(text(),'Точная')]")
    Price_button_average = (By.XPATH, "//div[contains(text(),'Средняя')]")
    Price_button_Follow_the_item = (By.XPATH, "//span[contains(text(), 'Следить за товаром')]")
    Price_button_info = (By.XPATH, "//div[@class ='at-body__controls']/*[1]")
    Price_button_settings = (By.XPATH, "//div[@class ='at-body__controls']/*[3]")
    Price_button_cross = (By.XPATH, "//div[@class ='at-body__controls']/*[4]")

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
#   обзоры
    Reviews_widget_button = (By.XPATH, "//div[contains(text(),'обзоры')]")
    Card_name_reviews = (By.XPATH, "//div[contains(text(),'Обзоры')]")
    Reviews_button_settings = (By.XPATH, "//div[@class ='at-body__controls']/*[1]")
    Reviews_button_cross = (By.XPATH, "//div[@class ='at-body__controls']/*[2]")
    Reviews_displayed_text = (By.CSS_SELECTOR, ".at-tab-empty__title")
    Value_Reviews = (By.XPATH, "//div[@class ='at-widget-reviews']/*[1]")
    Value_Reviews_Images = (By.CSS_SELECTOR, ".at-photo-reviews-list__item")
    Overview_is_displayed = (By.CSS_SELECTOR, ".at-gallery__current-image")


# --------------------------------------------------------------------------------------------------------------
#   похожие
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
#   история
    History_widget_button = (By.CSS_SELECTOR, ".at-widget-all-history")
    History_widget_collapse_button = (By.XPATH, "//div[@class ='at-widgets-panel at-widgets-history']/div[@class ='at-widgets-panel__arrow-wrapper']")
    History_widget_expand_button = (By.XPATH, "//div[@class ='at-widgets-panel at-widgets-history']/div[@class ='at-widgets-panel__arrow-wrapper at-widgets-panel__arrow-wrapper--open']")
    Card_name_history = (By.XPATH, "//div[contains(text(),'История просмотров')]")
    History_widget_control_context_menu = (By.XPATH, "//div[@class ='at-body__controls']/a/div[@class ='at-body__controls-context-menu']")
    History_button_cross = (By.XPATH, "//a[@class ='at-body__controls-item']/*[1]")
    History_text_today = (By.XPATH, "//div[contains(text(),'Сегодня')]")
    Product_in_history_for_widget = (By.CSS_SELECTOR, ".at-widgets-history-mask")

