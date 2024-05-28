import random

from data import TestData
from locators import Locators


class TestRegistration:

    def test_successful_registration(self, driver):  # Тест успешной регистрации

        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.REGISTRATION_BUTTON_MAIN).click()

        name_input = driver.find_element(*Locators.NAME_INPUT)
        name_input.send_keys(TestData.NAME)

        email_input = driver.find_element(*Locators.EMAIL_INPUT)
        email_input.send_keys('IlyaMalikov9'+str(random.randint(000, 999))+'@yandex.ru')

        password_input = driver.find_element(*Locators.PASSWORD_INPUT)
        password_input.send_keys(TestData.AUTH_PASSWORD)

        driver.find_element(*Locators.REGISTRATION_BUTTON_MAIN).click()

        assert driver.find_element(*Locators.ENTER)

    def test_password_error(self, driver):  # Тест ошибки для некорректного пароля
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.REGISTRATION_BUTTON_MAIN).click()

        name_input = driver.find_element(*Locators.NAME_INPUT)
        name_input.send_keys(TestData.NAME)

        email_input = driver.find_element(*Locators.EMAIL_INPUT)
        email_input.send_keys(TestData.AUTH_EMAIL)

        password_input = driver.find_element(*Locators.PASSWORD_INPUT)
        password_input.send_keys(TestData.INVALID_PASSWORD)

        driver.find_element(*Locators.REGISTRATION_BUTTON_MAIN).click()

        assert driver.find_element(*Locators.PASSWORD_ERROR)
