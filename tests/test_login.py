from test_data import Person, TextData
from locators import (
    MainPageLocators,
    AuthPageLocators,
    RegistrationPageLocators,
    RecoverPageLocators
)
from urls import URLS
from utils.test_helpers import wait_for_place_order_button

class TestLogin:

    def test_login_in_login_btn_success(self, driver):
        """Вход через кнопку 'Войти в аккаунт' на главной странице"""
        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.login_account_btn).click()
        
        # Вводим данные для авторизации
        driver.find_element(*AuthPageLocators.email_input).send_keys(Person.email)
        driver.find_element(*AuthPageLocators.password_input).send_keys(Person.password)
        driver.find_element(*AuthPageLocators.login_account_btn).click()
        
        # Ждём появления кнопки "Оформить заказ" и проверяем
        wait_for_place_order_button(driver, MainPageLocators.place_order_button)
        order_btn = driver.find_element(*MainPageLocators.place_order_button).text
        
        assert (driver.current_url == URLS.MAIN_PAGE_URL) and (order_btn == TextData.PLACE_ORDER_BUTTON)

    def test_login_in_personal_account_btn_success(self, driver):
        """Вход через кнопку 'Личный кабинет' на главной странице"""
        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.personal_account_btn).click()
        
        # Вводим данные для авторизации
        driver.find_element(*AuthPageLocators.email_input).send_keys(Person.email)
        driver.find_element(*AuthPageLocators.password_input).send_keys(Person.password)
        driver.find_element(*AuthPageLocators.login_account_btn).click()
        
        # Ждём появления кнопки "Оформить заказ" и проверяем
        wait_for_place_order_button(driver, MainPageLocators.place_order_button)
        order_btn = driver.find_element(*MainPageLocators.place_order_button).text
        
        assert (driver.current_url == URLS.MAIN_PAGE_URL) and (order_btn == TextData.PLACE_ORDER_BUTTON)

    def test_login_in_registration_form_success(self, driver):
        """Вход через форму регистрации"""
        driver.get(URLS.REG_PAGE_URL)
        driver.find_element(*RegistrationPageLocators.login_account_btn).click()
        
        # Вводим данные для авторизации
        driver.find_element(*AuthPageLocators.email_input).send_keys(Person.email)
        driver.find_element(*AuthPageLocators.password_input).send_keys(Person.password)
        driver.find_element(*AuthPageLocators.login_account_btn).click()
        
        # Ждём появления кнопки "Оформить заказ" и проверяем
        wait_for_place_order_button(driver, MainPageLocators.place_order_button)
        order_btn = driver.find_element(*MainPageLocators.place_order_button).text
        
        assert (driver.current_url == URLS.MAIN_PAGE_URL) and (order_btn == TextData.PLACE_ORDER_BUTTON)

    def test_login_in_recover_form_success(self, driver):
        """Вход через форму восстановления пароля"""
        driver.get(URLS.RECOVER_PAGE_URL)
        driver.find_element(*RecoverPageLocators.login_account_btn).click()
        
        # Вводим данные для авторизации
        driver.find_element(*AuthPageLocators.email_input).send_keys(Person.email)
        driver.find_element(*AuthPageLocators.password_input).send_keys(Person.password)
        driver.find_element(*AuthPageLocators.login_account_btn).click()
        
        # Ждём появления кнопки "Оформить заказ" и проверяем
        wait_for_place_order_button(driver, MainPageLocators.place_order_button)
        order_btn = driver.find_element(*MainPageLocators.place_order_button).text
        
        assert (driver.current_url == URLS.MAIN_PAGE_URL) and (order_btn == TextData.PLACE_ORDER_BUTTON)