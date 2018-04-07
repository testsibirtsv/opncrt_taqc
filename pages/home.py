"""
Home Page comes here.
"""
from urllib.parse import urlparse

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.base import BasePageLocators
from .cart import CartPage
from .login import LoginPage
from .products import ProductsPage
from .base import BasePage


# pylint: disable=too-many-public-methods
class HomePage(BasePage):
    """
    Home Page methods come here.
    """

    def goto_login(self):
        """
        Go to Login Page.
        """
        self.driver.find_element(*BasePageLocators.MY_ACCOUNT_DROPDOWN).click()
        self.driver.find_element(*BasePageLocators.GO_LOGIN).click()
        return LoginPage(self.driver)

    def is_on_home_page(self):
        """
        Make sure we on Home Page.
        """
        current_url_path = urlparse(self.driver.current_url).path
        if current_url_path == "/opencart.com/":
            return True
        return False

    def goto_cart(self):
        """
        Go to Cart Page.
        """
        self.driver.find_element(*BasePageLocators.GO_CART).click()
        return CartPage(self.driver)

    def click_nav_components(self):
        """
        Click Component Tab.
        """
        self.driver.find_element(*BasePageLocators.COMPONENTS).click()
        return self

    def click_nav_components_monitors(self):
        """
        Click Component Tab.
        Click Monitors.
        """
        self.click_nav_components()
        monitors = self.driver.find_element(*BasePageLocators.MONITORS)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.element_to_be_clickable(BasePageLocators.MONITORS))
        monitors.click()
        return ProductsPage(self.driver)

    def click_nav_phones(self):
        """
        Click Phones Tab.
        """
        self.driver.find_element(*BasePageLocators.PHONES).click()

        return ProductsPage(self.driver)

    def click_nav_desktops(self):
        """
        Click Desktops Tab.
        """
        self.driver.find_element(*BasePageLocators.DESKTOPS).click()
        return self

    def click_nav_laptops(self):
        """
        Click Laptops Tab.
        """
        self.driver.find_element(*BasePageLocators.LAPTOPS).click()
        return self

    def click_nav_tablets(self):
        """
        Click Tablests Tab.
        """
        self.driver.find_element(*BasePageLocators.TABLETS).click()
        return ProductsPage(self.driver)

    def click_nav_cameras(self):
        """
        Click Cameras Tab.
        """
        self.driver.find_element(*BasePageLocators.CAMERAS).click()
        return ProductsPage(self.driver)

    def click_nav_mp3_players(self):
        """
        Click MP3 Players Tab.
        """
        self.driver.find_element(*BasePageLocators.MP3S).click()
        return self

    def click_nav_desktops_pc(self):
        """
        Click Desktops Tab.
        Click Pc.
        """
        self.click_nav_desktops()
        self.driver.find_element(*BasePageLocators.DESKTOPS).click()
        return ProductsPage(self.driver)

    def click_nav_desktops_mac(self):
        """
        Click Desktops Tab.
        Click Mac.
        """
        self.click_nav_desktops()
        self.driver.find_element(*BasePageLocators.MAC).click()
        return ProductsPage(self.driver)

    def click_nav_desktops_show_all(self):
        """
        Click Desktops Tab.
        Click Show all desktops.
        """
        self.click_nav_desktops()
        self.driver.find_element(*BasePageLocators.ALLDESKTOPS).click()
        return ProductsPage(self.driver)

    def click_nav_laptops_macs(self):
        """
        Click Laptops Tab.
        Click Macs.
        """
        self.click_nav_laptops()
        self.driver.find_element(*BasePageLocators.MACS).click()
        return ProductsPage(self.driver)

    def click_nav_laptops_windows(self):
        """
        Click Laptops Tab.
        Click Windows.
        """
        self.click_nav_laptops()
        self.driver.find_element(*BasePageLocators.WINDOWS).click()
        return ProductsPage(self.driver)

    def click_nav_laptops_show_all(self):
        """
        Click Laptops Tab.
        Click Show all Laptops .
        """
        self.click_nav_laptops()
        self.driver.find_element(*BasePageLocators.ALLLEPTOPS).click()
        return ProductsPage(self.driver)

    def click_nav_components_mice(self):
        """
        Click Components Tab.
        Click Mice .
        """
        self.click_nav_components()
        self.driver.find_element(*BasePageLocators.MICE).click()
        return ProductsPage(self.driver)

    def click_nav_components_printers(self):
        """
        Click Components Tab.
        Click Printers .
        """
        self.click_nav_components()
        self.driver.find_element(*BasePageLocators.PRINTERS).click()
        return ProductsPage(self.driver)

    def click_nav_components_scanners(self):
        """
        Click Components Tab.
        Click Scanners.
        """
        self.click_nav_components()
        self.driver.find_element(*BasePageLocators.SCANNERS).click()
        return ProductsPage(self.driver)

    def click_nav_components_webcamera(self):
        """
        Click Components Tab.
        Click Web Camera.
        """
        self.click_nav_components()
        self.driver.find_element(*BasePageLocators.WEBCAMERAS).click()
        return ProductsPage(self.driver)

    def click_nav_components_show_all(self):
        """
        Click Components Tab.
        Click Show all components.
        """
        self.click_nav_components()
        self.driver.find_element(*BasePageLocators.ALLCOMPONENTS).click()
        return ProductsPage(self.driver)

    def get_components_list(self):
        """
        Find all subcategory Components
        """

        components_list = self.driver.find_elements(*BasePageLocators.LIST_COMPONENS)
        return components_list

    def get_desktops_list(self):
        """
        Find all subcategory Desktops
        """

        desktops_list = self.driver.find_elements(*BasePageLocators.LIST_DESKTOPS)
        return desktops_list

    def get_laptops_list(self):
        """
        Find all subcategory Desktops
        """

        laptops_list = self.driver.find_elements(*BasePageLocators.LIST_LAPTOPS)
        return laptops_list
