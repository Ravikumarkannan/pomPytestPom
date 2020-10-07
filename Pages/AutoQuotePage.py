from Pages.BasePage import BasePage
from Locators.locators import AutoQuoteLocators


class AutoQuotePage(BasePage):

    def select_service(self, service):
        self.drop_down(AutoQuoteLocators.service_menu, service)

    def enter_autoquote_info(self, zipcode, email):
        self.send_keys(AutoQuoteLocators.zipcode, zipcode)
        self.send_keys(AutoQuoteLocators.email, email)

    def choose_automobile_type(self, automobile):
        enabled_status = None
        if automobile == "car":
            self.click_element(AutoQuoteLocators.automobile_car)
            enabled_status = self.is_enabled(AutoQuoteLocators.automobile_car)
        elif automobile == "truck":
            self.click_element(AutoQuoteLocators.automobile_truck)
            enabled_status = self.is_enabled(AutoQuoteLocators.automobile_truck)
        assert enabled_status
        print(f"automobile enabled status: {enabled_status}")

        self.click_element(AutoQuoteLocators.next_btn)

    def enter_personal_info(self, age):
        self.send_keys(AutoQuoteLocators.age, age)

        self.click_element(AutoQuoteLocators.gender_male)
        assert self.is_enabled(AutoQuoteLocators.gender_male)
        print(f"gender enabled status: {self.is_enabled(AutoQuoteLocators.gender_male)}")

        self.click_element(AutoQuoteLocators.driving_record)
        assert self.is_enabled(AutoQuoteLocators.driving_record)
        print(f"driving record enabled status : {self.is_enabled(AutoQuoteLocators.driving_record)}")

        self.click_element(AutoQuoteLocators.next_btn)

    def choose_automobile_info(self, year):
        self.send_keys(AutoQuoteLocators.year, year)

        self.click_element(AutoQuoteLocators.make)
        self.click_element(AutoQuoteLocators.make_toyota)

        self.click_element(AutoQuoteLocators.model)
        self.click_element(AutoQuoteLocators.model_cross_fire)

        self.click_element(AutoQuoteLocators.financial_info)
        self.click_element(AutoQuoteLocators.next_btn)

    def get_quote_price(self):
        return self.get_element_text(AutoQuoteLocators.price)

    def proceed_to_purchase(self):
        self.click_element(AutoQuoteLocators.purchase_btn)