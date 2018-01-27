import pytest as pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pageobjects.basepage import BasePage


class HomeScreen(BasePage):

    def __init__(self, driver):
        self.driver = driver
        self.post_list = WebDriverWait(self.driver.instance, 10).until(
            EC.presence_of_all_elements_located((
                By.TAG_NAME, "article")))
        self.first_post = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_element_located((
                By.XPATH, "//article[1]//h3/a")))

    @pytest.allure.step("Validate blog posts are visible")
    def validate_posts_are_visible(self):
        assert len(self.post_list) > 0

    @pytest.allure.step("Click Blog's first post")
    def click_first_post(self):
        self.first_post.click()
