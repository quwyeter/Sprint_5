from selenium.webdriver.common.by import By


class Locators:
    LOGO_STELLARBURGERS = (By.XPATH, ".//a[@href = '/']")

    LOG_BUTTON_IN_PASSWORD_RECOVERY_PAGE = (
        By.XPATH, './/a[text()="Войти"]')  # Кнопка входа на странице восстановления пароля
    PASSWORD_RECOVERY_BUTTON = (By.XPATH, './/a[text()="Восстановить пароль"]')  # Кнопка восстановить пароль

    LOGIN_BUTTON = (By.XPATH, './/button[text()="Войти в аккаунт"]')  # Кнопка войти в аккаунт
    ACCOUNT_BUTTON = (By.XPATH, './/p[text()="Личный Кабинет"]')  # Кнопка личный кабинет
    ENTER = (By.XPATH, './/button[text()="Войти"]')  # Кнопка войти

    ORDER_BUTTON = (By.XPATH, './/button[text()="Оформить заказ"]')  # Кнопка оформить заказ

    REGISTRATION_BUTTON_MAIN = (By.CLASS_NAME, "Auth_link__1fOlj")  # Кнопка регистрации
    LOG_BUTTON_IN_REGISTRATION_PAGE = (By.XPATH, ".//a[text() = 'Войти']")  # Кнопка входа на странице регистрации
    PASSWORD_ERROR = (By.XPATH, ".//p[text()='Некорректный пароль']")  # Ошибка некорректный пароль

    NAME_INPUT = (By.NAME, "name")  # Поле ввода имени
    EMAIL_INPUT = (By.XPATH, ".//main/div/form/fieldset[2]/div/div/input")  # Поле ввода email в окне регистрации
    EMAIL_INPUT2 = (By.XPATH, ".//main/div/form/fieldset[1]/div/div/input")  # Поле ввода email в окне входа
    PASSWORD_INPUT = (By.NAME, "Пароль")  # Поле ввода пароля
    LOGIN_SUBMIT = (By.CLASS_NAME,
                    "button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg")  # Кнопка входа

    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text() = 'Конструктор']")  # Кнопка конструктор
    BURGER_TEXT = (By.XPATH, "//h1[text()='Соберите бургер']")
    BULKI_BUTTON = (By.XPATH, "//div[1]/span")  # Кнопка булки
    BULKI_SELECT = (
        By.XPATH, "//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")
    SAUCES_BUTTON = (By.XPATH, "//div[2]/span")  # Кнопка соусы
    SAUCES_SELECT = (
        By.XPATH, "//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")
    FILLINGS_BUTTON = (By.XPATH, "//div[3]/span")  # Кнопка начинки
    FILLINGS_SELECT = (
        By.XPATH, "//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")

    LOGOUT_BUTTON = (By.XPATH, "//button[text() = 'Выход']")  # Кнопка выхода
