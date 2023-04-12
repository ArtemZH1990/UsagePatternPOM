import pytest

import allure
from Pages.basket_page import BasketPage
from Pages.login_page import LoginPage
from Pages.main_page import MainPage

# Locators
link_sales_time = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"

# Tests
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/"
    browser = BasketPage(browser, link)
    browser.open()
    browser.go_to_basket()
    browser.there_is_not_some_products_in_the_basket()
    browser.empty_basket_control()


@pytest.mark.login_guest
@allure.description("test guest can go to login page")
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()




