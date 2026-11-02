import random as r
from locators.locators import LoginLocators
from helpers import click_button, send_keys, wait_visible, get_text


class TestAddAd:
        
    def test_add_ad(self, driver):
        email = 'name1234@gmail.com'
        password = 'password'
        item_name = 'test 123'
        item_description = 'description'
        item_condition = r.choice(LoginLocators.checkmarks)
        city_name = r.choice(LoginLocators.cities)
        category_choisen = r.choice(LoginLocators.categories)
        click_button(driver, LoginLocators.login_window_button)
        send_keys(driver, LoginLocators.email_field, email)
        send_keys(driver, LoginLocators.password_field, password)
        click_button(driver, LoginLocators.login_button)
        wait_visible(driver, LoginLocators.logout_button)
        click_button(driver, LoginLocators.add_ad_window_button)
        send_keys(driver, LoginLocators.ad_name, item_name)
        send_keys(driver, LoginLocators.ad_description, item_description)
        send_keys(driver, LoginLocators.ad_cost, r.randint(1, 1000000))
        click_button(driver, LoginLocators.cities_list_button)
        click_button(driver, LoginLocators.categories_buton)
        click_button(driver, category_choisen)
        click_button(driver, city_name)
        click_button(driver, item_condition)
        click_button(driver, LoginLocators.create_ad_button)
        wait_visible(driver, LoginLocators.ads_columns)
        click_button(driver, LoginLocators.user_logo)
        assert get_text(driver, LoginLocators.created_ad_name) == item_name
    
    def test_add_ad_unauthorized_user(self, driver):
        click_button(driver, LoginLocators.add_ad_button)
        assert get_text(driver, LoginLocators.add_add_window_unaurhorised_user_text) == 'Чтобы разместить объявление, авторизуйтесь'
    