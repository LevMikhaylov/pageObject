from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def get_product_screenshots(self):
        return self.driver.find_elements(By.XPATH, '//div[@id="content"]//ul[@class="thumbnails"]/li')
