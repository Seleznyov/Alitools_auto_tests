import pytest
from .pages.widget_page import WidgetPage
from .pages.base_page import BasePage


@pytest.fixture(scope="function", autouse=True)
def setup(browser):
    url = "https://alitools.io/ru"
    browser.get(url)
    page = BasePage(browser, browser.current_url)
    page.switch_to_window(1)
    if browser.name == "firefox":
        page = WidgetPage(browser, browser.current_url)
        page.setup_firefox()
        page.switch_to_window(1)


def test_greetings(browser):
    page = BasePage(browser, browser.current_url)
    # Проверка откуда вы узнали о расширении
    page.should_be_option_start()
    # Проверка отображения приветствия
    page.should_be_greetings()


def test_widget_price_view(browser):
    page = WidgetPage(browser, browser.current_url)
    # Проверка откуда вы узнали о расширении
    page.should_be_option_start()
    # Открыть "цена"
    page.open_price_widget()
    # Отображается ли имя карточки "История цены"
    page.should_be_card_price()
    # Отображается ли drop-down "за 3 месяца"
    page.should_be_price_drop_down_for_3_months()
    # Отображается ли кнопка [Точная]
    page.should_be_price_button_accurate()
    # Отображается ли кнопка [Средняя]
    page.should_be_price_button_average()
    # Отображается ли кнопка [Следить за товаром']
    page.should_be_price_button_follow_the_item()
    # Отображается ли иконка инфо
    page.should_be_price_button_info()
    # Отображается ли иконка настройки
    page.should_be_price_button_settings()
    # Отображается ли иконка закрыть [X]
    page.should_be_price_button_cross()


def test_widget_seller_view(browser):
    page = WidgetPage(browser, browser.current_url)
    # Проверка откуда вы узнали о расширении
    page.should_be_option_start()
    # Открыть "продавец"
    page.open_seller_widget()
    # Отображается ли имя карточки "Рейтинг продавца"
    page.should_be_card_seller()
    # Отображается ли иконка настройки
    page.should_be_seller_button_settings()
    # Отображается ли иконка закрыть [X]
    page.should_be_seller_button_cross()


def test_widget_reviews_view(browser):
    page = WidgetPage(browser, browser.current_url)
    # Проверка откуда вы узнали о расширении
    page.should_be_option_start()
    # Открыть "обзоры"
    page.open_reviews_widget()
    # Отображается ли имя карточки "Обзоры"
    page.should_be_card_reviews()
    # Отображается ли иконка настройки
    page.should_be_reviews_button_settings()
    # Отображается ли иконка закрыть [X]
    page.should_be_reviews_button_cross()


def test_widget_similar_view(browser):
    page = WidgetPage(browser, browser.current_url)
    # Проверка откуда вы узнали о расширении
    page.should_be_option_start()
    # Открыть "похожие"
    page.open_similar_widget()
    # Отображается ли имя карточки "Похожие"
    page.should_be_card_similar()
    # Отображается ли drop-down "сортировать v"
    page.should_similar_be_drop_down_sort()
    # Отображается ли иконка настройки
    page.should_be_similar_button_settings()
    # Отображается ли иконка закрыть [X]
    page.should_be_similar_button_cross()


def test_widget_history_view(browser):
    page = WidgetPage(browser, browser.current_url)
    # Проверка откуда вы узнали о расширении
    page.should_be_option_start()
    # Закрываем приветствие
    page.click_on_cross_start_greeting()
    # Отображается ли кнопка "свернуть историю"
    page.should_be_history_collapse_button()
    # Открыть "история"
    page.open_history_widget()
    # Отображается ли имя карточки "История просмотров"
    page.should_be_card_history()
    # Отображается ли иконка "контекстного меню"
    page.should_be_history_button_context_menu()
    # Отображается ли иконка закрыть [X]
    page.should_be_history_button_cross()
    # Отображается ли текст 'сегодня'
    page.should_be_history_text_today()
