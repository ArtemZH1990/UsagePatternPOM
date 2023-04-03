from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def empty_basket_control(self):
        assert self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_lINK), "The basket isn't empty"

    def there_is_not_some_products_in_the_basket(self):
        try:
            self.browser.find_element(*BasketPageLocators.BASKET_HEAD_TITLE)
        except:
            return True
        return False
