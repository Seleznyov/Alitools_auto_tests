import time
from .base_page import BasePage
from .locators import WidgetLocators
import nums_from_string
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import random


class WidgetPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(WidgetPage, self).__init__(*args, **kwargs)

    # ======================================================================================================================
    # цена
    def open_price_widget(self):
        price_widget_button = self.browser.find_element(*WidgetLocators.Price_widget_button)
        price_widget_button.click()

    def should_be_card_price(self):
        assert self.is_element_present(*WidgetLocators.Card_name_price), "element is not presented"

    def should_be_price_drop_down_for_3_months(self):
        assert self.is_element_present(*WidgetLocators.Price_drop_down_for_3_months), "element is not presented"

    def open_price_drop_down_for_3_months(self):
        drop_down_for_3_months = self.browser.find_element(*WidgetLocators.Price_drop_down_for_3_months)
        drop_down_for_3_months.click()

    def should_be_price_drop_down_value(self):
        assert self.is_element_present(*WidgetLocators.Drop_down_value_for_3_months), "element is not presented"
        assert self.is_element_present(*WidgetLocators.Drop_down_value_for_half_a_year), "element is not presented"

    def should_be_price_button_accurate(self):
        assert self.is_element_present(*WidgetLocators.Price_button_accurate), "element is not presented"

    def should_be_price_button_average(self):
        assert self.is_element_present(*WidgetLocators.Price_button_average), "element is not presented"

    def should_be_price_button_follow_the_item(self):
        assert self.is_element_present(*WidgetLocators.Price_button_Follow_the_item), "element is not presented"

    def should_be_price_button_info(self):
        assert self.is_element_present(*WidgetLocators.Price_button_info), "element is not presented"

    def price_button_info_open(self):
        button_info_open = self.browser.find_element(*WidgetLocators.Price_button_info)
        button_info_open.click()

    def should_be_price_button_settings(self):
        assert self.is_element_present(*WidgetLocators.Price_button_settings), "element is not presented"

    def open_price_settings(self):
        price_settings = self.browser.find_element(*WidgetLocators.Price_button_settings)
        price_settings.click()

    def close_price_card(self):
        price_card = self.browser.find_element(*WidgetLocators.Price_button_cross)
        price_card.click()

    def should_be_price_button_cross(self):
        assert self.is_element_present(*WidgetLocators.Price_button_cross), "element is not presented"

    # Значение точной цены на графике
    def exact_price(self):
        exact_price = self.browser.find_element(*WidgetLocators.Exact_price).text
        exact_price = exact_price.translate({ord(i): None for i in ' руб$€¥₽'})
        exact_price = exact_price.replace(' ', '')
        return float(exact_price)

    # Получить количество месяцев на графике
    def get_value_months(self):
        months_list = []
        months = self.browser.find_elements(*WidgetLocators.Value_months)
        for month in months:
            months_list.append(month.text)
        value_months = len(months_list)
        return value_months

    def select_value_for_half_a_year(self):
        for_half_a_year = self.browser.find_element(*WidgetLocators.Drop_down_value_for_half_a_year)
        for_half_a_year.click()

    # ======================================================================================================================
    # продавец
    def open_seller_widget(self):
        seller_widget_button = self.browser.find_element(*WidgetLocators.Seller_widget_button)
        seller_widget_button.click()

    def should_be_card_seller(self):
        assert self.is_element_present(*WidgetLocators.Card_name_seller), "element is not presented"

    def should_be_seller_button_settings(self):
        assert self.is_element_present(*WidgetLocators.Seller_button_settings), "element is not presented"

    def should_be_seller_button_cross(self):
        assert self.is_element_present(*WidgetLocators.Seller_button_cross), "element is not presented"

    def get_percentage_value(self):
        percentage_value = self.browser.find_element(*WidgetLocators.Percentage_value).text
        percentage_value = int(percentage_value)
        return percentage_value

    def get_percentage_value_inside_the_card(self):
        percentage_value = self.browser.find_element(*WidgetLocators.Value_inside_the_card).text
        percentage_value = nums_from_string.get_nums(percentage_value)[0]
        return percentage_value

    # Проверка рейтинга продовца
    def check_rating_seller(self):
        value = self.browser.find_element(*WidgetLocators.Value_inside_the_card).text
        value_rating = ''.join(c for c in value if c.isalpha())
        percentage_value = self.browser.find_element(*WidgetLocators.Percentage_value).text
        percentage_value = int(percentage_value)
        if value_rating == "Высокий":
            assert percentage_value in range(87, 101)
        elif value_rating == "Средний":
            assert percentage_value in range(50, 87)
        elif value_rating == "Низкий ":
            assert percentage_value in range(0, 50)
        return value_rating, percentage_value

    # ======================================================================================================================
    #  обзоры
    def open_reviews_widget(self):
        reviews_widget_button = self.browser.find_element(*WidgetLocators.Reviews_widget_button)
        reviews_widget_button.click()

    def should_be_card_reviews(self):
        assert self.is_element_present(*WidgetLocators.Card_name_reviews), "element is not presented"

    def should_be_reviews_button_settings(self):
        assert self.is_element_present(*WidgetLocators.Reviews_button_settings), "element is not presented"

    def should_be_reviews_button_cross(self):
        assert self.is_element_present(*WidgetLocators.Reviews_button_cross), "element is not presented"

    # Отображается текст для обзоров если в карточке их "0"
    def should_be_displayed_text(self):
        assert self.is_element_present(*WidgetLocators.Reviews_displayed_text), "text is not presented"

    # Возвращает текст для карточки у которой "0" обзоров
    def reviews_return_text_zero_reviews(self):
        text_zero_reviews = self.browser.find_element(*WidgetLocators.Reviews_displayed_text).text
        return text_zero_reviews

    # Количество обзоров - виджет
    def value_reviews(self):
        value_reviews = self.browser.find_element(*WidgetLocators.Value_Reviews).text
        return int(value_reviews)

    # Выбрать случайный обзор
    def choose_random_review(self):
        value_reviews = self.browser.find_element(*WidgetLocators.Value_Reviews).text
        random_index = random.randrange(int(value_reviews))
        return random_index

    # Найти в списке случайный обзор
    def scroll_to_random_review(self, index):
        reviews_images = self.browser.find_elements(*WidgetLocators.Value_Reviews_Images)
        while index >= len(reviews_images):
            image = reviews_images[-1]
            # self.browser.execute_script("arguments[0].scrollIntoView(true);", image)
            actions = ActionChains(self.browser)
            actions.move_to_element(image).perform()
            scroll_origin = ScrollOrigin.from_element(image)
            ActionChains(self.browser).scroll_from_origin(scroll_origin, 0, 100).perform()
            time.sleep(1)
            reviews_images = self.browser.find_elements(*WidgetLocators.Value_Reviews_Images)
        if index in range(len(reviews_images)):
            image = reviews_images[index]
            # self.browser.execute_script("arguments[0].scrollIntoView(true);", image)
            actions = ActionChains(self.browser)
            actions.move_to_element(image).perform()
            random_review = reviews_images[index - 1]
            # random_review.click()
            return random_review

    def open_random_review(self, review):
        review.click()

    def should_be_displayed_overview(self):
        assert self.is_element_present(*WidgetLocators.Overview_is_displayed), "Overview is not displayed"

    # Количество изображений обзоров в карточке [Обзоры]
    def value_reviews_images(self):
        images_list = []
        reviews_images = self.browser.find_elements(*WidgetLocators.Value_Reviews_Images)
        for image in reviews_images:
            images_list.append(image)
        return len(images_list)

    # Количество итераций для функции "scroll_reviews"
    def value_iterations(self):
        value_reviews = self.browser.find_element(*WidgetLocators.Value_Reviews).text
        value = int(value_reviews)
        iteration_value = int(value / 50)
        return iteration_value

    def scroll_reviews(self, iteration_value):
        reviews_images = self.browser.find_elements(*WidgetLocators.Value_Reviews_Images)
        x = 0
        while x <= iteration_value:
            for image in reviews_images:
                if image == reviews_images[-1]:
                    self.browser.execute_script("arguments[0].scrollIntoView(true);", image)
                    time.sleep(0.5)
            reviews_images = self.browser.find_elements(*WidgetLocators.Value_Reviews_Images)
            x += 1
        return len(reviews_images)

    # ======================================================================================================================
    #  похожие
    def open_similar_widget(self):
        similar_widget_button = self.browser.find_element(*WidgetLocators.Similar_widget_button)
        similar_widget_button.click()

    def should_be_card_similar(self):
        assert self.is_element_present(*WidgetLocators.Card_name_similar), "element is not presented"

    def should_similar_be_drop_down_sort(self):
        assert self.is_element_present(*WidgetLocators.Similar_drop_down_sort), "element is not presented"

    def should_be_similar_button_settings(self):
        assert self.is_element_present(*WidgetLocators.Similar_button_settings), "element is not presented"

    def should_be_similar_button_cross(self):
        assert self.is_element_present(*WidgetLocators.Similar_button_cross), "element is not presented"

    # Значение похожих товаров на виджите
    def value_similar_products(self):
        value_similar_products = self.browser.find_element(*WidgetLocators.Value_similar_products).text
        return int(value_similar_products)

    # Количество продуктов в карточке [Похожие]
    def get_value_similar_products(self):
        similar_products = self.browser.find_elements(*WidgetLocators.Similar_products)
        return len(similar_products)

    def choose_random_product(self):
        similar_products = self.browser.find_elements(*WidgetLocators.Similar_products)
        random_index = random.randrange(len(similar_products))
        return random_index

    def open_random_product(self, random_index):
        similar_products = self.browser.find_elements(*WidgetLocators.Similar_products)
        for i in range(len(similar_products)):
            if i == random_index:
                actions = ActionChains(self.browser)
                actions.move_to_element(similar_products[i]).perform()
                product = similar_products[i]
                product.click()

    def get_url_random_product(self, random_index):
        similar_products = self.browser.find_elements(*WidgetLocators.Similar_products_for_url)
        for i in range(len(similar_products)):
            if i == random_index:
                url = similar_products[i].get_attribute("href")
                return url.split('.html')[0]

    def get_price_random_product(self, random_index):
        prices = self.browser.find_elements(*WidgetLocators.Similar_products_price)
        for i in range(len(prices)):
            if i == random_index:
                actions = ActionChains(self.browser)
                actions.move_to_element(prices[i]).perform()
                price = prices[i].text
                if "US" in price:
                    price = price.translate({ord(i): None for i in ' руб$€¥₽US'})
                if "руб" in price:
                    price = price.translate({ord(i): None for i in ' руб.$€¥₽US'})
                    price = price.replace(",", ".")
                if "€" in price:
                    price = price.translate({ord(i): None for i in ' руб$€¥₽US'})
                    price = price.replace(",", ".")
                return float(price)

    # Проверка сортировки по цене
    def check_sorting_by_price(self):
        prices = self.browser.find_elements(*WidgetLocators.Products_price_sorted_by_price)
        for i in range(len(prices) - 1):
            price0 = prices[i].text
            price0 = "".join(c for c in price0 if c.isdecimal())
            self.browser.execute_script("arguments[0].scrollIntoView(true);", prices[i + 1])
            price1 = prices[i + 1].text
            price1 = "".join(c for c in price1 if c.isdecimal())
            # print(price0, price1)
            assert int(price0) <= int(price1), f"Ошибка сортировки цены товара, {price0} не меньше {price1} "

    # Проверка сортировки по заказам
    def check_sorting_by_orders(self):
        message = self.is_not_element_present(*WidgetLocators.Similar_message_displayed)
        if message is True:
            orders_list1 = self.browser.find_elements(*WidgetLocators.Similar_products_orders1)
            orders = orders_list1
        else:
            orders_list2 = self.browser.find_elements(*WidgetLocators.Similar_products_orders2)
            orders = orders_list2
        for i in range(len(orders) - 1):
            orders0 = orders[i].text
            orders0 = "".join(c for c in orders0 if c.isdecimal())
            self.browser.execute_script("arguments[0].scrollIntoView(true);", orders[i + 1])
            orders1 = orders[i + 1].text
            orders1 = "".join(c for c in orders1 if c.isdecimal())
            # print(orders0, orders1)
            assert int(orders0) >= int(
                orders1), f"Ошибка сортировки по количеству заказов, {orders0} меньше чем {orders1} "

    # Открыть drop_down "Сортировать"
    def open_drop_down_for_similar(self):
        drop_down_sort = self.browser.find_element(*WidgetLocators.Similar_drop_down_sort)
        drop_down_sort.click()

    def select_drop_down_values_price(self):
        drop_down_values = self.browser.find_elements(*WidgetLocators.Drop_down_values_1_2_3)
        for i in range(len(drop_down_values)):
            if i == 1:
                sort_by_price = drop_down_values[1]
                sort_by_price.click()

    def select_drop_down_values_orders(self):
        drop_down_values = self.browser.find_elements(*WidgetLocators.Drop_down_values_1_2_3)
        for i in range(len(drop_down_values)):
            if i == 2:
                sort_by_orders = drop_down_values[2]
                sort_by_orders.click()

    def select_drop_down_without_sorting(self):
        drop_down_values = self.browser.find_elements(*WidgetLocators.Drop_down_values_1_2_3)
        for i in range(len(drop_down_values)):
            if i == 0:
                without_sorting = drop_down_values[0]
                without_sorting.click()

    # ======================================================================================================================
    #   история
    def open_history_widget(self):
        history_widget_button = self.browser.find_element(*WidgetLocators.History_widget_button)
        history_widget_button.click()

    def should_be_history_collapse_button(self):
        assert self.is_element_present(*WidgetLocators.History_widget_collapse_button), "element is not presented"

    def should_be_card_history(self):
        assert self.is_element_present(*WidgetLocators.Card_name_history), "element is not presented"

    def should_be_history_button_context_menu(self):
        assert self.is_element_present(*WidgetLocators.History_widget_control_context_menu), "element is not presented"

    def should_be_history_button_cross(self):
        assert self.is_element_present(*WidgetLocators.History_button_cross), "element is not presented"

    def should_be_history_text_today(self):
        assert self.is_element_present(*WidgetLocators.History_text_today), "element is not presented"

    #  Открыть продукт из виджета "История"
    def open_product_from_history_widget(self):
        product_one = self.browser.find_element(*WidgetLocators.Product_in_history_for_widget)
        product_one.click()

    def should_be_card_of_product(self):
        assert self.is_element_present(
            *WidgetLocators.Product_in_history_for_widget), f"Карточка товара не отображается"

    def collapse_history(self):
        collapse_history_button = self.browser.find_element(*WidgetLocators.History_widget_collapse_button)
        collapse_history_button.click()

    def expand_history(self):
        expand_history_button = self.browser.find_element(*WidgetLocators.History_widget_expand_button)
        expand_history_button.click()

    def product_from_history_widget_not_displayed(self):
        product_one = self.browser.find_element(*WidgetLocators.Product_in_history_for_widget)
        assert product_one.is_displayed() is False, f"Карточка товара отображается"

    def product_from_history_widget_displayed(self):
        product_one = self.browser.find_element(*WidgetLocators.Product_in_history_for_widget)
        assert product_one.is_displayed() is True, f"Карточка товара не отображается"

    def list_products_from_history_widget(self):
        list_of_products = []
        products = self.browser.find_elements(*WidgetLocators.Product_in_history_for_widget)
        for product in products:
            product = product.get_attribute("href")
            list_of_products.append(product.split('?')[0])
        return list_of_products

    def open_product_list(self, list_product):
        for i in list_product:
            url = list_product[i]
            self.browser.get("https://www.aliexpress.com/item/" + url)
            window = self.browser.window_handles
            self.browser.switch_to.window(window[1])
            time.sleep(2)

    def max_number_of_products_in_history_widget(self, list_product):
        maximum_number_of_products = len(list_product)
        assert maximum_number_of_products == 4, f"Количеcтсво товаров равно: {maximum_number_of_products}, а не 4"

    def hover_on_product_card(self):
        product_card = self.browser.find_element(*WidgetLocators.Product_card_from_the_history)
        hover = ActionChains(self.browser).move_to_element(product_card)
        hover.perform()

    def should_be_button_cross(self):
        assert self.is_element_present(*WidgetLocators.Button_cross_for_history_card), f"Иконка крестик не отображается"

    def remove_product_card_from_history(self):
        cross = self.browser.find_element(*WidgetLocators.Button_cross_for_history_card)
        cross.click()

    def should_be_empty_text(self):
        empty_text = self.browser.find_element(*WidgetLocators.Empty_title_history_card).text
        assert empty_text == "Здесь будут товары,\nкоторые вы просматривали\nна AliExpress.", f"Тексты не совпадают"

    def open_history_widget_context_menu(self):
        history_widget_context_menu = self.browser.find_element(*WidgetLocators.History_widget_control_context_menu)
        history_widget_context_menu.click()

    def open_history_settings(self):
        customize_history_button = self.browser.find_element(*WidgetLocators.Customize_history_button)
        customize_history_button.click()

    def do_not_show_history_on_this_site(self):
        do_not_show_on_this_site_button = self.browser.find_element(*WidgetLocators.Do_not_show_on_this_site_button)
        do_not_show_on_this_site_button.click()

    def not_should_be_history_widget_button(self):
        history_widget_button = self.is_not_element_present(*WidgetLocators.History_widget_button)
        assert history_widget_button is True, f"Виджет [История] отображается"

    # Открыть продукт из карточки виджета "История"
    def open_product_from_card_of_widget_history(self):
        product_card = self.browser.find_element(*WidgetLocators.Product_card_from_the_history)
        product_card.click()

    # ======================================================================================================================
    # Переводы кнопок виджета
    def translation_check_for_widget(self, language):
        if language == "ru":
            price_button = self.browser.find_element(*WidgetLocators.Price_widget_button).text
            assert price_button == "цена", f"Ошибка, вернулось название кнопки {price_button}, для {language}"
        if language == "en":
            price_button = self.browser.find_element(*WidgetLocators.Price_widget_button).text
            assert price_button == "price", f"Ошибка, вернулось название кнопки {price_button}, для {language}"
            seller_button = self.browser.find_element(*WidgetLocators.Seller_widget_button).text
            assert seller_button == "seller", f"Ошибка, вернулось название кнопки {seller_button}, для {language}"
            reviews_button = self.browser.find_element(*WidgetLocators.Reviews_widget_button).text
            assert reviews_button == "reviews", f"Ошибка, вернулось название кнопки {reviews_button}, для {language}"
            similar_button = self.browser.find_element(*WidgetLocators.Similar_widget_button).text
            assert similar_button == "similar", f"Ошибка, вернулось название кнопки {similar_button}, для {language}"
            history_button = self.browser.find_element(*WidgetLocators.History_widget_button).text
            assert history_button == "history", f"Ошибка, вернулось название кнопки {history_button}, для {language}"

        if language == "pl":
            price_button = self.browser.find_element(*WidgetLocators.Price_widget_button).text
            assert price_button == "cena", f"Ошибка, вернулось название кнопки {price_button}, для {language}"
            seller_button = self.browser.find_element(*WidgetLocators.Seller_widget_button).text
            assert seller_button == "sprzedawca", f"Ошибка, вернулось название кнопки {seller_button}, для {language}"
            reviews_button = self.browser.find_element(*WidgetLocators.Reviews_widget_button).text
            assert reviews_button == "recenzje", f"Ошибка, вернулось название кнопки {reviews_button}, для {language}"
            similar_button = self.browser.find_element(*WidgetLocators.Similar_widget_button).text
            assert similar_button == "podobne", f"Ошибка, вернулось название кнопки {similar_button}, для {language}"
            history_button = self.browser.find_element(*WidgetLocators.History_widget_button).text
            assert history_button == "history", f"Ошибка, вернулось название кнопки {history_button}, для {language}"

        if language == "es":
            price_button = self.browser.find_element(*WidgetLocators.Price_widget_button).text
            assert price_button == "precio", f"Ошибка, вернулось название кнопки {price_button}, для {language}"
            seller_button = self.browser.find_element(*WidgetLocators.Seller_widget_button).text
            assert seller_button == "vendedor", f"Ошибка, вернулось название кнопки {seller_button}, для {language}"
            reviews_button = self.browser.find_element(*WidgetLocators.Reviews_widget_button).text
            assert reviews_button == "opiniones", f"Ошибка, вернулось название кнопки {reviews_button}, для {language}"
            similar_button = self.browser.find_element(*WidgetLocators.Similar_widget_button).text
            assert similar_button == "similares", f"Ошибка, вернулось название кнопки {similar_button}, для {language}"
            history_button = self.browser.find_element(*WidgetLocators.History_widget_button).text
            assert history_button == "history", f"Ошибка, вернулось название кнопки {history_button}, для {language}"

        if language == "fr":
            price_button = self.browser.find_element(*WidgetLocators.Price_widget_button).text
            assert price_button == "prix", f"Ошибка, вернулось название кнопки {price_button}, для {language}"
            seller_button = self.browser.find_element(*WidgetLocators.Seller_widget_button).text
            assert seller_button == "vendeur", f"Ошибка, вернулось название кнопки {seller_button}, для {language}"
            reviews_button = self.browser.find_element(*WidgetLocators.Reviews_widget_button).text
            assert reviews_button == "revues", f"Ошибка, вернулось название кнопки {reviews_button}, для {language}"
            similar_button = self.browser.find_element(*WidgetLocators.Similar_widget_button).text
            assert similar_button == "similaires", f"Ошибка, вернулось название кнопки {similar_button}, для {language}"
            history_button = self.browser.find_element(*WidgetLocators.History_widget_button).text
            assert history_button == "history", f"Ошибка, вернулось название кнопки {history_button}, для {language}"

        if language == "pt":
            price_button = self.browser.find_element(*WidgetLocators.Price_widget_button).text
            assert price_button == "preço", \
                f"Ошибка, вернулось название кнопки {price_button}, для {language} "
            seller_button = self.browser.find_element(*WidgetLocators.Seller_widget_button).text
            assert seller_button == "vendedor", f"Ошибка, вернулось название кнопки {seller_button}, для {language}"
            reviews_button = self.browser.find_element(*WidgetLocators.Reviews_widget_button).text
            assert reviews_button == "comentários", f"Ошибка, вернулось название кнопки {reviews_button}, для {language}"
            similar_button = self.browser.find_element(*WidgetLocators.Similar_widget_button).text
            assert similar_button == "semelhantes", f"Ошибка, вернулось название кнопки {similar_button}, для {language}"
            history_button = self.browser.find_element(*WidgetLocators.History_widget_button).text
            assert history_button == "histórico", f"Ошибка, вернулось название кнопки {history_button}, для {language}"
# ======================================================================================================================
