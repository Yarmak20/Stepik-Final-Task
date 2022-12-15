from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocoators:
    Login_Form = (By.CSS_SELECTOR, "[name = 'login_submit'].btn.btn-lg")
    Registration_Form = (By.CSS_SELECTOR, "[name = 'registration_submit'].btn.btn-lg")

class BasketLocators:
    Basket_ADD = (By.CSS_SELECTOR, "[type='submit'].btn.btn-lg")
    BASKET_FROM_MAIN_PAGE =(By.CSS_SELECTOR, ".basket-mini a.btn")
    BASKET_EMPTY = (By.CSS_SELECTOR,"#content_inner")

class ProductAdd:
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6 h1")
    NAME_MESSAGE = (By.CSS_SELECTOR,".alertinner strong")
    PRODUCT_PRICE =(By.CSS_SELECTOR,".col-sm-6 .price_color")
    PRICE_MESSAGE =(By.CSS_SELECTOR,".alert.alert-safe.alert-noicon.alert-info strong")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR,".icon-user")
