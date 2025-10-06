from pages.basepage import BasePage
from pages.locators import Locators

class LoginPage(BasePage):
    def validate_login_page_title(self, expected_title):
        self.validate_webpage_title(expected_title)

    def validate_login_page_url(self, expected_url):
        self.validate_current_url(expected_url)

    def is_login_header_displayed(self):
        assert self.is_element_visible(Locators.login_header), "Login header not displayed"

    def enter_username(self, username):
        self.enter_text(username)