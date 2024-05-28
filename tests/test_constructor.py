from locators import Locators


class TestConstructor:

    def test_bulki_click(self, driver):  # Тест перехода к разделу «Булки»
        driver.find_element(*Locators.SAUCES_BUTTON).click()
        driver.find_element(*Locators.BULKI_BUTTON).click()

        assert driver.find_element(*Locators.BULKI_SELECT)

    def test_sauces_click(self, driver):  # Тест перехода к разделу «Соусы»
        driver.find_element(*Locators.SAUCES_BUTTON).click()

        assert driver.find_element(*Locators.SAUCES_SELECT)

    def test_fillings_click(self, driver):  # Тест перехода к разделу «Начинки»
        driver.find_element(*Locators.FILLINGS_BUTTON).click()

        assert driver.find_element(*Locators.FILLINGS_SELECT)
