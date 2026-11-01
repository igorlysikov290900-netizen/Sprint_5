import random as r
from locators.locators import LoginLocators
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestAddAd:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://qa-desk.education-services.ru/')

    def click_button(self, element):        
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(element))
        elem = self.driver.find_element(*element).click()


    def send_keys(self, element, text):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(element))
        self.driver.find_element(*element).send_keys(text)
    
    def get_text(self, element):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(element))
        return self.driver.find_element(*element).text

    def wait_visible(self, element):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(element))

    def teardown_method(self):
        self.driver.quit()
        
    def test_add_ad(self):
        email = 'name1234@gmail.com'
        password = 'password'
        item_name = 'test 123'
        item_description = 'description'
        item_condition = r.choice(LoginLocators.checkmarks)
        city_name = r.choice(LoginLocators.cities)
        self.click_button(LoginLocators.login_window_button)
        self.send_keys(LoginLocators.email_field, email)
        self.send_keys(LoginLocators.password_field, password)
        self.click_button(LoginLocators.login_button)
        self.wait_visible(LoginLocators.logout_button)
        self.click_button(LoginLocators.add_ad_window_button)
        self.send_keys(LoginLocators.ad_name, item_name)
        self.send_keys(LoginLocators.ad_description, item_description)
        self.send_keys(LoginLocators.ad_cost, r.randint(1, 1000000))
        self.click_button(LoginLocators.cities_list_button)
        self.click_button(city_name)
        self.click_button(item_condition)
        self.click_button(LoginLocators.create_ad_button)
        self.wait_visible(LoginLocators.ads_columns)
        self.click_button(LoginLocators.profile_button)
        assert self.get_text(LoginLocators.created_ad_name) == item_name