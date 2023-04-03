from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.keys import Keys
import time

class LoginPage(BasePage):
    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"    #Random var, for tests(Don't forget to delete it)
        password = "Brbrbrbr1231231313"    #Random var, for tests(Don't forget to delete it)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_USERNAME_LINK).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_LINK).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_REPEAT_LINK).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON_LINK).click()

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