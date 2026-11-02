import pytest
from selenium import webdriver

url = 'https://qa-desk.education-services.ru/'

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.quit()