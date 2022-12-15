from .base_page import BasePage
from .locators import BasketLocators

class BasketPage(BasePage):
    def should_be_message_empty_basket(self):
        assert self.is_element_present(*BasketLocators.BASKET_EMPTY)

    def should_not_be_empty_basket(self):
        assert self.is_not_element_present(*BasketLocators.BASKET_EMPTY)