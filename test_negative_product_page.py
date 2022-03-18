from .pages.product_page import ProductPage

@pytest.mark.parametrize('link', ['http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'])

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    assert is_not_element_present


def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    assert is_not_element_present


def test_message_disappeared_after_adding_product_to_basket(browser, link): 
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    assert is_disappeared








