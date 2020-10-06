import pytest

from Pages.HomePage import HomePage
from Config.TestData import HomePageTestData


class TestHomePage:

    @pytest.mark.run(order=4)
    def test_select_service(self, init_driver):
        home_page = HomePage(init_driver)
        home_page.select_service(HomePageTestData.service)

    @pytest.mark.run(order=5)
    def test_enter_autoquote_info(self, init_driver):
        home_page = HomePage(init_driver)
        home_page.enter_autoquote_info(HomePageTestData.zipcode, HomePageTestData.email)
        home_page.choose_automobile_type(HomePageTestData.automobile_type)

    @pytest.mark.run(order=6)
    def test_enter_personal_details(self, init_driver):
        home_page = HomePage(init_driver)
        home_page.enter_personal_info(HomePageTestData.age)

    @pytest.mark.run(order=7)
    def test_choose_automobile_info(self, init_driver):
        home_page = HomePage(init_driver)
        home_page.choose_automobile_info(HomePageTestData.year)

    @pytest.mark.run(order=8)
    def test_validate_price(self, init_driver):
        home_page = HomePage(init_driver)
        assert home_page.get_quote_price() == HomePageTestData.price
