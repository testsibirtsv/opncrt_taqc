"""
TODO
"""
from selenium.webdriver.common.by import By
from .base import BasePageLocators


# pylint: disable=too-few-public-methods
class AccountLocators(BasePageLocators):
    """
    TODO
    """
    ADDRESS_BOOK_LINK = (By.LINK_TEXT, "Address Book")
    EDIT_ACCOUNT_LINK = (By.XPATH, "//div[@id='content']//a[.='Edit Account']")
    YOUR_STORE_LINK = (By.LINK_TEXT, "Your Store")
