"""
TODO
"""
from selenium import webdriver


# pylint: disable=too-few-public-methods
class BasePageElement:
    """Base element."""

    def __init__(self, driver=None):
        """
        TODO
        """
        self.driver = driver if driver else webdriver.Chrome()
