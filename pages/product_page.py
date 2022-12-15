from .base_page import BasePage
from .locators import BasketLocators
from .locators import ProductAdd

class BasketADD(BasePage):

    def add_to_basket(self):
        buy_button = self.browser.find_element(*BasketLocators.Basket_ADD)
        buy_button.click()

    def add_basket_link_is_present(self):
        assert self.is_element_present(*BasketLocators.Basket_ADD), "Login link is not presented"

    def product_name(self):
        product_name = self.browser.find_element(*ProductAdd.PRODUCT_NAME).text
        product_message = self.browser.find_element(*ProductAdd.NAME_MESSAGE).text
        print(product_name, product_message)
        assert product_message == product_name, f"{product_name} is not {product_message}"

    def product_price(self):
        product_price = self.browser.find_element(*ProductAdd.PRODUCT_PRICE).text
        product_price_message = self.browser.find_element(*ProductAdd.PRICE_MESSAGE).text
        print(product_price, product_price_message)
        assert product_price == product_price_message, f"{product_price} is not {product_price_message}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductAdd.SUCCESS_MESSAGE),  "Success message is presented, but should not be"

    def should_be_disapeared(self):
        assert self.is_disappeared(*ProductAdd.SUCCESS_MESSAGE), "Element is present, but should not be"