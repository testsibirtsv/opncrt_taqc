"""
Locators for Login Page
"""
from selenium.webdriver.common.by import By
from .base import BasePageLocators


# pylint: disable=too-few-public-methods
class LoginPageLocators(BasePageLocators):
    """
    Locators for Login Page
    """
    EMAIL_INPUT_FIELD = (By.ID, "input-email")
    PASSWORD_INPUT_FIELD = (By.ID, "input-password")
    LOGIN_BUTTON = (By.XPATH, '//*[@id="content"]/div/div[2]/div/form/input')
