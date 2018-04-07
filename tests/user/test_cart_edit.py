import pytest
from selenium import webdriver

from pages.cart import CartPage
from pages.home import HomePage

driver = webdriver.Chrome()
base_url = 'http://localhost:1234/opencart.com'
driver.get(base_url)


def test_add_goods_to_cart():
    _PAGE = None
    with pytest.allure.step('Testing adding goods to cart functional'):
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


def test_edit_goods_qty():
    with pytest.allure.step('Testing editing goods quantity in cart functional'):
        _PAGE = HomePage(driver).goto_cart().edit_good_qty(2)
        edited_cart = _PAGE.driver.find_element_by_id('cart-total')
        assert '2 item(s)' in edited_cart.text


def test_delete_goods_from_cart():
    with pytest.allure.step('Testing deleting goods from cart functional'):
        _PAGE = CartPage(driver).delete_good_from_cart()
        empty_cart = _PAGE.driver.find_element_by_id('cart-total')
        assert '0 item(s)' in empty_cart.text
