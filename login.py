import time

from data import TestData
from locators import Locators


class Login:

    driver = None

    def login(self):
        email_input = self.driver.find_element(*Locators.EMAIL_INPUT2)
        email_input.send_keys(TestData.AUTH_EMAIL)

        password_input = self.driver.find_element(*Locators.PASSWORD_INPUT)
        password_input.send_keys(TestData.AUTH_PASSWORD)

        self.driver.find_element(*Locators.ENTER).click()
        time.sleep(1)
