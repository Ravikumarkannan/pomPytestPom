from Pages.BasePage import BasePage
from Locators.locators import HomePageLocator


class HomePage(BasePage):

    def select_service(self, service):
        self.drop_down(HomePageLocator.service_menu, service)

    def enter_autoquote_info(self, zipcode, email):
        self.send_keys(HomePageLocator.zipcode, zipcode)
        self.send_keys(HomePageLocator.email, email)

    def choose_automobile_type(self, automobile):
        enabled_status = None
        if automobile == "car":
            self.click_element(HomePageLocator.automobile_car)
            enabled_status = self.is_enabled(HomePageLocator.automobile_car)
        elif automobile == "truck":
            self.click_element(HomePageLocator.automobile_truck)
            enabled_status = self.is_enabled(HomePageLocator.automobile_truck)
        assert enabled_status

        self.click_element(HomePageLocator.next_btn)

    def enter_personal_info(self, age):
        self.send_keys(HomePageLocator.age, age)

        self.click_element(HomePageLocator.gender_male)
        assert self.is_enabled(HomePageLocator.gender_male)

        self.click_element(HomePageLocator.driving_record)
        assert self.is_enabled(HomePageLocator.driving_record)

        self.click_element(HomePageLocator.next_btn)

    def choose_automobile_info(self, year):
        self.send_keys(HomePageLocator.year, year)

        self.click_element(HomePageLocator.make)
        self.click_element(HomePageLocator.make_toyota)

        self.click_element(HomePageLocator.model)
        self.click_element(HomePageLocator.model_cross_fire)

        self.click_element(HomePageLocator.financial_info)
        self.click_element(HomePageLocator.next_btn)

    def get_quote_price(self):
        return self.get_element_text(HomePageLocator.price)