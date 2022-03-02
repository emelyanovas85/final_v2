from typing_extensions import Self
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
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
 

