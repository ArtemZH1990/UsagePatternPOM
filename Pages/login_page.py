from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM_LINK) != None, "Check LOGIN_FORM locator"

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM_LINK) != None, "Check REGISTRATION_FORM locator"