from selenium import webdriver
import pytest
from Config.config import Configuration


@pytest.fixture(params=["chrome"], scope='session')
def init_driver(request):

    if request.param == "chrome":
        driver = webdriver.Chrome(Configuration.CHROME_EXECUTABLE_PATH)
    driver.maximize_window()
    driver.implicitly_wait(30)
    return driver
