import pytest
from selenium import webdriver

import settings


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.set_window_size(1600, 900)
    driver.get(settings.URL)
    yield driver
    driver.quit()
