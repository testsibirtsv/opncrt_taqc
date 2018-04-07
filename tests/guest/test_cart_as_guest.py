from selenium import webdriver

from helpers.settings import BASE_HOST
from pages.cart import CartPage
from pages.home import HomePage

driver = webdriver.Chrome()
driver.get(BASE_HOST)
product = "iPhone"


def test_goto_home_page():
    assert HomePage(driver).is_on_home_page()


def test_empty_cart_page():
    assert HomePage(driver).goto_cart().is_cart_empty()


def test_add_iphone_to_cart():
    assert (HomePage(driver)
            .click_nav_phones()
            .goto_product_page(product)
            .add_to_cart()
            .go_to_cart()
            .is_product_added(product))


def test_delete_from_cart():
    (HomePage(driver).
     click_nav_phones().
     goto_product_page(product).
     add_to_cart().go_to_cart().
     delete_good_from_cart())
    assert CartPage(driver).is_cart_empty()


def test_edit_product_qty():
    assert (HomePage(driver)
            .click_nav_phones()
            .goto_product_page(product)
            .add_to_cart()
            .go_to_cart()
            .edit_product_qty(2))
