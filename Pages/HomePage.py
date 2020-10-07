from Pages.BasePage import BasePage
from Locators.locators import HomepageLocators


class HomePage(BasePage):

    def verify_login(self, user_name):
        assert self.get_element_text(HomepageLocators.user_name) == user_name

    def is_details_button_exists(self):
        assert self.is_element_exists(HomepageLocators.details_btn)

    def is_logout_button_exists(self):
        assert self.is_element_exists(HomepageLocators.logout_btn)