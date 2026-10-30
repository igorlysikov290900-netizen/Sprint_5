from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class LoginLocators:
    login_window_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div/button[1]')
    add_ad_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div/button[2]')
    add_ad_window = (By. XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[1]/h1')
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
    mail_error_text = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[2]/div[1]/span')
    password_error = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[2]/div[2]/div/div')
    repeat_password_error = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[2]/div[3]/div/div')
    logout_button = (By.XPATH, '//*[@id="root"]/div/div[1]/div/div[1]/div/button')
    ad_name = (By,XPATH, '//*[@id="root"]/div/div[2]/div/form/div[2]/div[1]/div/div/input')
    ad_description = (By.XPATH, '//*[@id="root"]/div/div[2]/div/form/div[4]/div/textarea')
    ad=cost - (By.XPATH, '//*[@id="root"]/div/div[2]/div/form/div[5]/div/div/input')
    