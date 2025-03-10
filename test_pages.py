import pytest
from time import sleep
from main_page import MainPage
from product_page import ProductPage
from pc_category_page import PCCategoryPage
from registration_page import RegistrationPage

# Настройка драйвера Firefox

@pytest.fixture
def main_page(driver):
    return MainPage(driver)

def test_product_screenshots(main_page,base_url):
    driver = main_page.driver
    driver.get(base_url)
    main_page.click_first_product()
    
    product_page = ProductPage(driver)
    sleep(2)
    assert product_page.get_product_screenshots(), "Скриншоты не переключаются на странице продукта."

def test_currency_change(main_page,base_url):
    driver = main_page.driver
    driver.get(base_url)
    
    main_page.change_currency('EUR')  # Сменить валюту на евро
    sleep(2)
    main_page.change_currency('USD')  # Сменить валюту обратно на доллар

def test_pc_category_empty(main_page,base_url):
    driver = main_page.driver
    driver.get(base_url)
    
    main_page.click(By.XPATH, '//ul[@class="nav navbar-nav"]/li/a[contains(text(), "PC")]')
    pc_category_page = PCCategoryPage(driver)
    
    assert pc_category_page.is_empty(), "В категории PC есть продукты."

def test_registration(main_page,base_url):
    driver = main_page.driver
    driver.get(base_url)
    
    main_page.click(By.XPATH, '//ul[@class="nav navbar-nav"]/li/a[contains(text(), "Register")]')
    registration_page = RegistrationPage(driver)
    registration_page.fill_registration_form("John", "Doe", "john.doe@example.com", "1234567890", "Password123")
    registration_page.agree_to_terms()
    registration_page.submit_registration()
    sleep(2)

def test_search(main_page,base_url):
    driver = main_page.driver
    driver.get(base_url)
    
    main_page.search("Laptop")
    sleep(3)
