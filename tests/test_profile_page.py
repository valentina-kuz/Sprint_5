from locators import MainPageLocators, PersonalAreaLocators, AuthPageLocators
from urls import URLS
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class TestProfileArea:

    def test_transition_to_personal_area_from_main_page_success(self, get_login_driver):
        """Проверка перехода в личный кабинет с главной страницы"""
        driver = get_login_driver
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.personal_account_btn)
        )  # Ждём появления кнопки "Личный кабинет"
        driver.find_element(*MainPageLocators.personal_account_btn).click()  # Нажимаем на кнопку
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(PersonalAreaLocators.exit_btn)
        )  # Ждём появления кнопки "Выход"
        save_btn_displayed = driver.find_element(*PersonalAreaLocators.save_btn).is_displayed()  # Проверяем кнопку "Сохранить"
        assert driver.current_url == URLS.PROFILE_PAGE_URL and save_btn_displayed  # Проверяем URL и видимость кнопки

    def test_transition_from_personal_area_to_constructor_by_click_constructor_btn_success(self, get_login_driver):
        """Проверка перехода из личного кабинета в конструктор по кнопке 'Конструктор'"""
        driver = get_login_driver
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.personal_account_btn)
        )  # Ждём появления кнопки "Личный кабинет"
        driver.find_element(*MainPageLocators.personal_account_btn).click()  # Нажимаем на кнопку
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(PersonalAreaLocators.exit_btn)
        )  # Ждём появления кнопки "Выход"
        driver.find_element(*PersonalAreaLocators.constructor_btn).click()  # Нажимаем "Конструктор"
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.bun)
        )  # Ждём появления раздела "Булки"
        bun_displayed = driver.find_element(*MainPageLocators.bun).is_displayed()  # Проверяем видимость раздела
        assert driver.current_url == URLS.MAIN_PAGE_URL and bun_displayed  # Проверяем URL и видимость раздела

    def test_transition_from_personal_area_to_constructor_by_click_logo_success(self, get_login_driver):
        """Проверка перехода из личного кабинета в конструктор по логотипу"""
        driver = get_login_driver
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.personal_account_btn)
        )  # Ждём появления кнопки "Личный кабинет"
        driver.find_element(*MainPageLocators.personal_account_btn).click()  # Нажимаем на кнопку
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(PersonalAreaLocators.exit_btn)
        )  # Ждём появления кнопки "Выход"
        driver.find_element(*PersonalAreaLocators.logo_btn).click()  # Нажимаем на логотип
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.bun)
        )  # Ждём появления раздела "Булки"
        bun_displayed = driver.find_element(*MainPageLocators.bun).is_displayed()  # Проверяем видимость раздела
        assert driver.current_url == URLS.MAIN_PAGE_URL and bun_displayed  # Проверяем URL и видимость раздела

    def test_logout_from_personal_area_success(self, get_login_driver):
        """Проверка выхода из личного кабинета"""
        driver = get_login_driver
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.personal_account_btn)
        )  # Ждём появления кнопки "Личный кабинет"
        driver.find_element(*MainPageLocators.personal_account_btn).click()  # Нажимаем на кнопку
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(PersonalAreaLocators.exit_btn)
        )  # Ждём появления кнопки "Выход"
        driver.find_element(*PersonalAreaLocators.exit_btn).click()  # Нажимаем "Выход"
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(AuthPageLocators.login_account_btn)
        )  # Ждём появления кнопки входа
        login_btn_displayed = driver.find_element(*AuthPageLocators.login_account_btn).is_displayed()  # Проверяем кнопку входа
        assert driver.current_url == URLS.AUTH_PAGE_URL and login_btn_displayed  # Проверяем URL и видимость кнопки