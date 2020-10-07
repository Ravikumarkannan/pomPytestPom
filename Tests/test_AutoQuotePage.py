import pytest

from Pages.AutoQuotePage import AutoQuotePage
from Resources.TestData import AutoQuoteTestData


class TestAutoQuotePage:

    @pytest.mark.run(order=5)
    def test_select_service(self, init_driver):
        autoquote = AutoQuotePage(init_driver)
        autoquote.select_service(AutoQuoteTestData.service)

    @pytest.mark.run(order=6)
    def test_enter_autoquote_info(self, init_driver):
        autoquote = AutoQuotePage(init_driver)
        autoquote.enter_autoquote_info(AutoQuoteTestData.zipcode, AutoQuoteTestData.email)
        autoquote.choose_automobile_type(AutoQuoteTestData.automobile_type)

    @pytest.mark.run(order=7)
    def test_enter_personal_details(self, init_driver):
        autoquote = AutoQuotePage(init_driver)
        autoquote.enter_personal_info(AutoQuoteTestData.age)

    @pytest.mark.run(order=8)
    def test_choose_automobile_info(self, init_driver):
        autoquote = AutoQuotePage(init_driver)
        autoquote.choose_automobile_info(AutoQuoteTestData.year)

    @pytest.mark.run(order=9)
    def test_validate_price(self, init_driver):
        autoquote = AutoQuotePage(init_driver)
        assert autoquote.get_quote_price() == AutoQuoteTestData.price

    @pytest.mark.run(order=10)
    def test_proceed_to_purchase(self, init_driver):
        autoquote = AutoQuotePage(init_driver)
        autoquote.proceed_to_purchase()
