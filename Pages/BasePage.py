from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

"""This class is base class of all pages"""


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, by_locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).click()

    def send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).send_keys(text)

    def get_page_title(self, expected_title):
        WebDriverWait(self.driver, 10).until(ec.title_is(expected_title))
        assert self.driver.title == expected_title

    def get_element_text(self, by_locator):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).text

    def drop_down(self, menu_locator, submenu):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(menu_locator))
        select = Select(element)
        select.select_by_visible_text(submenu)

    def is_enabled(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        return element.is_enabled()
