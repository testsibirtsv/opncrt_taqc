import re
from selenium.webdriver.support.ui import Select
from .base import BasePage
from .addressbook import AddressBookPage
from locators.addaddress import AddAddressLocators
from models.addressbook import AddressBook


class AddAddressPage(BasePage):

    def fill_address_form(self, address):
        """
        Fill fields with data in Add Address form.

        :param address: object with parameters for fields.
        """
        self.change_text_field_data(
            self.driver.find_element(*AddAddressLocators.FIRSTNAME_FIELD), address.first_name)
        self.change_text_field_data(
            self.driver.find_element(*AddAddressLocators.LASTNAME_FIELD), address.last_name)
        self.change_text_field_data(
            self.driver.find_element(*AddAddressLocators.COMPANY_FIELD), address.company)
        self.change_text_field_data(
            self.driver.find_element(*AddAddressLocators.ADDRESS1_FIELD), address.address_1)
        self.change_text_field_data(
            self.driver.find_element(*AddAddressLocators.ADDRESS2_FIELD), address.address_2)
        self.change_text_field_data(
            self.driver.find_element(*AddAddressLocators.CITY_FIELD), address.city)
        self.change_text_field_data(
            self.driver.find_element(*AddAddressLocators.POSTCODE_FIELD), address.post_code)
        self.change_drop_list_data(
            self.driver.find_element(*AddAddressLocators.COUNTRY_OPTION), address.country)
        self.change_drop_list_data(
            self.driver.find_element(*AddAddressLocators.REGION_OPTION), address.region_state)
        self.driver.find_element(*AddAddressLocators.BTN_CONTINUE).click()
        return AddressBookPage(self.driver)

    @staticmethod
    def change_drop_list_data(ddlist_option, value):
        """
        Select option in dropdown list in Add Address form.

        :param ddlist_option: option's id in dropdown list.
        :param value: option's text in dropdown list.
        """
        if value is not None:
            data_select = Select(ddlist_option)
            data_select.select_by_visible_text(value)

    @staticmethod
    def change_text_field_data(field_name, value):
        """
        Set text into Add Address form field.

        :param field_name: field's id in Add Address form.
        :param value: field's text in Add Address form.
        """
        if value is not None:
            field_name.click()
            field_name.clear()
            field_name.send_keys(value)

    def get_firstname_error(self):
        return self.driver.find_element(*AddAddressLocators.FIRSTNAME_ERROR).text

    def get_lastname_error(self):
        return self.driver.find_element(*AddAddressLocators.LASTNAME_ERROR).text

    def get_address1_error(self):
        return self.driver.find_element(*AddAddressLocators.ADDRESS1_ERROR).text

    def get_city_error(self):
        return self.driver.find_element(*AddAddressLocators.CITY_ERROR).text

    def get_postcode_error(self):
        return self.driver.find_element(*AddAddressLocators.POSTCODE_ERROR).text

    def get_region_error(self):
        return self.driver.find_element(*AddAddressLocators.REGION_ERROR).text

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
