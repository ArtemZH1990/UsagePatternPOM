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