from selenium.webdriver.common.by import By
from .base import BasePageLocators


class AddressBookLocators(BasePageLocators):

    EDIT_BUTTON = (By.XPATH, "//td[@class='text-right']//a[.='Edit']")
    EDIT_BUTTONS_LIST = (By.XPATH, "//div[@class='table-responsive']//a[.='Edit']")
    DELETE_BUTTON = (By.XPATH, "//td[@class='text-right']//a[.='Delete']")
    DELETE_BUTTONS_LIST = (By.XPATH, "//div[@class='table-responsive']//a[.='Delete']")
    NEW_ADDRESS_BUTTON = (By.XPATH, "//div[@id='content']//a[.='New Address']")
    ALERT_MESSAGE = (By.XPATH, "//div[@id='account-address']/div[1]")
    CONTENT_LIST = (By.XPATH, '//*[@id="content"]//table/tbody//td[1]')
