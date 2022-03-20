from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_FILD = (By.CSS_SELECTOR, ".form-control#id_registration-email")
    REGISTER_PASSWORD_FILD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD_FILD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    BTN_REGISTER = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary[data-loading-text='Registering...']")


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
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > .btn-default:nth-child(1)")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    MESSAGE_ABOUT_BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner p") 
    SOME_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")
    

