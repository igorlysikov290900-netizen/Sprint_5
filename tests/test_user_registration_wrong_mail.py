import random as r
from locators import LoginLocators
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class RegistrationInvalidMail:
    def __init__(self, driver):
        self.driver = driver
        self.locator = LoginLocators
### вынести в фикстуру
    
    def generate_email(self):
        number = r.randint(1000, 9999)
        return f"name{number}"

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

login = RegistrationInvalidMail(webdriver.Chrome())
email = login.generate_email()
password = 'password'
login.generate_email
login.setup()
login.click_button(LoginLocators.login_window_button)
login.click_button(LoginLocators.signup_window_button)
login.send_keys(LoginLocators.signup_email_field, email)
login.send_keys(LoginLocators.sign_up_password_field, password)
login.send_keys(LoginLocators.signup_repeat_password_field, password)
login.click_button(LoginLocators.sign_up_create_button)
error_text = 'Ошибка'
assert login.get_text(LoginLocators.mail_error_text) == 'Ошибка' and login.is_element_visible(LoginLocators.password_error) == True and login.is_element_visible(LoginLocators.repeat_password_error) == True
login.quit()