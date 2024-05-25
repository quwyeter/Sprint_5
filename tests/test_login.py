import pytest
from selenium import webdriver

import settings
from locators import Locators
from login import Login


class TestLogin(Login):

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1600, 900)
        self.driver.get(settings.URL)
        yield
        self.driver.quit()

    def test_login_main_page(self):  # Тест входа по кнопке «Войти в аккаунт» на главной странице
        self.driver.find_element(*Locators.LOGIN_BUTTON).click()

        self.login()

        assert self.driver.find_element(*Locators.ORDER_BUTTON)

    def test_login_account_page(self):  # Тест входа через кнопку «Личный кабинет»
        self.driver.find_element(*Locators.ACCOUNT_BUTTON).click()

        self.login()

        assert self.driver.find_element(*Locators.ORDER_BUTTON)

    def test_login_registration_page(self):  # Тест входа через кнопку в форме регистрации
        self.driver.find_element(*Locators.LOGIN_BUTTON).click()
        self.driver.find_element(*Locators.REGISTRATION_BUTTON_MAIN).click()
        self.driver.find_element(*Locators.LOG_BUTTON_IN_REGISTRATION_PAGE).click()

        self.login()

        assert self.driver.find_element(*Locators.ORDER_BUTTON)

    def test_login_password_recovery_page(self):  # Тест входа через кнопку в форме восстановления пароля
        self.driver.find_element(*Locators.LOGIN_BUTTON).click()
        self.driver.find_element(*Locators.PASSWORD_RECOVERY_BUTTON).click()
        self.driver.find_element(*Locators.LOG_BUTTON_IN_PASSWORD_RECOVERY_PAGE).click()

        self.login()

        self.driver.find_element(*Locators.ENTER).click()

        assert self.driver.find_element(*Locators.ORDER_BUTTON)
