"""
Contains the AddressBookPage class for interacting with the AddressBook page.
"""
from .base import BasePage
from .addaddress import AddAddressPage
from models.addressbook import AddressBook
from locators.addressbook import AddressBookLocators
import re


class AddressBookPage(BasePage):
    """
    Contains methods for interacting with the AddressBook page.
    """

    def get_alert_message_text(self):
        """
        Receive a message from the address book after adding,
        editing or deleting a record.
        """
        return self.driver.find_element(*AddressBookLocators.ALERT_MESSAGE).text

    def records_count(self):
        """
        Count the number of address records on the Address Book page.

        """
        return len(self.driver.find_elements(*AddressBookLocators.BTN_EDIT_LIST))

    def goto_editaddress_page_by_index(self, index):
        """
        Edit address book entry from the Address Book page
        by it's positional index.

        :param index: positional index of address entry
        in list of addresses on the Address Book page.
        """
        self.driver.find_elements(*AddressBookLocators.BTN_EDIT_LIST)[index].click()
        return AddAddressPage(self.driver)

    def delete_record_by_index(self, index):
        """
        Delete Address Book entry from Address Book page
        by it's positional index.

        :param index: positional index of address entry
        in list of addresses on Address Book page.
        """
        self.driver.find_elements(*AddressBookLocators.BTN_DELETE_LIST)[index].click()
        return self

    def goto_addaddres_page(self):
        """
        Open Add Address form o
        n Address Book page.
        """
        self.driver.find_element(*AddressBookLocators.BTN_NEW_ADDRESS).click()
        return AddAddressPage(self.driver)

    def get_content_info_from_list(self):
        """
        Get text of each individual address record in table on the Address Book page,
        filter and convert it into object, append them to list and return it.

        :return: list of objects.
        """
        address_list = []
        for line in self.driver.find_elements(*AddressBookLocators.CONTENT_LIST):
            content = re.sub(r'\s', '', line.text)
            address_list.append(AddressBook(content=content))
        return address_list

    @staticmethod
    def get_content_info_from_form(address_obj):
        """
        Get text from object, filter and convert it into another object.

        :param address_obj: object that we used to create/edit Add Address form.
        :return: object with filtered text.
        """
        info_from_object = []
        for attr in address_obj.__dict__.items():
            if attr[1] is not None:
                info_from_object.append(attr[1])
        content = re.sub(r'\s', '', "".join(info_from_object))
        return AddressBook(content=content)

    def get_content_info_by_index(self, index):
        """
        Get text from address record  by index in table on the Address Book page,
        filter and convert it into object.

        :return: object.
        """
        info = self.driver.find_elements(*AddressBookLocators.CONTENT_LIST)[index].text
        content = re.sub(r'\s', '', info)
        return AddressBook(content=content)

    #
    #
    #
    #
    #
    #
    # def create(self, address):
    #     """
    #     Open Address Book page, then open and fill Add Address form
    #     and submit creation.
    #
    #     :param address: object with parameters for fields in Add Address form.
    #     """
    #     self.open_address_book_page()
    #     self.open_form_page()
    #     self.fill_address_form(address)
    #     self.get_continue_button().click()
    #
    # def edit_record_by_index(self, updated_values, index: int):
    #     """
    #     Open Address Book page, then open already existing address entry,
    #     fill Add Address form with new data and submit changes.
    #
    #     :param updated_values: object with parameters for fields in Add Address form.
    #     :param index: position of address in list on Address Book page.
    #     """
    #
    #     self.open_address_book_page()
    #     self.open_edit_page_by_position(index)
    #     self.fill_address_form(updated_values)
    #     self.get_continue_button_from_form().click()
