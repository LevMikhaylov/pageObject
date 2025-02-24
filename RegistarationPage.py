from selenium.webdriver.common.by import By
from .base_page import BasePage

class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def fill_registration_form(self, first_name, last_name, email, telephone, password):
        self.send_keys(By.ID, 'input-firstname', first_name)
        self.send_keys(By.ID, 'input-lastname', last_name)
        self.send_keys(By.ID, 'input-email', email)
        self.send_keys(By.ID, 'input-telephone', telephone)
        self.send_keys(By.ID, 'input-password', password)
        self.send_keys(By.ID, 'input-confirm', password)
    
    def agree_to_terms(self):
        self.click(By.NAME, 'agree')
    
    def submit_registration(self):
        self.click(By.XPATH, '//input[@value="Continue"]')
