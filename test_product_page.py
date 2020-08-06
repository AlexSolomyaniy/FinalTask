import pytest

from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product = ProductPage(browser,link)
    product.open()
    product.add_book_in_bucket()
    product.should_be_login_url()
    #product.solve_quiz_and_get_code()
    #product.should_not_be_success_message()
    #product.should_is_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()
    
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = BasketPage(browser,link)
    page.open()
    page.click_on_bucket()
    page.should_be_empty_messaege()
    page.should_be_without_books()

class TestUserAddToBasketFromProductPage():
    @pytest.mark.need_review
    def test_user_cant_see_product_in_basket_opened_from_product_page(self,browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.register_new_user()
        page.should_be_logined()
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = BasketPage(browser, link)
        page.open()
        page.click_on_bucket()
        page.should_be_empty_messaege()
        page.should_be_without_books()