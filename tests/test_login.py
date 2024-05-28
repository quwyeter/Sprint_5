from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from data import TestData
from locators import Locators


class TestLogin:

    def test_login_main_page(self, driver):  # Тест входа по кнопке «Войти в аккаунт» на главной странице
        driver.find_element(*Locators.LOGIN_BUTTON).click()

        email_input = driver.find_element(*Locators.EMAIL_INPUT2)
        email_input.send_keys(TestData.AUTH_EMAIL)

        password_input = driver.find_element(*Locators.PASSWORD_INPUT)
        password_input.send_keys(TestData.AUTH_PASSWORD)

        driver.find_element(*Locators.ENTER).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(*Locators.ORDER_BUTTON))

        assert driver.find_element(*Locators.ORDER_BUTTON)

    def test_login_account_page(self, driver):  # Тест входа через кнопку «Личный кабинет»
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()

        email_input = driver.find_element(*Locators.EMAIL_INPUT2)
        email_input.send_keys(TestData.AUTH_EMAIL)

        password_input = driver.find_element(*Locators.PASSWORD_INPUT)
        password_input.send_keys(TestData.AUTH_PASSWORD)

        driver.find_element(*Locators.ENTER).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(*Locators.ORDER_BUTTON))

        assert driver.find_element(*Locators.ORDER_BUTTON)

    def test_login_registration_page(self, driver):  # Тест входа через кнопку в форме регистрации
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.REGISTRATION_BUTTON_MAIN).click()
        driver.find_element(*Locators.LOG_BUTTON_IN_REGISTRATION_PAGE).click()

        email_input = driver.find_element(*Locators.EMAIL_INPUT2)
        email_input.send_keys(TestData.AUTH_EMAIL)

        password_input = driver.find_element(*Locators.PASSWORD_INPUT)
        password_input.send_keys(TestData.AUTH_PASSWORD)

        driver.find_element(*Locators.ENTER).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(*Locators.ORDER_BUTTON))

        assert driver.find_element(*Locators.ORDER_BUTTON)

    def test_login_password_recovery_page(self, driver):  # Тест входа через кнопку в форме восстановления пароля
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        driver.find_element(*Locators.PASSWORD_RECOVERY_BUTTON).click()
        driver.find_element(*Locators.LOG_BUTTON_IN_PASSWORD_RECOVERY_PAGE).click()

        email_input = driver.find_element(*Locators.EMAIL_INPUT2)
        email_input.send_keys(TestData.AUTH_EMAIL)

        password_input = driver.find_element(*Locators.PASSWORD_INPUT)
        password_input.send_keys(TestData.AUTH_PASSWORD)

        driver.find_element(*Locators.ENTER).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(*Locators.ORDER_BUTTON))

        assert driver.find_element(*Locators.ORDER_BUTTON)
