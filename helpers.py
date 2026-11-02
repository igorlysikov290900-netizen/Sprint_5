import random as r
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def generate_email():
    number = r.randint(1000, 9999)
    domain = r.choice(["@gmail.com", "@yandex.ru", "@mail.ru"])
    email = f"name{number}{domain}"
    return email

def generate_invalid_email():
    number = r.randint(1000, 9999)
    email = f"name{number}"
    return email

def click_button(driver, element):
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(element))
    driver.find_element(*element).click()


def send_keys(driver, element, text):
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(element))
    driver.find_element(*element).send_keys(text)
    
def get_text(driver, element):
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(element))
    return driver.find_element(*element).text

def is_element_visible(driver, element):
    try:
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(element))
        return True
    except:
        return False

def wait_visible(driver, element):
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(element))