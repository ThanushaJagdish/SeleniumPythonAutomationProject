from pages.search_page import SearchPage
from pages.cart_page import CartPage
from utilities.config_reader import ConfigReader

config = ConfigReader()
username = config.get_username()
password = config.get_password()

def test_add_item_to_cart(search_product):
    driver = search_product
    search_pg = SearchPage(driver)
    cart_pg = CartPage(driver)
    initial_count_in_cart = cart_pg.cart_button_count()
    search_pg.add_product_to_cart('iphone 13 pro')
    cart_pg.wait_for_text_to_be_present(cart_pg.cart_button_label,str(initial_count_in_cart+1))
    assert cart_pg.cart_button_count()==initial_count_in_cart+1
    cart_pg.click_cart()
    assert 'iphone 13 pro' in cart_pg.get_cart_items_names()

def test_remove_item_from_cart(search_product):
    driver = search_product
    search_pg = SearchPage(driver)
    cart_pg = CartPage(driver)
    search_pg.add_product_to_cart('iphone 13 pro')
    cart_pg.wait_for_text_to_be_present(cart_pg.cart_button_label, "1")
    cart_pg.click_cart()
    cart_pg.remove_items_from_cart("iphone 13 pro")
    cart_pg.wait_for_text_to_be_present(cart_pg.cart_button_label, "")
    assert cart_pg.cart_is_empty()
