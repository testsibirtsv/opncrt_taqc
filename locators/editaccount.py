from selenium.webdriver.common.by import By
from .base import BasePageLocators


class EditAccountLocators(BasePageLocators):

    FIRSTNAME_FIELD = (By.ID, "input-firstname")
    LASTNAME_FIELD = (By.ID, "input-lastname")
    EMAIL_FIELD = (By.ID, "input-email")
    TELEPHONE_FIELD = (By.ID, "input-telephone")
    CONTINUE_BUTTON = (By.XPATH, "//form[@class='form-horizontal']/div/div[2]/input")
