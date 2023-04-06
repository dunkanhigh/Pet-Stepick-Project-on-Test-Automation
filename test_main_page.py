import pytest
from selenium.webdriver.common.by import By

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=midsummer"
        page = MainPage(browser, link)
        page.open()
        login_page = LoginPage(*page.go_to_login())
        login_page.should_be_login_url()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/'
        page = MainPage(browser, link)
        page.open()
        basket_page = BasketPage(*page.go_to_basket())
        basket_page.basket_is_empty()
