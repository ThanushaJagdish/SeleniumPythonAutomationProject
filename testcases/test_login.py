from pages.login_page import LoginPage
from utilities.config_reader import ConfigReader
from utilities.customLogger import LogGen

config = ConfigReader()
logger=LogGen.loggen()
username = config.get_username()
password = config.get_password()

def test_login_valid_user(setup):
    logger.info("Test Login with valid username and password")
    driver = setup
    login_page = LoginPage(driver)
    login_page.login(username,password)
    login_page.wait_for_url_contains("dashboard")
    logger.info("Login successful")
    assert "dashboard" in driver.current_url.lower()


def test_login_with_invalid_password(setup):
    logger.info("Test Login with valid username but invalid password")
    driver = setup
    login_page = LoginPage(driver)
    login_page.login(username,"123")
    assert login_page.invalid_email_or_password_msg_displayed()

def test_login_with_invalid_username(setup):
    logger.info("Test Login with invalid username")
    driver = setup
    login_page = LoginPage(driver)
    login_page.login("Abc",password)
    assert login_page.invalid_username_msg_displayed()

