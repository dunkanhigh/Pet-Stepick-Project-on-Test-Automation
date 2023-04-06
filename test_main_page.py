import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage

link = 'http://selenium1py.pythonanywhere.com/'


@pytest.mark.login_guest
class TestLoginFromMainPage():
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser, link=link):
        page = MainPage(browser, link)
        page.open()
        self.page = page

    def test_guest_can_go_to_login_page(self):
        login_page = LoginPage(*self.page.go_to_login())
        login_page.should_be_login_url()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self):
        basket_page = BasketPage(*self.page.go_to_basket())
        basket_page.basket_is_empty()
