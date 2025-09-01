from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException

def wait_for_registration_form(driver, registration_btn_locator, timeout=5):
    """Ожидание появления формы регистрации"""
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(registration_btn_locator)
    )

def wait_for_auth_page(driver, login_btn_locator, timeout=5):
    """Ожидание появления страницы авторизации"""
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(login_btn_locator)
    )

def wait_for_error_message(driver, error_locator, timeout=3):
    """Ожидание появления сообщения об ошибке"""
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(error_locator)
    )

def wait_for_any_error_message(driver, error_locators, timeout=3):
    """Ожидание появления любого из сообщений об ошибке"""
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_any_elements_located(error_locators)
    )

def wait_for_place_order_button(driver, button_locator, timeout=10):
    """Ожидание появления кнопки 'Оформить заказ' после авторизации"""
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(button_locator)
    )

def wait_for_personal_area(driver, exit_btn_locator, timeout=10):
    """Ожидание загрузки личного кабинета"""
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(exit_btn_locator)
    )

def wait_for_constructor_section(driver, section_locator, timeout=10):
    """Ожидание загрузки раздела конструктора"""
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(section_locator)
    )
