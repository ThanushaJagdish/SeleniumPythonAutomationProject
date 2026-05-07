from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckOutSuccessPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    order_placed_txt = (By.XPATH,"//h1[normalize-space()='Thankyou for the order.']")

    def order_successful_message(self):
        return self.wait_for_element_to_be_visible(self.order_placed_txt).is_displayed()

