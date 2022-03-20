from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from .locators import BasePageLocators
import math


class BasePage():


    def open(self):
        self.browser.get(self.url)

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)


    def send_keyss(self, how, what, value):
        try:
            self.browser.find_element(how, what).send_keys(value)
        except (NoSuchElementException):
            return False
        return True


    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def click(self, how, what):
        try:
            self.browser.find_element(how, what).click()
        except (NoSuchElementException):
            return False
        return True
    
    def get_text(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return self.browser.find_element(how, what).text

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        #try:
        #    alert = self.browser.switch_to.alert
        #    alert_text = alert.text
        #    print(f"Your code: {alert_text}")
        #    time.sleep(4)
        #    alert.accept()
        #    time.sleep(4)
        #except NoAlertPresentException:
        #    print("No second alert presented")
        
#ПРОДОЖАЕМ ПИСАТЬ ТУТ нужно добавить импорт ЕС (п 4.3.5.)
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        link.click()

    def should_be_basket_link(self):
        assert self.is_element_present(*BasePageLocators.BASKET_LINK), "Basket link is not presented"

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                 " probably unauthorised user"

#В классе BasePage реализуйте соответствующий метод для перехода в корзину
#РАЗМЕСТИТЬ В АЛФАВИТНОМ ПОРЯДКЕ 



