from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage

class RegistrationPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    txt_firstname = (By.ID,"firstName")
    txt_lastname = (By.ID,"lastName")
    txt_useremail = (By.ID,"userEmail")
    txt_userphone = (By.ID,"userMobile")
    txt_password = (By.ID,"userPassword")
    txt_confirm_password = (By.ID,"confirmPassword")
    select_occupation = (By.CSS_SELECTOR, "select[formcontrolname='occupation']")
    gender_radio_button_locators = (By.CSS_SELECTOR, "input[formcontrolname='gender']")
    age_greater_than_18_year_checkbox = (By.CSS_SELECTOR,"input[type='checkbox']")
    register_button = (By.NAME,"login")
    registered_successfully_msg = (By.XPATH,"//h1[text()='Account Created Successfully']")

    def enter_first_name(self,fname):
        self.enter_value(self.txt_firstname,fname)

    def enter_last_name(self,lname):
        self.enter_value(self.txt_lastname,lname)

    def enter_email(self,email):
        self.enter_value(self.txt_useremail,email)

    def enter_phone(self,phone):
        self.enter_value(self.txt_userphone,phone)

    def enter_password(self,password):
        self.enter_value(self.txt_password,password)

    def confirm_password(self,confirmpass):
        self.enter_value(self.txt_confirm_password,confirmpass)

    def choose_occupation(self,occupation):
        select_obj = Select(self.wait_for_element_to_be_clickable(self.select_occupation))
        select_obj.select_by_visible_text(occupation)

    def choose_gender(self,gender):
        genders = self.wait_for_elements_to_be_visible(self.gender_radio_button_locators)
        for gender_btn in genders:
            if gender_btn.get_attribute('value')==gender:
                gender_btn.click()
                break

    def check_age_greater_than_18(self):
        self.safe_click(self.age_greater_than_18_year_checkbox)

    def click_register(self):
        self.safe_click(self.register_button)

    def registration_successful(self):
        return self.wait_for_element_to_be_visible(self.registered_successfully_msg).is_displayed()



