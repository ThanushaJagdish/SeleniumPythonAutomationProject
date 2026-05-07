import pytest
from selenium import webdriver
from utilities.config_reader import ConfigReader
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.cart_page import CartPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

@pytest.fixture(scope="function")
def setup():
    config = ConfigReader()

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(config.get_base_url())

    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def logged_in_user(setup):
    driver = setup
    config = ConfigReader()

    login_page = LoginPage(driver)
    login_page.login(config.get_username(), config.get_password())

    WebDriverWait(driver, 10).until(
        EC.url_contains("dashboard")
    )

    return driver

@pytest.fixture(scope="function")
def search_product(logged_in_user):
    driver = logged_in_user
    search_pg = SearchPage(driver)
    search_pg.search("iphone")
    return driver

@pytest.fixture(scope="function")
def add_to_cart(logged_in_user):
    driver = logged_in_user
    search_pg = SearchPage(driver)
    search_pg.search("iphone")
    search_pg.add_product_to_cart('iphone 13 pro')
    cart_pg = CartPage(driver)
    cart_pg.wait_for_text_to_be_present(cart_pg.cart_button_label, "1")
    cart_pg.click_cart()
    return driver

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs["setup"]

        time = datetime.now().strftime("%Y%m%d_%H%M%S")

        driver.save_screenshot(
            f"screenshots/{item.name}_{time}.png"
        )
