from typing_extensions import Self
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import time


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_should_see_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/"  #указываем ссылку
    page = MainPage(browser, link)                   #берем брузер из базы и ссылку из верхней строки
    page.open()                                      #выполняем открытие self.browser.get(self.url)
    page.go_to_login_page()                          #переход к странице авторизации self.click(*MainPageLocators.LOGIN_LINK), "Go to Login link"
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

@pytest.mark.temp_new
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
    #message_about_basket_is_empty_disappeared()
#
#Гость открывает главную страницу 
#Переходит в корзину по кнопке в шапке сайта
#Ожидаем, что в корзине нет товаров
#Ожидаем, что есть текст о том что корзина пуста 
#
#В классе BasePage реализуйте соответствующий метод для перехода в корзину. Создайте файл basket_page.py и в нем класс BasketPage. Реализуйте там необходимые проверки, в том числе отрицательную, которую мы обсуждали в предыдущих шагах. 
#
#Убедитесь, что тесты проходят и зафиксируйте изменения в коммите. 



