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

    def should_be_price_button_cross(self):
        assert self.is_element_present(*WidgetLocators.Price_button_cross), "element is not presented"

# Значение точной цены на графике
    def exact_price(self):
        exact_price = self.browser.find_element(*WidgetLocators.Exact_price).text
        exact_price = exact_price.partition('.')[0]
        exact_price = "".join(c for c in exact_price if c.isdecimal())
        return int(exact_price)

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
            actions = ActionChains(self.browser)
            actions.move_to_element(image).perform()
            scroll_origin = ScrollOrigin.from_element(image)
            ActionChains(self.browser).scroll_from_origin(scroll_origin, 0, 100).perform()
            time.sleep(2)
            reviews_images = self.browser.find_elements(*WidgetLocators.Value_Reviews_Images)
        if index in range(len(reviews_images)):
            image = reviews_images[index]
            actions = ActionChains(self.browser)
            actions.move_to_element(image).perform()
            random_review = reviews_images[index-1]
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
                    actions = ActionChains(self.browser)
                    actions.move_to_element(image).perform()
                    scroll_origin = ScrollOrigin.from_element(image)
                    ActionChains(self.browser).scroll_from_origin(scroll_origin, 0, 100).perform()
                    time.sleep(2)
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
                price = "".join(c for c in price if c.isdecimal())
                return int(price)

# Проверка сортировки по цене
    def check_sorting_by_price(self):
        prices = self.browser.find_elements(*WidgetLocators.Products_price_sorted_by_price)
        for i in range(len(prices) - 1):
            price0 = prices[i].text
            price0 = "".join(c for c in price0 if c.isdecimal())
            actions = ActionChains(self.browser)
            actions.move_to_element(prices[i + 1]).perform()
            price1 = prices[i + 1].text
            price1 = "".join(c for c in price1 if c.isdecimal())
            # print(price0,price1)
            assert int(price0) <= int(price1), f"Ошибка сортировки цене товара, {price0} не меньше {price1} "

#Проверка сортировки по заказам
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
            actions = ActionChains(self.browser)
            actions.move_to_element(orders[i + 1]).perform()
            orders1 = orders[i + 1].text
            orders1 = "".join(c for c in orders1 if c.isdecimal())
            # print(orders0,orders1)
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

# Открыть продукт из виджета "История"
    def open_product_from_history_widget(self):
        product_one = self.browser.find_element(*WidgetLocators.Product_in_history_for_widget)
        product_one.click()

# ======================================================================================================================
