from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_element_to_be_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_elements_to_be_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )

    def safe_click(self, locator):
        element = self.wait_for_element_to_be_clickable(locator)
        element.click()

    def enter_value(self, locator, value, press_enter=False):
        element = self.wait_for_element_to_be_clickable(locator)
        element.clear()
        if press_enter:
            element.send_keys(value,Keys.ENTER)
        else:
            element.send_keys(value)

    def get_text(self, locator):
        element = self.wait_for_element_to_be_visible(locator)
        return element.text

    def clear_element(self, locator):
        element = self.wait_for_element_to_be_clickable(locator)
        element.clear()

    def wait_for_url_contains(self, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(text)
        )

    def wait_for_text_to_be_present(self, locator, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        )

