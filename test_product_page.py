from selenium.common.exceptions import NoAlertPresentException # в начале файла
from .pages.product_page import ProductPage



def test_guest_can_add_product_to_basket(browser):
    link1 = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    link2 = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link2)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_add_in_basket()
    assert str(page.price_products_add_to_basket()) == str(page.fix_price_main_product()), "Product name is not equal"
    assert str(page.name_products_add_to_basket()) == str(page.fix_name_main_product()), "Product price is not equal"


