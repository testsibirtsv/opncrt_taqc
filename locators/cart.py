"""
TODO
"""
from selenium.webdriver.common.by import By
from .base import BasePageLocators


# pylint: disable=too-few-public-methods
class CartPageLocators(BasePageLocators):
    """
    TODO
    """
    GO_CHECKOUT = (By.XPATH, '//*[@id="content"]/div[3]/div[2]/a')
    EMPTY_CART_TEXT = (By.XPATH, '//*[@id="content"]/p')
    BTN_CONTINUE = (By.XPATH, '//*[@id="content"]/div/div/a')
    QTY_FIELD = (By.XPATH, '//*[@id="content"]/form/div/table/tbody/tr/td[4]/div/input')
    BTN_UPDATE = (
        By.XPATH, '//*[@id="content"]/form/div/table/tbody/tr/td[4]/div/span/button[1]')
    BTN_DELETE = (
        By.XPATH, '//*[@id="content"]/form/div/table/tbody/tr/td[4]/div/span/button[2]')

    BTN_DELETE_PRODUCT = (By.CLASS_NAME, 'btn btn-danger')
    BTN_EDIT_QTY = (By.CLASS_NAME, 'btn-primary')
    FIELD_PRODUCT_QTY = (By.CLASS_NAME, 'form-control')
