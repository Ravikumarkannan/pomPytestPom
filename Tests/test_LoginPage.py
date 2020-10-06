import pytest

from Pages.LoginPage import LoginPage
from Config.TestData import LoginTestData


class TestLogin:

    @pytest.mark.run(order=1)
    def test_verify_page_title(self, init_driver):
        self.login = LoginPage(init_driver)
        self.login.get_page_title(LoginTestData.login_page_title)

    @pytest.mark.run(order=2)
    def test_login(self, init_driver):
        self.login = LoginPage(init_driver)
        self.login.do_login(LoginTestData.email, LoginTestData.password)

    @pytest.mark.run(order=3)
    def test_verify_login(self, init_driver):
        self.login = LoginPage(init_driver)
        self.login.verify_login(LoginTestData.user_name)

