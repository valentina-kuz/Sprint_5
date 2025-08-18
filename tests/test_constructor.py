from locators import MainPageLocators
from urls import URLS
from test_data import TextData
from utils.browser_helpers import wait_for_element_visible, wait_for_element_clickable, safe_scroll_to_element

class TestConstructorPage:

    def test_transition_to_bun_success(self, driver):
        """Проверка, что раздел 'Булки' активен по умолчанию"""
        driver.get(URLS.MAIN_PAGE_URL)
        
        # Ждём загрузки страницы
        wait_for_element_visible(driver, MainPageLocators.bun, timeout=10)
        
        # Проверяем содержимое раздела "Булки" (он активен по умолчанию)
        bun_text = driver.find_element(*MainPageLocators.bun).text
        bun_displayed = driver.find_element(*MainPageLocators.bun_ul).is_displayed()
        
        assert bun_text == TextData.BUNS_SECTION and bun_displayed

    def test_transition_to_sauces_success(self, driver):
        """Проверка перехода к разделу 'Соусы'"""
        driver.get(URLS.MAIN_PAGE_URL)
        
        # Ждём, что кнопка "Соусы" станет кликабельной
        sauces_btn = wait_for_element_clickable(driver, MainPageLocators.sauces_btn)
        
        # Прокручиваем к элементу и кликаем
        safe_scroll_to_element(driver, sauces_btn)
        sauces_btn.click()
        
        # Проверяем содержимое раздела
        sauces = driver.find_element(*MainPageLocators.sauces).text
        sauces_displayed = driver.find_element(*MainPageLocators.sauces_ul).is_displayed()
        assert sauces == TextData.SAUCES_SECTION and sauces_displayed

    def test_transition_to_topping_success(self, driver):
        """Проверка перехода к разделу 'Начинки'"""
        driver.get(URLS.MAIN_PAGE_URL)
        
        # Ждём, что кнопка "Начинки" станет кликабельной
        toppings_btn = wait_for_element_clickable(driver, MainPageLocators.toppings_btn)
        
        # Прокручиваем к элементу и кликаем
        safe_scroll_to_element(driver, toppings_btn)
        toppings_btn.click()
        
        # Проверяем содержимое раздела
        topping = driver.find_element(*MainPageLocators.topping).text
        topping_displayed = driver.find_element(*MainPageLocators.topping_ul).is_displayed()
        assert topping == TextData.TOPPINGS_SECTION and topping_displayed