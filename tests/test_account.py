from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

import settings
from data import TestData
from locators import Locators


class TestAccount:

    def test_account_click(self, driver):  # Тест перехода по клику на «Личный кабинет»
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()

        email_input = driver.find_element(*Locators.EMAIL_INPUT2)
        email_input.send_keys(TestData.AUTH_EMAIL)

        password_input = driver.find_element(*Locators.PASSWORD_INPUT)
        password_input.send_keys(TestData.AUTH_PASSWORD)

        driver.find_element(*Locators.ENTER).click()
        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(ec.visibility_of_element_located(Locators.BURGER_TEXT))

        driver.find_element(*Locators.ACCOUNT_BUTTON).click()

        acc_url = 'https://stellarburgers.nomoreparties.site/account/profile'
        get_url = driver.current_url

        assert get_url == acc_url

    def test_constructor_click(self, driver):  # Тест перехода из личного кабинета в конструктор
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()

        email_input = driver.find_element(*Locators.EMAIL_INPUT2)
        email_input.send_keys(TestData.AUTH_EMAIL)

        password_input = driver.find_element(*Locators.PASSWORD_INPUT)
        password_input.send_keys(TestData.AUTH_PASSWORD)

        driver.find_element(*Locators.ENTER).click()
        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(ec.visibility_of_element_located(Locators.BURGER_TEXT))

        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

        assert driver.find_element(*Locators.BURGER_TEXT)

    def test_logo_click(self, driver):  # Тест перехода по клику на логотип Stellar Burgers
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()

        email_input = driver.find_element(*Locators.EMAIL_INPUT2)
        email_input.send_keys(TestData.AUTH_EMAIL)

        password_input = driver.find_element(*Locators.PASSWORD_INPUT)
        password_input.send_keys(TestData.AUTH_PASSWORD)

        driver.find_element(*Locators.ENTER).click()
        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(ec.visibility_of_element_located(Locators.BURGER_TEXT))

        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.LOGO_STELLARBURGERS).click()

        url = 'https://stellarburgers.nomoreparties.site/'
        get_url = driver.current_url

        assert get_url == url

    def test_logout(self, driver):  # Тест выхода по кнопке «Выйти» в личном кабинете
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()

        email_input = driver.find_element(*Locators.EMAIL_INPUT2)
        email_input.send_keys(TestData.AUTH_EMAIL)

        password_input = driver.find_element(*Locators.PASSWORD_INPUT)
        password_input.send_keys(TestData.AUTH_PASSWORD)

        driver.find_element(*Locators.ENTER).click()
        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(ec.visibility_of_element_located(Locators.BURGER_TEXT))

        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.LOGOUT_BUTTON).click()

        url = 'https://stellarburgers.nomoreparties.site/login/'
        get_url = driver.current_url

        assert get_url == url
