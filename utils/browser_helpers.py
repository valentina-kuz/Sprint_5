from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import MainPageLocators, AuthPageLocators
from urls import URLS
from test_data import Person

def create_chrome_driver():
    """Создание и настройка Chrome драйвера"""
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    return driver

def create_authorized_driver(driver):
    """Создание авторизованного драйвера для тестов личного кабинета"""
    driver.get(URLS.MAIN_PAGE_URL)
    
    # Переходим в личный кабинет
    personal_account_btn = driver.find_element(*MainPageLocators.personal_account_btn)
    personal_account_btn.click()
    
    # Вводим данные для авторизации
    email_input = driver.find_element(*AuthPageLocators.email_input)
    password_input = driver.find_element(*AuthPageLocators.password_input)
    
    email_input.send_keys(Person.email)
    password_input.send_keys(Person.password)
    
    # Нажимаем кнопку входа
    login_btn = driver.find_element(*AuthPageLocators.login_account_btn)
    login_btn.click()
    
    return driver

def wait_for_element_clickable(driver, locator, timeout=10):
    """Ожидание, что элемент станет кликабельным"""
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )

def wait_for_element_visible(driver, locator, timeout=10):
    """Ожидание, что элемент станет видимым"""
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )

def safe_scroll_to_element(driver, element):
    """Безопасная прокрутка к элементу"""
    driver.execute_script("arguments[0].scrollIntoView();", element)
