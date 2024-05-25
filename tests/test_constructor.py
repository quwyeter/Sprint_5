import pytest
from selenium import webdriver

import settings
from locators import Locators


class TestConstructor:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1600, 900)
        self.driver.get(settings.URL)
        yield
        self.driver.quit()

    def test_bulki_click(self):  # Тест перехода к разделу «Булки»
        assert self.driver.find_element(*Locators.BULKI_SELECT)

    def test_sauces_click(self):  # Тест перехода к разделу «Соусы»
        self.driver.find_element(*Locators.SAUCES_BUTTON).click()

        assert self.driver.find_element(*Locators.SAUCES_SELECT)

    def test_fillings_click(self):  # Тест перехода к разделу «Начинки»
        self.driver.find_element(*Locators.FILLINGS_BUTTON).click()

        assert self.driver.find_element(*Locators.FILLINGS_SELECT)
