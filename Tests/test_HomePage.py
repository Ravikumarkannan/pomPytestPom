import pytest
from Pages.HomePage import HomePage
from Resources.TestData import HomePageTestData


class TestHomePage:

    @pytest.mark.run(order=3)
    def test_verify_login(self, init_driver):
        homepage = HomePage(init_driver)
        homepage.verify_login(HomePageTestData.user_name)

    @pytest.mark.run(order=4)
    def test_validate_buttons(self, init_driver):
        homepage = HomePage(init_driver)

        homepage.is_details_button_exists()
        homepage.is_logout_button_exists()
