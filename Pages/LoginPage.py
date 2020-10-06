from Pages.BasePage import BasePage
from Locators.locators import LoginPageLocators
from Config.config import Configuration


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        driver.get(Configuration.BASE_URL)

    def get_login_page_title(self, title):
        return self.get_page_title(title)

    def do_login(self, email, password):
        self.send_keys(LoginPageLocators.user_email, email)
        self.send_keys(LoginPageLocators.user_password, password)
        self.click_element(LoginPageLocators.login_btn)

    def verify_login(self, user_name):
        assert self.get_element_text(LoginPageLocators.user_name) == user_name