from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from time import sleep
from main_page import MainPage
from product_page import ProductPage
from pc_category_page import PCCategoryPage
from registration_page import RegistrationPage

# Настройка драйвера Firefox
options = Options()
options.headless = False  # Для отображения браузера (True для безголового режима)
service = Service(executable_path='C:\\Users\\Student\\Downloads\\geckodriver-v0.26.0-win64\\geckodriver.exe')  # Укажите путь до geckodriver
driver = webdriver.Firefox(service=service, options=options)

try:
    # Создаем экземпляр главной страницы
    main_page = MainPage(driver)
    
    # 1. Открыть сайт и кликнуть на продукт на главной странице
    driver.get("https://demo.opencart.com/")
    main_page.click_first_product()
    
    # Переходим на страницу продукта
    product_page = ProductPage(driver)
    
    # Проверка переключения скриншотов
    sleep(2)
    if product_page.get_product_screenshots():
        print("Скриншоты переключаются на странице продукта.")
    else:
        print("Скриншоты не переключаются на странице продукта.")
    
    # 2. Сменить валюту с доллара на евро и обратно
    main_page.change_currency('EUR')  # Сменить валюту на евро
    sleep(2)
    main_page.change_currency('USD')  # Сменить валюту обратно на доллар

    # 3. Перейти в категорию PC и проверить, что страница пуста
    main_page.click(By.XPATH, '//ul[@class="nav navbar-nav"]/li/a[contains(text(), "PC")]')
    pc_category_page = PCCategoryPage(driver)
    
    if pc_category_page.is_empty():
        print("Страница категории PC пуста.")
    else:
        print("В категории PC есть продукты.")

    # 4. Перейти в регистрацию, заполнить все поля и нажать «зарегистрироваться»
    main_page.click(By.XPATH, '//ul[@class="nav navbar-nav"]/li/a[contains(text(), "Register")]')
    registration_page = RegistrationPage(driver)
    registration_page.fill_registration_form("John", "Doe", "john.doe@example.com", "1234567890", "Password123")
    registration_page.agree_to_terms()
    registration_page.submit_registration()
    sleep(2)

    # 5. Написать поисковое слово в строке поиска и нажать кнопку поиска
    main_page.search("Laptop")
    sleep(3)

finally:
    # Закрыть браузер после выполнения всех шагов
    driver.quit()
