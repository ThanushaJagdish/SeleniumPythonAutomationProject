from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    select_country_input_box = (By.CSS_SELECTOR,"input[placeholder='Select Country']")
    search_results_dropdown = (By.XPATH,"//input[@placeholder='Select Country']/following-sibling::section//span")
    cvv_input_box = (By.XPATH,"//div[contains(text(),'CVV')]/following-sibling::input")
    name_on_card_input_box = (By.XPATH,"//div[normalize-space()='Name on Card']/following-sibling::input")
    place_order_button = (By.XPATH,"//a[normalize-space()='Place Order']")

    def select_country(self,user_text):
        # self.enter_value(self.select_country_input_box,user_text)
        # search_results = self.wait_for_elements_to_be_visible(self.search_results_dropdown)
        # for result in search_results:
        #     country_name = result.text
        #     if country_name == "India":
        #         self.safe_click(result)
        self.enter_value(self.select_country_input_box, user_text)

        self.wait_for_elements_to_be_visible(self.search_results_dropdown)

        results = self.driver.find_elements(*self.search_results_dropdown)

        for i in range(len(results)):
            result = self.driver.find_elements(*self.search_results_dropdown)[i]
            if result.text.strip() == "India":
                result.click()
                return

    def enter_cvv(self,cvv):
        self.enter_value(self.cvv_input_box,cvv)

    def enter_name(self,name):
        self.enter_value(self.name_on_card_input_box,name)

    def click_place_order(self):
        self.safe_click(self.place_order_button)



