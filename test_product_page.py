from typing_extensions import Self
from selenium.common.exceptions import NoAlertPresentException
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time


@pytest.mark.parametrize('links', ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'])
def test_guest_cant_see_success_message(browser, links):
    link = f'{links}'
    page = ProductPage(browser, link)
    page.open()
    page.guest_cant_see_success_message()

@pytest.mark.parametrize('part_of_link', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail(reason="nu 3.14zdec...")), 8, 9])
def test_guest_can_add_product_to_basket(browser, part_of_link):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{part_of_link}'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_add_in_basket()
    page.add_price_equals_main_price()
    page.add_name_equals_main_name()
    

@pytest.mark.parametrize('links', ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'])
@pytest.mark.xfail(reason="Negative test, all good (MESSAGE_ABOUT_ADD_IN_BASKET is presented)")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, links):
    link = f'{links}'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.guest_cant_see_success_message_after_adding_product_to_basket()
    


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/' #ХЗ какую
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user()
        page.should_be_authorized_user()

    @pytest.mark.temp_new
    @pytest.mark.parametrize('links', ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'])
    def test_user_cant_see_success_message(self, browser, links):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.guest_cant_see_success_message()
    
    @pytest.mark.temp_new
    @pytest.mark.parametrize('part_of_link', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail(reason="nu 3.14zdec...")), 8, 9])
    def test_user_can_add_product_to_basket(self, browser, part_of_link):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{part_of_link}'
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_message_about_add_in_basket()
        page.add_price_equals_main_price()
        page.add_name_equals_main_name()



@pytest.mark.parametrize('links', ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'])
@pytest.mark.xfail(reason="Negative test, all good (MESSAGE_ABOUT_ADD_IN_BASKET don't disappeared)")
def test_message_disappeared_after_adding_product_to_basket(browser, links): 
    link = f'{links}'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.message_disappeared_after_adding_product_to_basket()


@pytest.mark.parametrize('links', ['http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'])
def test_guest_should_see_login_link_on_product_page(browser, links):
    link = f'{links}'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.parametrize('links', ['http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'])
def test_guest_can_go_to_login_page_from_product_page(browser, links):
    link = f'{links}'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.parametrize('links', ['http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'])
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, links):
    link = f'{links}'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket_page()
    page2 = BasketPage(browser, browser.current_url)
    page2.guest_can_see_message_about_basket_is_empty()
    page2.basket_is_empty()
    page2.guest_cant_see_success_some_adding_product_to_basket()        
    

