from locators.locators import LoginLocators
from selenium import webdriver 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestAddAdUnauthorizedUser:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://qa-desk.education-services.ru/')
        

    def click_button(self, element):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(element))
        self.driver.find_element(*element).click()
    
    def get_text(self, element):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(element))
        return self.driver.find_element(*element).text

    def teardown_method(self):
        self.driver.quit()

    def test_add_ad_unauthorized_user(self):
        self.click_button(LoginLocators.add_ad_button)
        assert self.get_text(LoginLocators.add_add_window_unaurhorised_user_text) == 'Чтобы разместить объявление, авторизуйтесь'
