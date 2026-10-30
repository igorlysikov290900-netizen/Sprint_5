import random as r
from locators import LoginLocators
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class Addad:
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

drive = Addad(webdriver.Chrome())
email = 'name1234@gmail.com'
password = 'password'
drive.setup()
drive.click_button(LoginLocators.login_window_button)
drive.send_keys(LoginLocators.email_field, email)
drive.send_keys(LoginLocators.password_field, password)
drive.click_button(LoginLocators.login_button)
drive.click_button(LoginLocators.add_ad_window)
drive.send_keys(LoginLocators)
drive.quit()