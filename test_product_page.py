import time
import pytest
from selenium.webdriver.common.by import By
from Pages.product_page import ProductPage
from Pages.basket_page import BasketPage
from Pages.login_page import LoginPage
from selenium import webdriver

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser = ProductPage(browser, link)
    browser.open()
    browser.should_add_item_to_cart()
    browser.add_to_cart_item_title_control()
    browser.add_to_cart_item_price_control()
    browser.add_to_cart_item_stock_control()

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser = ProductPage(browser, link)
    browser.open()
    browser.should_add_item_to_cart()
    browser.should_not_be_success_message()

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser = ProductPage(browser, link)
    browser.open()
    browser.should_add_item_to_cart()
    browser.is_element_disappeared()

@pytest.mark.skip
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_quest_can_add_product_to_basket_with_parametrize(browser, link):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    browser = ProductPage(browser, link)
    browser.open()
    browser.should_add_item_to_cart()
    browser.add_to_cart_item_title_control()
    browser.add_to_cart_item_price_control()
    browser.add_to_cart_item_stock_control()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    browser = BasketPage(browser, link)
    browser.open()
    browser.go_to_basket()
    browser.there_is_not_some_products_in_the_basket()
    browser.empty_basket_control()

def test_quest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser = ProductPage(browser, link)
    browser.open()
    browser.should_not_be_success_message()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        browser = LoginPage(browser, link)
        browser.open()
        browser.go_to_login_page()
        browser.register_new_user()
        browser.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser = ProductPage(browser, link)
        browser.open()
        browser.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser = ProductPage(browser, link)
        browser.open()
        browser.should_add_item_to_cart()
        browser.add_to_cart_item_title_control()
        browser.add_to_cart_item_price_control()
        browser.add_to_cart_item_stock_control()






