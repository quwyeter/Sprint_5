import pytest
from selenium import webdriver

import settings
from locators import Locators
from login import Login


class TestAccount(Login):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1600, 900)
        self.driver.get(settings.URL)
        yield
        self.driver.quit()

    def test_account_click(self):  # Тест перехода по клику на «Личный кабинет»
        self.driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        self.login()

        self.driver.find_element(*Locators.ACCOUNT_BUTTON).click()

        acc_url = 'https://stellarburgers.nomoreparties.site/account/profile'
        get_url = self.driver.current_url

        assert get_url == acc_url

    def test_constructor_click(self):  # Тест перехода из личного кабинета в конструктор
        self.driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        self.login()

        self.driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        self.driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

        assert self.driver.find_element(*Locators.BURGER_TEXT)

    def test_logo_click(self):  # Тест перехода по клику на логотип Stellar Burgers
        self.driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        self.login()

        self.driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        self.driver.find_element(*Locators.LOGO_STELLARBURGERS).click()

        url = 'https://stellarburgers.nomoreparties.site/'
        get_url = self.driver.current_url

        assert get_url == url

    def test_logout(self):  # Тест выхода по кнопке «Выйти» в личном кабинете
        self.driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        self.login()

        self.driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        self.driver.find_element(*Locators.LOGOUT_BUTTON).click()

        url = 'https://stellarburgers.nomoreparties.site/login/'
        get_url = self.driver.current_url

        assert get_url == url
