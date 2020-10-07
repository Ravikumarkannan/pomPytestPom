import pytest

from Pages.PurchasePage import PurchasePage
from Resources.TestData import PurchaseTestData


class TestPurchase:

    @pytest.mark.run(order=11)
    def test_validate_credit_card_name(self, init_driver):
        purchase = PurchasePage(init_driver)
        purchase.get_credit_card_name(PurchaseTestData.credit_card_name)

    @pytest.mark.run(order=12)
    def test_enter_credit_card_details(self, init_driver):
        purchase = PurchasePage(init_driver)
        purchase.enter_credit_card_info(PurchaseTestData.credit_cart_number, PurchaseTestData.expiration_date)
        purchase.click_purchase_button()
