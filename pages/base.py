"""
Base Page comes here.
"""

from selenium import webdriver

from locators.base import BasePageLocators


# pylint: disable=too-few-public-methods
class BasePage:
    """
    Base class to initialize the base page that will be called from all pages
    """

    def __init__(self, driver=None):
        """
        Initialization of base driver
        """
        self.driver = driver if driver else webdriver.Chrome()
        self.grey_cart_btn = GreyCartBtn(driver)


class GreyCartBtn:
    """
    Class to work with grey Cart button.
    """
    def __init__(self, driver):
        """
        Initialization of grey Cart Button
        """
        self.driver = driver

    def click_btn_grey_cart(self):
        """
        Make webdriver click grey Cart button.
        """
        self.driver.find_element(*BasePageLocators.BTN_GREY_CART).click()
        return self

    def click_link_viewcart(self):
        """
        Make webdriver click Viewcart Link in grey Cart button.
        """
        self.driver.find_element(*BasePageLocators.LINK_VIEW_CART).click()
        return self

    def click_link_checkout(self):
        """
        Make webdriver click Checkout Link in grey Cart button.
        """
        self.driver.find_element(*BasePageLocators.LINK_CHECKOUT).click()
        return self
