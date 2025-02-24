# pages/wishlist_page.py
from selenium.webdriver.common.by import By
from .base_page import BasePage

class WishlistPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def is_item_in_wishlist(self, item_name):
        wishlist_items = self.driver.find_elements(By.XPATH, '//table[@class="table table-bordered"]/tbody/tr')
        for item in wishlist_items:
            if item_name in item.text:
                return True
        return False
