from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    cart_button = (By.XPATH, "//button[@routerlink='/dashboard/cart']")
    cart_button_label = (By.XPATH, "//button[@routerlink='/dashboard/cart']/label")
    cart_empty_text = (By.XPATH, "//h1[normalize-space()='No Products in Your Cart !']")
    cart_items = (By.XPATH, "//div[@class='infoWrap']")
    checkout_btn = (By.XPATH, "//button[normalize-space()='Checkout']")

    def click_cart(self):
        self.safe_click(self.cart_button)

    def cart_button_count(self):
        cart_item_count = self.get_text(self.cart_button_label)
        return int(cart_item_count) if cart_item_count else 0

    def cart_is_empty(self):
        return self.wait_for_element_to_be_visible(self.cart_empty_text).is_displayed()

    def get_cart_items_names(self):
        items = self.wait_for_elements_to_be_visible(self.cart_items)
        item_names = []
        for item in items:
            item_names.append(item.find_element(By.XPATH,".//h3").text.lower())
        return item_names

    def remove_items_from_cart(self,item_name):
        items = self.wait_for_elements_to_be_visible(self.cart_items)
        for item in items:
            if item.find_element(By.XPATH, ".//h3").text.lower() == item_name:
                item.find_element(By.XPATH, ".//button[@class='btn btn-danger']").click()

    def click_checkout(self):
        self.safe_click(self.checkout_btn)





