import random as r
from locators import LoginLocators
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class Logout:
    def __init__(self, driver):
        self.driver = driver
        self.locator = LoginLocators
### вынести в фикстуру

    def setup(self):
        self.driver.maximize_window()
        self.driver.get('https://qa-desk.education-services.ru/')
        

    def click_button(self, element):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(element))
        self.driver.find_element(*element).click()


    def send_keys(self, element, text):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(element))
        self.driver.find_element(*element).send_keys(text)
    
    def get_text(self, element):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(element))
        return self.driver.find_element(*element).text

    def is_element_visible(self, element):
        try:
            WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(element))
            return True
        except:
            return False

    def quit(self):
        self.driver.quit()

driver = Logout(webdriver.Chrome())
email = 'name1234@gmail.com'
password = 'password'
driver.setup()
driver.click_button(LoginLocators.login_window_button)
driver.send_keys(LoginLocators.email_field, email)
driver.send_keys(LoginLocators.password_field, password)
driver.click_button(LoginLocators.login_button)
driver.click_button(LoginLocators.logout_button)
assert driver.get_text(LoginLocators.add_ad_button) == 'Разместить объявление' and driver.get_text(LoginLocators.login_window_button) == 'Вход и регистрация' and driver.is_element_visible(LoginLocators.user_name) == False and driver.is_element_visible(LoginLocators.user_logo) == False
driver.quit()
