from pages.basepage import BasePage
from pages.locators import Locators


class LoginPage(BasePage):
    def validate_login_page_title(self, expected_title):
        self.validate_webpage_title(expected_title)

    def validate_login_page_url(self, expected_url):
        self.validate_current_url(expected_url)

    def is_login_header_displayed(self):
        return self.is_element_visible(Locators.login_header)

    def enter_email_address(self, email):
        self.enter_text(Locators.email_textbox, email)

    def enter_password(self, password):
        self.enter_text(Locators.password_textbox, password)

    def click_login_button(self):
        self.click_element(Locators.login_page_login_button)

    def get_invalid_email_error(self):
        error_text = self.get_element_text(Locators.invalid_email_error)
        return error_text

    def get_invalid_login_error(self):
        error_text = self.get_element_text(Locators.invalid_login_error)
        return error_text
