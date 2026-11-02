from locators.locators import LoginLocators
from helpers import click_button, send_keys, get_text, is_element_visible


class TestUserLogin:

    def test_user_login(self, driver):
        email = 'name1234@gmail.com'
        password = 'password'
        click_button(driver, LoginLocators.login_window_button)
        send_keys(driver, LoginLocators.email_field, email)
        send_keys(driver, LoginLocators.password_field, password)
        click_button(driver, LoginLocators.login_button)
        assert get_text(driver, LoginLocators.user_name) == 'User.' and is_element_visible(driver, LoginLocators.user_logo) == True
