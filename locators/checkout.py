"""
TODO
"""
from selenium.webdriver.common.by import By
from .base import BasePageLocators


# pylint: disable=too-few-public-methods
class CheckoutPageLocators(BasePageLocators):
    """
    TODO
    """
    REGISTER_ACCOUNT = (By.XPATH,
                        '//*[@id="collapse-checkout-option"]/div/div/div[1]/div[1]/label/input')
    GUEST_ACCOUNT = (By.XPATH,
                     '//*[@id="collapse-checkout-option"]/div/div/div[1]/div[2]/label/input')
    STEP_ONE_CONTINUE = (By.ID, 'button-account')
    STEP_TWO_CONTINUE = (By.ID, 'button-register')
