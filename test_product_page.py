from selenium.webdriver.common.by import By
from .Pages.product_page import ProductsPage

#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
def test_guest_can_add_product_to_basket(browser):
    browser = ProductsPage(browser, link)
    browser.open()
    browser.should_add_item_to_cart()
    browser.add_to_cart_item_title_control()
    browser.add_to_cart_item_price_control()
