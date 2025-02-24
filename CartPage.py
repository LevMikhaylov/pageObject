from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def is_item_in_cart(self, item_name):
        cart_items = self.driver.find_elements(By.XPATH, '//table[@class="table table-bordered"]/tbody/tr')
        for item in cart_items:
            if item_name in item.text:
                return True
        return False
