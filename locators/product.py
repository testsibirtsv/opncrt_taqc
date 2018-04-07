"""
TODO
"""
from selenium.webdriver.common.by import By
from .base import BasePageLocators


# pylint: disable=too-few-public-methods
class ProductPageLocators(BasePageLocators):
    """
    TODO
    """
    BTN_CART = (By.ID, 'button-cart')
