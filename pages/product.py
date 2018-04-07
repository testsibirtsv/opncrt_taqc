"""
Product Page comes here.
"""
from locators.product import ProductPageLocators
from .base import BasePage
from .cart import CartPage


# pylint: disable=too-few-public-methods
class ProductPage(BasePage):
    """
    Product Page methods come here.
    """

    def add_to_cart(self):
        """
        TODO
        """
        self.driver.find_element(*ProductPageLocators.BTN_CART).click()
        self.driver.implicitly_wait(5)
        return self

    def go_to_cart(self):
        """
        TODO
        """
        self.driver.find_element(*ProductPageLocators.GO_CART).click()
        return CartPage(self.driver)
