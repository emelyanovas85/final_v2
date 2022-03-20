from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators
import time



class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        text = str(self.url)
        assert "login" in text, 'Login not in url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "ZZZZZZZZZ"
        self.send_keyss(*LoginPageLocators.REGISTER_EMAIL_FILD, email)
        self.send_keyss(*LoginPageLocators.REGISTER_PASSWORD_FILD, password)
        self.send_keyss(*LoginPageLocators.REGISTER_PASSWORD_FILD_CONFIRM, password)
        self.click(*LoginPageLocators.BTN_REGISTER)






