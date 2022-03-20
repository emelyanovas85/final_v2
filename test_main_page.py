from typing_extensions import Self
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import time



@pytest.mark.login_guest
class TestLoginFromMainPage():

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()



def test_guest_should_see_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page1 = LoginPage(browser, browser.current_url)
    login_page1.should_be_login_form()
    
def test_guest_hould_see_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page2 = LoginPage(browser, browser.current_url)
    login_page2.should_be_register_form()
    
def test_guest_should_see_login_url(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page3 = LoginPage(browser, browser.current_url)
    login_page3.should_be_login_url()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket_page()
    page2 = BasketPage(browser, browser.current_url)
    page2.guest_can_see_message_about_basket_is_empty()
    page2.basket_is_empty()
    page2.guest_cant_see_success_some_adding_product_to_basket()

def test_register_new_user(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page3 = LoginPage(browser, link)
    page3.open()
    page3.register_new_user()


