"""
Account Page comes here.
"""
from locators.account import AccountLocators
from .base import BasePage
from .addressbook import AddressBookPage


class AccountPage(BasePage):
    """
    Account Page methods come here.
    """

    def goto_addressbook_page(self):
        """
        TODO
        """
        self.driver.find_element(*AccountLocators.ADDRESS_BOOK_LINK).click()
        return AddressBookPage(self.driver)

    def open_user_edit_page(self):
        """
        TODO
        """
        self.driver.find_element(*AccountLocators.EDIT_ACCOUNT_LINK).click()
        return self

    def goto_homepage(self):
        """
        TODO
        """
        self.driver.find_element(*AccountLocators.YOUR_STORE_LINK).click()
        return self
