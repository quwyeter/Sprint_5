import pytest
from selenium import webdriver

import settings
from data import TestData
from locators import Locators


class TestRegistration:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1600, 900)
        self.driver.get(settings.URL)
        yield
        self.driver.quit()

    def test_successful_registration(self):  # Тест успешной регистрации
        self.driver.find_element(*Locators.LOGIN_BUTTON).click()
        self.driver.find_element(*Locators.REGISTRATION_BUTTON_MAIN).click()

        name_input = self.driver.find_element(*Locators.NAME_INPUT)
        name_input.send_keys(TestData.NAME)

        email_input = self.driver.find_element(*Locators.EMAIL_INPUT)
        email_input.send_keys(TestData.AUTH_EMAIL)

        password_input = self.driver.find_element(*Locators.PASSWORD_INPUT)
        password_input.send_keys(TestData.AUTH_PASSWORD)

        self.driver.find_element(*Locators.REGISTRATION_BUTTON_MAIN).click()

        assert self.driver.find_element(*Locators.ENTER)

    def test_password_error(self):  # Тест ошибки для некорректного пароля
        self.driver.find_element(*Locators.LOGIN_BUTTON).click()
        self.driver.find_element(*Locators.REGISTRATION_BUTTON_MAIN).click()

        name_input = self.driver.find_element(*Locators.NAME_INPUT)
        name_input.send_keys(TestData.NAME)

        email_input = self.driver.find_element(*Locators.EMAIL_INPUT)
        email_input.send_keys(TestData.AUTH_EMAIL)

        password_input = self.driver.find_element(*Locators.PASSWORD_INPUT)
        password_input.send_keys(TestData.INVALID_PASSWORD)

        self.driver.find_element(*Locators.REGISTRATION_BUTTON_MAIN).click()

        assert self.driver.find_element(*Locators.PASSWORD_ERROR)
