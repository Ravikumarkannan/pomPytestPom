from selenium.webdriver.common.by import By


class LoginPageLocators(object):

    user_email = (By.ID, "login-form:email")
    user_password = (By.ID, "login-form:password")
    login_btn = (By.ID, "login-form:login")
    user_name = (By.XPATH, "(//input[@value='logout-form']/following-sibling::div)[2]/child::label")


class HomePageLocator(object):

    service_menu = (By.ID, "quick-link:jump-menu")
    zipcode = (By.ID, "autoquote:zipcode")
    email = (By.ID, "autoquote:e-mail")
    automobile_car = (By.ID, "autoquote:vehicle:0")
    next_btn = (By.ID, "autoquote:next")
    automobile_truck = (By.ID, "autoquote:vehicle:1")
    age = (By.ID,"autoquote:age")
    gender_male = (By.ID, "autoquote:gender:0")
    gender_female = (By.ID, "autoquote:gender:1")
    driving_record = (By.ID, "autoquote:type:1")
    year = (By.ID, "autoquote:year")
    make = (By.ID, "ext-gen4")
    model = (By.ID, "ext-gen6")
    make_toyota = (By.XPATH, "(//div[@id='ext-gen8']/child::div)[4]")
    model_cross_fire = (By.XPATH, "(//div[@id='ext-gen12']/child::div)[3]")
    financial_info = (By.ID, "autoquote:finInfo:0")
    price = (By.XPATH, "(//h1)[2]/child::b")