from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    

    def add_product_to_basket(self):
        self.click(*ProductPageLocators.BTN_ADD_TO_BASKET), "Add product to basket"

    def fix_price_main_product(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "PRODUCT_PRICE is not presented"
        return self.get_text(*ProductPageLocators.PRODUCT_PRICE)

    def fix_name_main_product(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "PRODUCT_NAME is not presented"
        return self.get_text(*ProductPageLocators.PRODUCT_NAME)

    def price_products_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCTS_PRICE_IN_BASKET), "PRODUCTS_PRICE_IN_BASKET is not presented"
        return self.get_text(*ProductPageLocators.PRODUCTS_PRICE_IN_BASKET)

    def name_products_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_IN_BASKET), "PRODUCT_NAME_IN_BASKET is not presented"
        return self.get_text(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)

    def should_be_message_about_add_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADD_IN_BASKET), "MESSAGE_ABOUT_ADD_IN_BASKET is not presented"
    
    