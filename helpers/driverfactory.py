""""Class to create singleton specified WebDriver"""

from selenium import webdriver

# pylint: disable=too-few-public-methods
class DriverFactory:
    """
    TODO
    """
    _single_factory = None
    _single_web_driver = None

    def __new__(cls):
        if cls._single_factory is None:
            cls._single_factory = object.__new__(cls)
        return cls._single_factory

    @classmethod
    def create_web_driver(cls, driver_name='chrome'):
        """
        TODO
        """
        if cls._single_web_driver is None:
            if driver_name.lower() == 'chrome':
                cls._single_web_driver = webdriver.Chrome()
            elif driver_name.lower() == 'firefox':
                cls._single_web_driver = webdriver.Firefox()
            elif driver_name.lower() in ('ie', 'iexplorer', 'internetexplorer'):
                cls._single_web_driver = webdriver.Ie()
            elif driver_name.lower() == 'edge':
                cls._single_web_driver = webdriver.Edge()
            elif driver_name.lower() == 'safari':
                cls._single_web_driver = webdriver.Safari()
            else:
                raise ValueError('Unknown type of browser')

        return cls._single_web_driver
