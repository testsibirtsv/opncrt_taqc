"""
Login Page comes here.
"""
from locators.login import LoginPageLocators
from .account import AccountPage
from .base import BasePage


class LoginPage(BasePage):
    """
    Login Page methods come here.
    """

    def input_email(self, email):
        """Make webdriver set 'E-Mail' value."""
        self.driver.find_element(*LoginPageLocators.EMAIL_INPUT_FIELD).send_keys(email)
        return self

    def input_password(self, password):
        """Make webdriver set 'Password' value."""
        self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT_FIELD).send_keys(password)
        return self

    def login(self):
        """Make webdriver initiate login by click 'Login' Button"""
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        return AccountPage(self.driver)
