from pages.product_page import ProductPage
import pytest

first_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
promo_num_list = [str(i) for i in range(
    7)] + [pytest.param("7", marks=pytest.mark.xfail)]+[str(i) for i in range(8, 10)]


@pytest.mark.parametrize('promo_num', promo_num_list)
def test_guest_can_add_product_to_basket(browser, promo_num):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_num}'
    page = ProductPage(browser, url=link)
    page.open()
    page.add_to_basket()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link=first_link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser, first_link):
    page = ProductPage(browser, first_link)
    page.open()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser, link=first_link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_disappeared_success_message()


def test_guest_should_see_login_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login()
