from models.personaldetails import PersonalDetails
from models.addressbook import AddressBook
from selenium import webdriver

from pages.home import HomePage

driver = webdriver.Chrome()
base_url = 'http://localhost/opencart'
driver.get(base_url)

editaccount_data = PersonalDetails(first_name="Serhii",
                                   last_name="TestLastName",
                                   email="taqc296@gmail.com",
                                   telephone="12345")

address_data = AddressBook(first_name="edited_firstname",
                           last_name="edited_lastname",
                           company="edited_company",
                           address_1="edited_address1",
                           address_2="edited_address2",
                           city="edited_city",
                           post_code="e_postcode",
                           country="Ukraine",
                           region_state="Ternopil's'ka Oblast'")


def test_addressbook_delete():
    HomePage(driver)\
        .goto_login()\
        .input_email('taqc296@gmail.com')\
        .input_password('root')\
        .login()\
        .goto_addressbook_page()\
        .delete_record_by_index(1)


def test_editaccount():
    HomePage(driver)\
        .goto_login()\
        .input_email('taqc296@gmail.com')\
        .input_password('root')\
        .login()\
        .goto_editaccount_page()\
        .fill_edit_account_form(editaccount_data)


def test_editaddress():
    HomePage(driver) \
        .goto_login() \
        .input_email('taqc296@gmail.com') \
        .input_password('root') \
        .login()\
        .goto_addressbook_page()\
        .goto_editaddress_page_by_index(0)\
        .fill_address_form(address_data)
