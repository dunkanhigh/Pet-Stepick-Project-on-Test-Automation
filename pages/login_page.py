from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url.find('login') != -1, "Not login page"

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        email_field.send_keys(email)
        password1_field = self.browser.find_element(
            *LoginPageLocators.REG_PASSWORD)
        password1_field.send_keys(password)
        password2_field = self.browser.find_element(
            *LoginPageLocators.REG_PASSWORD_REPEAT)
        password2_field.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        button.click()
