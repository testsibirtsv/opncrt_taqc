"""
Register Page comes here.
"""
from selenium.webdriver.common.keys import Keys

from helpers.generators import (generate_random_email,
                                get_random_name,
                                get_random_digit,
                                get_random_password)
from .base import BasePage


class RegisterPage(BasePage):
    """
    Register Page methods come here.
    """

    last_created_password = None
    last_created_email = None

    def input_firstname(self):
        """Make webdriver set random 'First Name' value with presetted length."""
        self.driver.find_element_by_id("input-firstname").send_keys(get_random_name(5))

    def input_lastname(self):
        """Make webdriver set random 'Last Name' value with presetted length."""
        self.driver.find_element_by_id("input-lastname").send_keys(get_random_name(7))

    def input_email(self):
        """
        Make webdriver set random 'E-Mail' value with presetted length of local-name.
        Save generated E-Mail to last_created_email variable (for login).
        """
        self.last_created_email = generate_random_email(5)
        self.driver.find_element_by_id("input-email").send_keys(self.last_created_email)

    def input_telephone(self):
        """Make webdriver set random 'Telephone' value with presetted length."""
        self.driver.find_element_by_id("input-telephone").send_keys(get_random_digit(9))

    def input_password(self):
        """
        Make webdriver set random 'Password' value with presetted length.
        Save generated password to last_created_password variable (for login and confirm).
        """
        self.last_created_password = get_random_password(8)
        self.driver.find_element_by_id("input-password").send_keys(self.last_created_password)

    def input_confirm_password(self):
        """
        Make webdriver set 'Confirm Password' value
        (take from last_created_password variable).
        """
        self.driver.find_element_by_id("input-confirm").send_keys(self.last_created_password)

    def check_checkbox(self):
        """Make webdriver check 'Privacy Policy' Checkbox."""
        self.driver.find_element_by_name("agree").send_keys(Keys.SPACE)

    def registration(self):
        """Make webdriver click 'Continue' Button for registration complete."""
        self.driver.find_element_by_xpath('//*[@id="content"]/form/div/div/input[2]').click()
