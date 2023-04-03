from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_is_empty(self):
        assert self.is_not_element_present(
            *BasketPageLocators.GOODS_BLOCK), "Find goods block!"
        assert self.is_element_present(
            *BasketPageLocators.MESSAGE), 'Message not found!'
