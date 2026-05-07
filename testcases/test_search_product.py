from pages.search_page import SearchPage
from utilities.customLogger import LogGen

logger=LogGen.loggen()

def test_product_by_entering_full_name(logged_in_user):
    logger.info("Test search product by entering full name")
    driver = logged_in_user
    search_pg = SearchPage(driver)
    search_pg.search("iphone")
    prod_names = search_pg.items_name_in_search_results()
    assert all("iphone" in name for name in prod_names)
    qty = search_pg.search_result_qty()
    assert 1==int(qty)

def test_product_by_entering_partial_name(logged_in_user):
    logger.info("Test search product by entering partial name")
    driver = logged_in_user
    search_pg = SearchPage(driver)
    search_pg.search("iph")
    prod_names = search_pg.items_name_in_search_results()
    assert all("iphone" in name for name in prod_names)
    qty = search_pg.search_result_qty()
    assert 1==int(qty)


def test_product_by_entering_invalid_name(logged_in_user):
    logger.info("Test search product by entering invalid name")
    driver = logged_in_user
    search_pg = SearchPage(driver)
    search_pg.search("xyz")
    qty = search_pg.search_result_qty()
    assert 0==int(qty)
