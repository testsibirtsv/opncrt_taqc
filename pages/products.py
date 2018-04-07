"""
Products Page comes here.
"""
# pylint: disable=too-few-public-methods
from locators.products import ProductsPageLocators
from .base import BasePage
from .product import ProductPage


class ProductsPage(BasePage):
    """
    Products Page methods come here.
    """
    def goto_mac_desctops(self):
        """Make webdriver add Mac product to Cart."""
        self.driver.find_element(*ProductsPageLocators.MAC_PRODUCT_IMAGE).click()
        return ProductPage(self.driver)

    def goto_product_page(self, product_name):
        """
        TODO
        """
        self.driver.find_element(*ProductsPageLocators.find_product_link(product_name)).click()
        return ProductPage(self.driver)
