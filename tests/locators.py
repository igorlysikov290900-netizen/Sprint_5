from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class LoginLocators:
    login_window_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div/button')
    email_field = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[2]/div[1]/div/div/input')
    password_field = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[2]/div[2]/div/div/input')
    login_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[3]/button[1]')
    signup_window_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[3]/button[2]')
    signup_email_field = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[2]/div[1]/div/div/input')
    sign_up_password_field = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[2]/div[2]/div/div/input')
    signup_repeat_password_field = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[2]/div[3]/div/div/input')
    sign_up_create_button = (By. XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[3]/button[1]')
    user_logo = (By.CSS_SELECTOR, '.svgSmall')
    user_name = (By.XPATH, '//*[@id="root"]/div/div[1]/div/div[1]/div/h3')
    picture = (By.CSS_SELECTOR, '.picture')