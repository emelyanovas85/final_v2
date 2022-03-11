from selenium.common.exceptions import NoAlertPresentException
from .pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize('part_of_link', [0, 1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail(reason="nu 3.14zdec...")), 8, 9])


def test_guest_can_add_product_to_basket(browser, part_of_link):
    link1 = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    link2 = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    link3 = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{part_of_link}'
    page = ProductPage(browser, link3)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_add_in_basket()
    assert page.price_products_add_to_basket() == page.fix_price_main_product(), "Product name is not equal"
    assert page.name_products_add_to_basket() == page.fix_name_main_product(), "Product price is not equal"


