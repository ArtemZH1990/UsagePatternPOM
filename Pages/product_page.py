from .base_page import BasePage
from .locators import ProductsPageLocators
import time

class ProductPage(BasePage):
    #Methods
    def add_to_cart_item_price_control(self):
        actual_price = self.browser.find_element(*ProductsPageLocators.BOOK_TITLE_LINK).text.split('\n')[1]    #This book price
        expected_price = self.browser.find_element(*ProductsPageLocators.BASKET_TOTAL_LINK).text.split('\n')[0]

        assert actual_price in expected_price, "Price of added items is wrong!"

    def add_to_cart_item_stock_control(self):
        actual_status = self.browser.find_element(*ProductsPageLocators.BOOK_TITLE_LINK).text.split('\n')[2]   #This item stock status

        assert "available" in actual_status

    def add_to_cart_item_title_control(self):
        actual_title = self.browser.find_element(*ProductsPageLocators.BOOK_TITLE_LINK).text.split('\n')[0]    #This book title
        expected_title = self.browser.find_element(*ProductsPageLocators.ADD_INFO_POLE_LINK).text.split('\n')[1]

        assert actual_title in expected_title, "Title of added items is wrong!"

    def is_element_disappeared(self):
        assert self.is_disappeared(*ProductsPageLocators.SUCCESS_MESSAGE), \
        "Element is not disappeared"

    def should_add_item_to_cart(self):
        self.browser.find_element(*ProductsPageLocators.BASKET_SUBMIT_BUTTON_LINK).click()
        #self.solve_quiz_and_get_code()    #If alert is appear. It's bonus method from course creators. Be careful with it!

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductsPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"





