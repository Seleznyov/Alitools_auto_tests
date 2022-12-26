import datetime
import time
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, browser, url, timeout=3):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def should_be_option_start(self):
        questionnaire = self.is_not_element_present(*BasePageLocators.Possible_answer)
        if questionnaire is False:
            cross_option_start = self.browser.find_element(*BasePageLocators.Cross_start_greeting)
            cross_option_start.click()

    def should_be_greetings(self):
        try:
            WebDriverWait(self.browser, 20).until(EC.presence_of_element_located((By.XPATH, BasePageLocators.Greeting)))
        except TimeoutException:
            pytest.skip("Не успел отобразиться стартовый элемент Приветствие")
        assert self.is_element_present(*BasePageLocators.Starting_greeting), "element is not presented"

    def click_on_cross_start_greeting(self):
        try:
            WebDriverWait(self.browser, 25).until(EC.presence_of_element_located((By.XPATH, BasePageLocators.Cross_start)))
            time.sleep(0.5)
        except TimeoutException:
            pytest.skip("Не успел отобразиться стартовый элемент [x]")
        cross_start_greeting = self.browser.find_element(*BasePageLocators.Cross_start_greeting)
        cross_start_greeting.click()

    def click_on_cress_repeated_favorites(self):
        cross_repeated_favorites = self.browser.find_element(*BasePageLocators.Cross_repeated_favorites)
        cross_repeated_favorites.click()

    # Добработать
    def close_warning(self):
        close = self.browser.find_element(*BasePageLocators.Dialog_close)
        close.click()
        # ActionChains(self.browser).click_and_hold(source).move_by_offset(300, 0)
        # ActionChains(self.browser).drag_and_drop_by_offset(source, 300, 0).perform()

        # Добработать
    def hold_and_move_section_to_down(self):
        source = self.browser.find_element(*BasePageLocators.Slider)
        ActionChains(self.browser).drag_and_drop_by_offset(source, 300, 0).perform()
        # Второй вариант
        # ActionChains(self.browser).click_and_hold(source).move_by_offset(300, 0)
        errloading = self.is_not_element_present(*BasePageLocators.Errloading)
        if errloading is False:
            err = self.browser.find_element(*BasePageLocators.Errloading)
            err.click()
            time.sleep(1)
            source = self.browser.find_element(*BasePageLocators.Slider)
            ActionChains(self.browser).drag_and_drop_by_offset(source, 300, 0).perform()

    def check_warning_text(self):
        warning_text = self.is_not_element_present(*BasePageLocators.Warning_text)
        return warning_text

    def screenshot_page(self, directory_name, name="test"):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = name+"_screenshot_" + now_date + ".png"
        self.browser.save_screenshot("D:\\Alitools_auto_tests\\screenshot\\" + directory_name + "\\" + name_screenshot)

    def get_usd_course(self):
        url = "https://moneyfromnothing.ru/blog/aliexpress-kurs-dollara/"
        self.browser.get(url)
        usd_courses = self.browser.find_elements(*BasePageLocators.Usd_course_aliExpress_global)
        for i in range(len(usd_courses)):
            self.browser.execute_script("arguments[0].scrollIntoView(true);", usd_courses[1])
            usd_course = usd_courses[1].text
            usd_course = usd_course[:5]
            return float(usd_course)

    def setup_firefox(self):
        setup_firefox = self.browser.find_element(*BasePageLocators.Setup_firefox)
        setup_firefox.click()

    def refresh_page(self):
        self.browser.refresh()

    def cleared_list(self, new_list):
        list_without_dots = []
        for i in new_list:
            x = i.split(".")
            list_without_dots.append(x[0])
        return list_without_dots

    def switch_to_window(self, number):
        window2 = self.browser.window_handles
        self.browser.switch_to.window(window2[number])

    def page_domain(self):
        url_page = self.browser.current_url
        page_domain = url_page.split("/")
        return page_domain

    # Ждем загрузку страницы
    def page_loading(self):
        time.sleep(5)
        WebDriverWait(self.browser, 10).until(
            lambda browser: self.browser.execute_script('return document.readyState') == 'complete')

