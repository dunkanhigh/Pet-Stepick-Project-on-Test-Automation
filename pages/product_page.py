from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def add_to_basket(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET), 'No button'
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()
        self.solve_quiz_and_get_code()
        assert self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text == self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text, "Wrong name"
        # time.sleep(5)
