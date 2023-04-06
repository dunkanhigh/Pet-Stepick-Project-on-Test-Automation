from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.ID, "registration_link")
    SEE_BASKET = (By.XPATH, '//a[@class = "btn btn-default"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    REG_EMAIL = (
        By.XPATH, f'//form[@id ="{REGISTER_FORM[1]}"]//input[@id="id_registration-email"]')
    REG_PASSWORD = (
        By.XPATH, f'//form[@id ="{REGISTER_FORM[1]}"]//input[@id="id_registration-password1"]')
    REG_PASSWORD_REPEAT = (
        By.XPATH, f'//form[@id ="{REGISTER_FORM[1]}"]//input[@id="id_registration-password2"]')
    REG_BUTTON = (By.XPATH, "//button[@value='Register']")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CLASS_NAME, 'btn-add-to-basket')
    PRODUCT_NAME = (By.TAG_NAME, 'h1')
    SUCCESS_MESSAGE = (By.XPATH, "//div[@class='alertinner ']/strong")


class BasketPageLocators():
    GOODS_BLOCK = (By.CLASS_NAME, 'basket-items')
    MESSAGE = (By.XPATH, '//p')
