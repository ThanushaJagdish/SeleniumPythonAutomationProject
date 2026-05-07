from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    search_box = (By.XPATH, "(//input[@formcontrolname='productName'])[2]")
    search_result = (By.XPATH,"//div[@class='card']")
    search_result_text = (By.ID,"res")


    def search(self,search_item):
        self.enter_value(self.search_box,search_item,press_enter=True)


    def items_name_in_search_results(self):
        items_card = self.wait_for_elements_to_be_visible(self.search_result)
        item_names = []
        for item in items_card:
            name = item.find_element(By.XPATH,(".//h5/b")).text.lower()
            item_names.append(name)
        print(item_names)
        return item_names

    def search_result_qty(self):
        search_txt = self.get_text(self.search_result_text)
        list_of_word = search_txt.split(" ")
        return list_of_word[1]

    def add_product_to_cart(self,itemname):
        items_card = self.wait_for_elements_to_be_visible(self.search_result)
        # add_to_cart_button = item_card.find_element(By.XPATH,("./div/button[2]"))
        # add_to_cart_button.click()
        for item in items_card:
            name= item.find_element(By.XPATH,(".//h5/b")).text.lower()
            if name==itemname:
                item.find_element(By.XPATH,("./div/button[2]")).click()


