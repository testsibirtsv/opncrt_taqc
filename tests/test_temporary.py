import pytest
from selenium import webdriver

from pages.home import HomePage

driver = webdriver.Chrome()
base_url = 'http://localhost/opencart'
driver.get(base_url)


def test_add_goods_to_cart():
    _PAGE = None
    _PAGE = HomePage(driver)\
        .goto_login()\
        .input_password('saxon123')\
        .input_email('oleksandr.makar.ol@gmail.com')\
        .login().goto_homepage()
    _PAGE = HomePage(driver)\
        .click_nav_desktops_mac()\
        .goto_mac_desctops()\
        .add_to_cart()
    success_text = _PAGE.driver.find_element_by_class_name('alert')
    assert 'Success: You have added' in success_text.text


def test_temp():
    HomePage(driver).goto_login().input_email('taqc296@gmail.com').input_password('root').login().goto_addressbook_page().delete_record_by_index(1)
