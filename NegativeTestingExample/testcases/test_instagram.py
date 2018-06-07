import unittest

from pageobjects.sign_up_page import SignUpPage
from values import strings
from webdriver import Driver


class TestInstagram(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(strings.base_url)

    def test_verify_username_character_limit(self):
        sign_up_page = SignUpPage(self.driver)
        sign_up_page.write_username(strings.long_username)
        sign_up_page.verify_character_count(30)

    def test_verify_required_fields(self):
        sign_up_page = SignUpPage(self.driver)
        sign_up_page.write_email_or_phone(strings.invalid_email)
        sign_up_page.click_next_button()
        sign_up_page.verify_form_errors(3)

    def test_login_button_is_not_present(self):
        sign_up_page = SignUpPage(self.driver)
        sign_up_page.verify_login_button_is_not_present()
