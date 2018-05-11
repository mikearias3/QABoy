from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC


class CheckTitleAndLogo(object):
    def __init__(self, title_locator, logo_locator):
        self.title_locator = title_locator
        self.logo_locator = logo_locator

    def __call__(self, driver):
        try:
            title_element = EC._find_element(driver, self.title_locator)
            logo_element = EC._find_element(driver, self.logo_locator)
            return True
        except StaleElementReferenceException:
            return False
