import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class QuickAndDirtySeleniumExample(unittest.TestCase):

    def test_search_proper_tutorial(self):
        driver = webdriver.Chrome()
        driver.get("https://www.google.com/")
        searchbox = driver.find_element_by_name("q")
        searchbox.send_keys("selenium automation framework qaboy")
        searchbox.send_keys(Keys.ENTER)
        link = driver.find_element_by_xpath(
            "//a[@href='https://qaboy.com/2018/01/15/automated-framework-using-selenium-with-python/']")
        link.click()
        assert driver.find_element_by_class_name("entry-title"), "Element was not found."


if __name__ == '__main__':
    unittest.main()
