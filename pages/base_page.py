from time import sleep

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)
        sleep(2)

    def element_not_present(self, how, what):
        return WebDriverWait(self.browser, timeout=4).until_not(EC.presence_of_element_located((how, what)))


    def get_element_present(self, how, what):
        try:
            element = WebDriverWait(self.browser, timeout=4).until(EC.presence_of_element_located((how, what)))
        except NoSuchElementException:
            return False
        return element

        # try:
        #     object = self.browser.find_element(how, what)
        # except NoSuchElementException:
        #     return False
        # return object

    def get_element_presents(self, how, what):
        try:
            elements = self.browser.find_elements(how, what)
        except NoSuchElementException:
            return False
        return elements