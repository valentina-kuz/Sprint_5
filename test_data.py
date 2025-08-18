from random import randint

class Person:
    """Существующий пользователь для тестов авторизации"""
    user_name = 'Valentina'
    email = 'valentina_kuzmina_29_777@yandex.ru'
    password = '1Password!'

class RandomData:
    """Генератор случайных данных для тестов регистрации"""
    user_name = 'Test'
    email = f'test{randint(0, 999)}@yandex.ru'
    password = f'{randint(1000, 9999)}Password!'

class TextData:
    """Текстовые выражения для тестов"""
    
    # Названия разделов конструктора
    BUNS_SECTION = 'Булки'
    SAUCES_SECTION = 'Соусы'
    TOPPINGS_SECTION = 'Начинки'
    
    # Сообщения об ошибках регистрации
    INCORRECT_PASSWORD_ERROR = 'Некорректный пароль'
    USER_EXISTS_ERROR = 'Такой пользователь уже существует'
    
    # Названия кнопок
    LOGIN_BUTTON = 'Войти'
    REGISTER_BUTTON = 'Зарегистрироваться'
    ENTER_ACCOUNT_BUTTON = 'Войти в аккаунт'
    PLACE_ORDER_BUTTON = 'Оформить заказ'
    