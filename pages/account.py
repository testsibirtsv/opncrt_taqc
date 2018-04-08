"""
Account Page comes here.
"""
from locators.account import AccountLocators
from .base import BasePage
from .addressbook import AddressBookPage
from .editaccount import EditAccountPage


class AccountPage(BasePage):
    """
    Account Page methods come here.
    """

    def goto_address_book(self):
        """
        TODO
        """
        self.driver.find_element(*AccountLocators.ADDRESS_BOOK_LINK).click()
        return AddressBookPage(self.driver)

    def goto_edit_account(self):
        """
        TODO
        """
        self.driver.find_element(*AccountLocators.EDIT_ACCOUNT_LINK).click()
        return EditAccountPage(self.driver)

    def goto_homepage(self):
        """
        TODO
        """
        self.driver.find_element(*AccountLocators.YOUR_STORE_LINK).click()
        return self
