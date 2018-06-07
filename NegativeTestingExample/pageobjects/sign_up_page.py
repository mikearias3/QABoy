import pytest as pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class SignUpPage:

    def __init__(self, driver):
        self.driver = driver
        self.mobile_or_email_textbox = WebDriverWait(self.driver.instance, 5).until(
            EC.visibility_of_element_located((
                By.NAME, "emailOrPhone")))
        self.fullname_textbox = WebDriverWait(self.driver.instance, 5).until(
            EC.visibility_of_element_located((
                By.NAME, "fullName")))
        self.username_textbox = WebDriverWait(self.driver.instance, 5).until(
            EC.visibility_of_element_located((
                By.NAME, "username")))
        self.password_textbox = WebDriverWait(self.driver.instance, 5).until(
            EC.visibility_of_element_located((
                By.NAME, "password")))
        self.next_button = WebDriverWait(self.driver.instance, 5).until(
            EC.visibility_of_element_located((
                By.XPATH, "//button[contains(text(), 'Next')]")))

    def write_username(self, username):
        self.username_textbox.send_keys(username)

    def verify_character_count(self, count):
        character_count = len(self.username_textbox.get_attribute('value'))
        assert character_count == count, "Character count is not equal to " + str(count)

    def write_email_or_phone(self, email_or_phone):
        self.mobile_or_email_textbox.send_keys(email_or_phone)

    def click_next_button(self):
        self.next_button.click()

    def verify_form_errors(self, count):
        form_errors = WebDriverWait(self.driver.instance, 5).until(
            EC.visibility_of_all_elements_located((
                By.CLASS_NAME, "coreSpriteInputError")))
        assert len(form_errors) == count, "The amount of errors is not equal to " + str(count)

    def verify_login_button_is_not_present(self):
        try:
            login_button = WebDriverWait(self.driver.instance, 5).until(
                EC.visibility_of_element_located((
                    By.XPATH, "//button[text() = 'Log in']")))
            assert False, "Login button was found when it was not supposed to."
        except TimeoutException:
            assert True, "Login button was not found, as expected."
