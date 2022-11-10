from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=5):
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

    def is_not_element_present(self, how, what, timeout=3):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def should_be_option_start(self):
        questionnaire = self.is_not_element_present(*BasePageLocators.Possible_answer)
        if questionnaire is False:
            cross_option_start = self.browser.find_element(*BasePageLocators.Possible_answer)
            cross_option_start.click()

    def should_be_greetings(self):
        assert self.is_element_present(*BasePageLocators.Starting_greeting), "element is not presented"

    def click_on_cross_start_greeting(self):
        cross_start_greeting = self.browser.find_element(*BasePageLocators.Cross_start_greeting)
        cross_start_greeting.click()

    def click_on_cress_repeated_favorites(self):
        cross_repeated_favorites = self.browser.find_element(*BasePageLocators.Cross_repeated_favorites)
        cross_repeated_favorites.click()


