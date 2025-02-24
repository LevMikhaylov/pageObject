# run_tests.py
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import sys

def run_tests():
    browser = sys.argv[1] if len(sys.argv) > 1 else "firefox"

    if browser == "chrome":
        options = Options()
        options.headless = False
        service = Service(executable_path='C:\\Users\\Student\\Downloads\\chromedriver-win64\\chromedriver.exe')
        driver = webdriver.Chrome(service=service, options=options)
    else:
        options = FirefoxOptions()
        options.headless = False
        service = FirefoxService(executable_path='C:\\Users\\Student\\Downloads\\geckodriver-v0.26.0-win64\\geckodriver.exe')
        driver = webdriver.Firefox(service=service, options=options)

    driver.get("https://demo.opencart.com/")
    
    # Ваши тесты
    unittest.TextTestRunner().run()  # Запуск всех тестов в тестовом классе

    driver.quit()

if __name__ == "__main__":
    run_tests()
