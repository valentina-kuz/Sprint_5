import pytest
from utils.browser_helpers import create_chrome_driver, create_authorized_driver

@pytest.fixture
def driver():
    """Фикстура для создания и закрытия драйвера для каждого теста"""
    driver = create_chrome_driver()
    yield driver
    driver.quit()

@pytest.fixture
def get_login_driver(driver):
    """Фикстура для получения авторизованного драйвера"""
    return create_authorized_driver(driver)