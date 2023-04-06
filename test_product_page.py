import pytest
from faker import Faker

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage

fake = Faker()

product_link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
login_link = 'https://selenium1py.pythonanywhere.com/accounts/login/'


# Example with parametrize

# promo_num_list = [str(i) for i in range(
#     7)] + [pytest.param("7", marks=pytest.mark.xfail)]+[str(i) for i in range(8, 10)]


# @pytest.mark.parametrize('promo_num', promo_num_list)
# def test_guest_can_add_product_to_basket(browser, promo_num):
#     link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_num}'
#     page = ProductPage(browser, url=link)
#     page.open()
#     page.add_to_basket_with_alert()


@pytest.mark.product_page_for_guest
class TestGuestAddToBasketFromProductPage():
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser, link=product_link):
        page = ProductPage(browser, link)
        page.open()
        self.page = page

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self):
        self.page.add_to_basket()
        self.page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self):
        self.page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self):
        self.page.add_to_basket()
        self.page.should_not_disappeared_success_message()

    def test_guest_should_see_login_on_product_page(self):
        self.page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self):
        self.page.go_to_login()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self):
        basket_page = BasketPage(*self.page.go_to_basket())
        basket_page.basket_is_empty()

    def test_guest_can_add_product_to_basket(self):
        self.page.add_to_basket_with_alert()


@pytest.mark.product_page_for_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser, link=login_link):
        self.browser = browser
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(fake.email(), fake.password())
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, product_link=product_link):
        page = ProductPage(self.browser, product_link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, product_link=product_link):
        page = ProductPage(self.browser, product_link)
        page.open()
        page.add_to_basket()
