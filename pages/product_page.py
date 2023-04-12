from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET), 'No button'
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()
        assert self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text == self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text, "Wrong name"

    def add_to_basket_with_alert(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET), 'No button'
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()
        self.solve_quiz_and_get_code()
        assert self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text == self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text, "Wrong name"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_not_disappeared_success_message(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE), "Element is disappeared"
