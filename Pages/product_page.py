from .base_page import BasePage
from .locators import ProductsPageLocators
import time

class ProductsPage(BasePage):
    #Actions
    def should_add_item_to_cart(self):
        self.browser.find_element(*ProductsPageLocators.CART_SUBMIT_BUTTON_LINK).click()
        self.solve_quiz_and_get_code()

    def add_to_cart_item_title_control(self):
        expected_title = self.browser.find_element(*ProductsPageLocators.ADD_INFO_POLE_LINK).text
        actual_title = self.browser.find_element(*ProductsPageLocators.BOOK_TITLE_LINK).text.split('\n')[0]    #This book title
        assert actual_title in expected_title, "Title of added items is wrong!"

    def add_to_cart_item_price_control(self):
        actual_price = self.browser.find_element(*ProductsPageLocators.BOOK_TITLE_LINK).text.split('\n')[1]    #This book price
        expected_price = self.browser.find_element(*ProductsPageLocators.BASKET_TOTAL_LINK).text.split('\n')[0]
        assert actual_price in expected_price, "Price of added items is wrong!"




