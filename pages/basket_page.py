from .base_page import BasePage
from .locators import BasketPageLocators



class BasketPage(BasePage):
    

    def guest_can_see_message_about_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_ABOUT_BASKET_IS_EMPTY), "MESSAGE_ABOUT_BASKET_IS_EMPTY is not presented"

    def basket_is_empty(self):
        text_message = self.get_text(*BasketPageLocators.MESSAGE_ABOUT_BASKET_IS_EMPTY)
        print (text_message)
        assert "Your basket is empty." in str(text_message), "MESSAGE_ABOUT_BASKET_IS_EMPTY have a error in text"

    def guest_cant_see_success_some_adding_product_to_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.SOME_PRODUCT_IN_BASKET), "SOME_PRODUCT_IN_BASKET, but guest did not add product to basket"

    
