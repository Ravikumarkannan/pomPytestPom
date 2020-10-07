from Pages.BasePage import BasePage
from Locators.locators import LoginPageLocators
from Resources.config import Configuration


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        driver.get(Configuration.BASE_URL)

    def validate_login_page_title(self, title):
        return self.get_page_title(title)

    def do_login(self, email, password):
        self.send_keys(LoginPageLocators.user_email, email)
        self.send_keys(LoginPageLocators.user_password, password)
        self.click_element(LoginPageLocators.login_btn)
