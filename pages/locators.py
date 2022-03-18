from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6 .price_color")
    PRODUCT_NAME_IN_BASKET= (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    PRODUCTS_PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alertinner p strong")
    MESSAGE_ABOUT_ADD_IN_BASKET = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
