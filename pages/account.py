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

    def goto_addressbook_page(self) -> object:
        """
        Redirect to AddressBook page.
        """
        self.driver.find_element(*AccountLocators.ADDRESS_BOOK_LINK).click()
        return AddressBookPage(self.driver)

    def goto_editaccount_page(self) -> object:
        """
        Redirect to EditAccount page.
        """
        self.driver.find_element(*AccountLocators.EDIT_ACCOUNT_LINK).click()
        return EditAccountPage(self.driver)

    def goto_homepage(self):
        """
        TODO
        """
        self.driver.find_element(*AccountLocators.YOUR_STORE_LINK).click()
        return self
