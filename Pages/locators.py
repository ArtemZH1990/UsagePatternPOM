from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.XPATH, "//a[@id='login_link']")
    LOGIN_LINK_SALES_TIME = (By.XPATH, "//a[@id='registration_link']")


class LoginPageLocators:
    #LogIn form
    LOGIN_FORM_LINK = (By.XPATH, "//form[@id='login_form']")
    LOGIN_USERNAME_LINK = (By.XPATH, "//input[@name='login-username']")
    LOGIN_PASSSWORD_LINK = (By.XPATH, "//input[@name='login-password']")
    LOGIN_SUBMIT_BUTTON_LINK = (By.XPATH, "//button[@name='login_submit']")

    #Registration form
    REGISTRATION_FORM_LINK = (By.XPATH, "//form[@id='register_form']")
    REGISTRATION_USERNAME_LINK = (By.XPATH, "//input[@name='registration-email']")
    REGISTRATION_PASSWORD_LINK = (By.XPATH, "//input[@name='registration-password1']")
    REGISTRATION_PASSWORD_REPEAT_LINK = (By.XPATH, "//input[@name='registration-password2']")
    REGISTRATION_SUBMIT_BUTTON_LINK = (By.XPATH, "//button[@name='registration_submit']")


class ProductsPageLocators:
    BASKET_SUBMIT_BUTTON_LINK = (By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    ADD_INFO_POLE_LINK = (By.XPATH, "//div[@class='alert alert-safe alert-noicon alert-success  fade in']")
    BOOK_TITLE_LINK = (By.XPATH, "//div[@class='col-sm-6 product_main']")
    BASKET_TOTAL_LINK = (By.XPATH, "//div[@class='basket-mini pull-right hidden-xs']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@class='alert alert-safe alert-noicon alert-success  fade in']")


class BasePageLocators:
    LOGIN_LINK = (By.XPATH, "//a[@id='login_link']")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//a[@class='btn btn-default']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    EMPTY_BASKET_lINK = (By.XPATH, "//div[@id='content_inner']/p")
    BASKET_HEAD_TITLE = (By.XPATH, "//div[@class='basket-title hidden-xs']")    #There is if the basket has some products
