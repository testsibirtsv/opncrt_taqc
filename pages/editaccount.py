"""
Contains the EditAccountPage class for interacting with the EditAccount page.
"""
from locators.editaccount import EditAccountLocators
from .base import BasePage


# pylint: disable=too-few-public-methods
class EditAccountPage(BasePage):
    """
    Contains methods for interacting with the EditAccount page.
    """

    @staticmethod
    def _change_data_in_text_fields(form_textfield, data):
        """
        Enter the data in the textfield.

        :param form_textfield: textfield's id.
        :param data: data entered in the textfield.
        """
        if data is not None:
            form_textfield.click()
            form_textfield.clear()
            form_textfield.send_keys(data)

    def fill_edit_account_form(self, user_data):
        """
        Change user data in the Edit Account form.

        :param user_data: data entered in the textfield.
        """
        self._change_data_in_text_fields(
            self.driver.find_element(*EditAccountLocators.FIRSTNAME_FIELD), user_data.first_name)
        self._change_data_in_text_fields(
            self.driver.find_element(*EditAccountLocators.LASTNAME_FIELD), user_data.last_name)
        self._change_data_in_text_fields(
            self.driver.find_element(*EditAccountLocators.EMAIL_FIELD), user_data.email)
        self._change_data_in_text_fields(
            self.driver.find_element(*EditAccountLocators.TELEPHONE_FIELD), user_data.telephone)
        self.driver.find_element(*EditAccountLocators.BTN_CONTINUE).click()
        return self
