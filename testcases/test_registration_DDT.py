import pytest
import os
from pages.registration_page import RegistrationPage
from pages.login_page import LoginPage
from utilities.data_provider import read_excel_data

path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "testdata", "data_for_registration.xlsx"))

@pytest.mark.parametrize('registration_data',read_excel_data(path,"Sheet1"))
def test_user_registration(setup,registration_data):
    data = registration_data
    driver = setup
    reg_page = RegistrationPage(driver)
    login_pg = LoginPage(driver)

    login_pg.click_register()
    reg_page.enter_first_name(data[0])
    reg_page.enter_last_name(data[1])
    reg_page.enter_email(data[2])
    reg_page.enter_phone(data[3])
    reg_page.choose_occupation(data[4])
    reg_page.choose_gender(data[5])
    reg_page.enter_password(data[6])
    reg_page.confirm_password(data[7])
    reg_page.check_age_greater_than_18()
    reg_page.click_register()
    assert reg_page.registration_successful()
