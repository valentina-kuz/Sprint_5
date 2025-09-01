from test_data import Person, RandomData, TextData
from locators import RegistrationPageLocators, AuthPageLocators
from urls import URLS
from utils.test_helpers import (
    wait_for_registration_form,
    wait_for_auth_page,
    wait_for_error_message,
    wait_for_any_error_message
)

class TestRegistrationPage:

    def test_registration_success(self, driver):
        """Проверка успешной регистрации с корректными данными"""
        driver.get(URLS.REG_PAGE_URL)
        
        # Ждём появления формы регистрации
        wait_for_registration_form(driver, RegistrationPageLocators.registration_btn)
        
        # Вводим данные для регистрации
        driver.find_element(*RegistrationPageLocators.name_input).send_keys(RandomData.user_name)
        driver.find_element(*RegistrationPageLocators.email_input).send_keys(RandomData.email)
        driver.find_element(*RegistrationPageLocators.password_input).send_keys(RandomData.password)
        
        # Нажимаем "Зарегистрироваться"
        driver.find_element(*RegistrationPageLocators.registration_btn).click()
        
        # Ждём появления страницы авторизации и проверяем
        wait_for_auth_page(driver, AuthPageLocators.login_account_btn)
        login_btn_displayed = driver.find_element(*AuthPageLocators.login_account_btn).is_displayed()
        
        assert driver.current_url == URLS.AUTH_PAGE_URL and login_btn_displayed

    def test_registration_incorrect_password_check_error(self, driver):
        """Проверка ошибки при некорректном пароле (менее 6 символов)"""
        driver.get(URLS.REG_PAGE_URL)
        
        # Ждём появления формы регистрации
        wait_for_registration_form(driver, RegistrationPageLocators.registration_btn)
        
        # Вводим данные с некорректным паролем
        driver.find_element(*RegistrationPageLocators.name_input).send_keys(Person.user_name)
        driver.find_element(*RegistrationPageLocators.email_input).send_keys(Person.email)
        driver.find_element(*RegistrationPageLocators.password_input).send_keys(12345)
        
        # Нажимаем "Зарегистрироваться"
        driver.find_element(*RegistrationPageLocators.registration_btn).click()
        
        # Ждём появления ошибки и проверяем
        wait_for_any_error_message(driver, RegistrationPageLocators.error_message_incorrect_password)
        error = driver.find_element(*RegistrationPageLocators.error_message_incorrect_password).text
        
        assert (error == TextData.INCORRECT_PASSWORD_ERROR) and (driver.current_url == URLS.REG_PAGE_URL)

    def test_double_registration_check_error(self, driver):
        """Проверка ошибки при повторной регистрации существующего пользователя"""
        driver.get(URLS.REG_PAGE_URL)
        
        # Ждём появления формы регистрации
        wait_for_registration_form(driver, RegistrationPageLocators.registration_btn)
        
        # Вводим данные существующего пользователя
        driver.find_element(*RegistrationPageLocators.name_input).send_keys(Person.user_name)
        driver.find_element(*RegistrationPageLocators.email_input).send_keys(Person.email)
        driver.find_element(*RegistrationPageLocators.password_input).send_keys(Person.password)
        
        # Нажимаем "Зарегистрироваться"
        driver.find_element(*RegistrationPageLocators.registration_btn).click()
        
        # Ждём появления ошибки и проверяем
        wait_for_error_message(driver, RegistrationPageLocators.error_message_double_reg)
        error = driver.find_element(*RegistrationPageLocators.error_message_double_reg).text
        
        assert (error == TextData.USER_EXISTS_ERROR) and (driver.current_url == URLS.REG_PAGE_URL)