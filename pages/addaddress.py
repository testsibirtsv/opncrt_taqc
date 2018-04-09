"""
Contains the AddAddressPage class for interacting with the AddAddress page.
"""
from selenium.webdriver.support.ui import Select
from locators.addaddress import AddAddressLocators
from models.addressbook import AddressBook
from .base import BasePage


class AddAddressPage(BasePage):
    """
    Contains methods for interacting with the AddAddress page.
    """

    def fill_address_form(self, address: AddressBook) -> object:
        """
        Fill fields with data in Add Address form.

        :param address: object with parameters for fields.
        """
        self._change_text_field_data(
            self.driver.find_element(*AddAddressLocators.FIRSTNAME_FIELD), address.first_name)
        self._change_text_field_data(
            self.driver.find_element(*AddAddressLocators.LASTNAME_FIELD), address.last_name)
        self._change_text_field_data(
            self.driver.find_element(*AddAddressLocators.COMPANY_FIELD), address.company)
        self._change_text_field_data(
            self.driver.find_element(*AddAddressLocators.ADDRESS1_FIELD), address.address_1)
        self._change_text_field_data(
            self.driver.find_element(*AddAddressLocators.ADDRESS2_FIELD), address.address_2)
        self._change_text_field_data(
            self.driver.find_element(*AddAddressLocators.CITY_FIELD), address.city)
        self._change_text_field_data(
            self.driver.find_element(*AddAddressLocators.POSTCODE_FIELD), address.post_code)
        self._change_drop_list_data(
            self.driver.find_element(*AddAddressLocators.COUNTRY_OPTION), address.country)
        self._change_drop_list_data(
            self.driver.find_element(*AddAddressLocators.REGION_OPTION), address.region_state)
        self.driver.find_element(*AddAddressLocators.BTN_CONTINUE).click()
        return self

    @staticmethod
    def _change_drop_list_data(ddlist_option, value):
        """
        Select option in dropdown list in Add Address form.

        :param ddlist_option: option's id in dropdown list.
        :param value: option's text in dropdown list.
        """
        if value is not None:
            data_select = Select(ddlist_option)
            data_select.select_by_visible_text(value)

    @staticmethod
    def _change_text_field_data(field_name, value):
        """
        Set text into Add Address form field.

        :param field_name: field's id in Add Address form.
        :param value: field's text in Add Address form.
        """
        if value is not None:
            field_name.click()
            field_name.clear()
            field_name.send_keys(value)

    def get_firstname_error(self) -> str:
        """
        Get an error message from the 'First Name' field.

        :return: error message.
        """
        return self.driver.find_element(*AddAddressLocators.FIRSTNAME_ERROR).text

    def get_lastname_error(self) -> str:
        """
        Get an error message from the 'Last Name' field.

        :return: error message.
        """
        return self.driver.find_element(*AddAddressLocators.LASTNAME_ERROR).text

    def get_address1_error(self) -> str:
        """
        Get an error message from the 'Address 1' field.

        :return: error message.
        """
        return self.driver.find_element(*AddAddressLocators.ADDRESS1_ERROR).text

    def get_city_error(self) -> str:
        """
        Get an error message from the 'City' field.

        :return: error message.
        """
        return self.driver.find_element(*AddAddressLocators.CITY_ERROR).text

    def get_postcode_error(self) -> str:
        """
        Get an error message from the 'Post Code' field.

        :return: error message.
        """
        return self.driver.find_element(*AddAddressLocators.POSTCODE_ERROR).text

    def get_region_error(self) -> str:
        """
        Get an error message from the 'Region / State' drop down list option.

        :return: error message.
        """
        return self.driver.find_element(*AddAddressLocators.REGION_ERROR).text
