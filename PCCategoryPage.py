from selenium.webdriver.common.by import By
from .base_page import BasePage

class PCCategoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def is_empty(self):
        page_content = self.get_text(By.XPATH, '//div[@id="content"]')
        return "There are no products to list in this category." in page_content
