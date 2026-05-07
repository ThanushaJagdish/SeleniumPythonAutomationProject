from pages.checkout_page import CheckoutPage
from pages.checkout_successful_page import CheckOutSuccessPage
from pages.cart_page import CartPage

from utilities.config_reader import ConfigReader

config = ConfigReader()
cvv = config.get_cvv()
name = config.get_name_on_card()

def test_checkout_page(add_to_cart):
    driver = add_to_cart
    cart_pg = CartPage(driver)
    cart_pg.click_checkout()
    checkout_pg = CheckoutPage(driver)
    checkout_pg.enter_cvv(cvv)
    checkout_pg.enter_name(name)
    checkout_pg.select_country("ind")
    checkout_pg.click_place_order()
    checkout_successful_pg = CheckOutSuccessPage(driver)
    assert checkout_successful_pg.order_successful_message()

