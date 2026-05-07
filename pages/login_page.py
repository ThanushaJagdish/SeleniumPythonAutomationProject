from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    email_input = (By.ID, "userEmail")
    password_input = (By.ID, "userPassword")
    login_button = (By.ID, "login")
    input_error = (By.CSS_SELECTOR, "div.invalid-feedback")
    pop_error = (By.CSS_SELECTOR,"div#toast-container")
    register_button = (By.LINK_TEXT, "Register here")

    def login(self, email, password):
        self.enter_value(self.email_input, email)
        self.enter_value(self.password_input, password)
        self.safe_click(self.login_button)

    def invalid_username_msg_displayed(self):
        return self.get_text(self.input_error)=="*Enter Valid Email"

    def invalid_email_or_password_msg_displayed(self):
        return self.get_text(self.pop_error)=="Incorrect email or password."

    def click_register(self):
        self.safe_click(self.register_button)