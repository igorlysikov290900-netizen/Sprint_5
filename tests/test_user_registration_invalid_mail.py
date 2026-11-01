import random as r
from locators.locators import LoginLocators
from selenium import webdriver 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestUserRegistrationInvalidMail:

    def generate_email(self):
        number = r.randint(1000, 9999)
        email = f"name{number}"
        return email

    def setup_method(self):
        self.driver = webdriver.Chrome()
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

    def teardown_method(self):
        self.driver.quit()

    def test_registration_invalid_mail(self):
        password = 'password'
        email = self.generate_email()
        self.generate_email()
        self.click_button(LoginLocators.login_window_button)
        self.click_button(LoginLocators.signup_window_button)
        self.send_keys(LoginLocators.signup_email_field, email)
        self.send_keys(LoginLocators.sign_up_password_field, password)
        self.send_keys(LoginLocators.signup_repeat_password_field, password)
        self.click_button(LoginLocators.sign_up_create_button)
        assert self.get_text(LoginLocators.mail_error_text) == 'Ошибка' and self.is_element_visible(LoginLocators.password_error) == True and self.is_element_visible(LoginLocators.repeat_password_error) == True