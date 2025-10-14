from pages.basepage import BasePage
from pages.locators import Locators


class SignUpPage(BasePage):

    def validate_signup_page_title(self, expected_title):
        self.validate_webpage_title(expected_title)

    def validate_signup_page_url(self, expected_url):
        self.validate_current_url(expected_url)

    def is_signup_header_displayed(self):
        self.is_element_visible(Locators.signup_page_header)
