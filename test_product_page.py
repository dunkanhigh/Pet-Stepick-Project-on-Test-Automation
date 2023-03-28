from pages.product_page import ProductPage
import pytest

promo_num_list = [str(i) for i in range(
    7)] + [pytest.param("7", marks=pytest.mark.xfail)]+[str(i) for i in range(8, 10)]


@pytest.mark.parametrize('promo_num', promo_num_list)
def test_guest_can_add_product_to_basket(browser, promo_num):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_num}'
    page = ProductPage(browser, url=link)
    page.open()
    page.add_to_basket()
