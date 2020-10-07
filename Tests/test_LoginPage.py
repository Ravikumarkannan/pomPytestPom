import pytest

from Pages.LoginPage import LoginPage
from Resources.TestData import LoginTestData


class TestLogin:

    @pytest.mark.run(order=1)
    def test_verify_page_title(self, init_driver):
        login = LoginPage(init_driver)
        login.validate_login_page_title(LoginTestData.login_page_title)

    @pytest.mark.run(order=2)
    def test_login(self, init_driver):
        login = LoginPage(init_driver)
        login.do_login(LoginTestData.email, LoginTestData.password)