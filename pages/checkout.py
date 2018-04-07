"""
Checkout Page comes here.
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.checkout import CheckoutPageLocators
from .base import BasePage


class CheckoutPage(BasePage):
    """
    Checkout Page methods come here.
    """

    def checkout_options(self):
        """
        TODO
        """
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(CheckoutPageLocators.STEP_ONE_CONTINUE))

        element = self.driver.find_element(*CheckoutPageLocators.GUEST_ACCOUNT)
        element.click()

        element = self.driver.find_element(*CheckoutPageLocators.STEP_ONE_CONTINUE)
        element.click()

    def add_billing_details(self):
        """
        TODO
        """

    def add_payment_method(self):
        """
        TODO
        """

    def confirm_order(self):
        """
        TODO
        """

    def create_order_obj(self):
        """
        TODO
        """
