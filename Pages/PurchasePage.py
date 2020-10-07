from Locators.locators import PurchaseLocators
from Pages.BasePage import BasePage
from Resources.TestData import PurchaseTestData


class PurchasePage(BasePage):

    def get_credit_card_name(self, expected_card_name):
        card_name = self.get_element_attribute(PurchaseLocators.credit_card_name, "value")
        assert card_name == expected_card_name

    def enter_credit_card_info(self, card_number, expiration_date):
        self.send_keys(PurchaseLocators.credit_card_number, card_number)
        self.send_keys(PurchaseLocators.expiration_date, expiration_date)

    def click_purchase_button(self):
        self.click_element(PurchaseLocators.purchase_quote)