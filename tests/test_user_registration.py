from helpers import generate_email, generate_invalid_email, click_button, send_keys, get_text, is_element_visible
from locators.locators import LoginLocators



class TestUserRegistration:

    def test_user_registration(self, driver):
        email = generate_email()
        password = 'password'
        click_button(driver, LoginLocators.login_window_button)
        click_button(driver, LoginLocators.signup_window_button)
        send_keys(driver, LoginLocators.email_field, email)
        send_keys(driver, LoginLocators.password_field, password)
        send_keys(driver, LoginLocators.signup_repeat_password_field, password)
        click_button(driver, LoginLocators.sign_up_create_button)
        assert get_text(driver, LoginLocators.user_name) == 'User.' and is_element_visible(driver, LoginLocators.user_logo) == True

    def test_registration_invalid_mail(self, driver):
        password = 'password'
        email = generate_invalid_email()
        click_button(driver, LoginLocators.login_window_button)
        click_button(driver, LoginLocators.signup_window_button)
        send_keys(driver, LoginLocators.email_field, email)
        send_keys(driver, LoginLocators.password_field, password)
        send_keys(driver, LoginLocators.signup_repeat_password_field, password)
        click_button(driver, LoginLocators.sign_up_create_button)
        assert get_text(driver, LoginLocators.mail_error_text) == 'Ошибка' and is_element_visible(driver, LoginLocators.password_error) == True and is_element_visible(driver, LoginLocators.repeat_password_error) == True

    def test_user_registration_already_registred(self, driver):
        email = 'name1234@gmail.com'
        password = 'password'
        click_button(driver, LoginLocators.login_window_button)
        click_button(driver, LoginLocators.signup_window_button)
        send_keys(driver, LoginLocators.email_field, email)
        send_keys(driver, LoginLocators.password_field, password)
        send_keys(driver, LoginLocators.signup_repeat_password_field, password)
        click_button(driver, LoginLocators.sign_up_create_button)
        assert get_text(driver, LoginLocators.mail_error_text) == 'Ошибка' and is_element_visible(driver, LoginLocators.password_error) == True and is_element_visible(driver, LoginLocators.repeat_password_error) == True