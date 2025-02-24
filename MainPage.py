from selenium.webdriver.common.by import By
from .base_page import BasePage

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def click_first_product(self):
        self.click(By.XPATH, '//div[@class="product-layout product-grid"]//a')

    def change_currency(self, currency):
        self.click(By.XPATH, '//div[@class="btn-group"]/button')
        self.click(By.XPATH, f'//button[@name="{currency}"]')

    def search(self, keyword):
        self.send_keys(By.NAME, 'search', keyword)
        self.find_element(By.NAME, 'search').send_keys(Keys.RETURN)

    def get_screenshot_count(self):
        screenshots = self.driver.find_elements(By.XPATH, '//div[@id="content"]//ul[@class="thumbnails"]/li')
        return len(screenshots)
