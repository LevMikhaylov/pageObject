# tests/test_product_page.py
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.wishlist_page import WishlistPage
import time

class TestProductPage(unittest.TestCase):
    def setUp(self):
        # Запуск в Firefox
        self.options = Options()
        self.options.headless = False  # Для отображения браузера
        self.service = Service(executable_path='C:\\path_to_driver\\geckodriver.exe')
        self.driver = webdriver.Firefox(service=self.service, options=self.options)
        self.driver.get("https://demo.opencart.com/")
    
    def test_add_to_wishlist(self):
        main_page = MainPage(self.driver)
        main_page.click_first_product()
        product_page = ProductPage(self.driver)
        product_page.add_to_wishlist()
        wishlist_page = WishlistPage(self.driver)
        self.assertTrue(wishlist_page.is_item_in_wishlist("Product"))
    
    def test_add_to_cart(self):
        main_page = MainPage(self.driver)
        main_page.click_first_product()
        product_page = ProductPage(self.driver)
        product_page.add_to_cart()
        cart_page = CartPage(self.driver)
        self.assertTrue(cart_page.is_item_in_cart("Product"))

    def test_add_review(self):
        main_page = MainPage(self.driver)
        main_page.click_first_product()
        product_page = ProductPage(self.driver)
        product_page.write_review("John Doe", "Great product!")
        # Проверяем, что отзыв был отправлен
        time.sleep(2)
        self.assertTrue("Thank you for your review" in self.driver.page_source)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
