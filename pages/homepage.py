from pages.basepage import BasePage
from pages.locators import Locators

class HomePage(BasePage):

    def validate_home_page_title(self, expected_title):
        self.validate_webpage_title(expected_title)

    def validate_home_page_url(self, expected_url):
        self.validate_current_url(expected_url)

    def get_signup_button_text(self):
        signup_button_text = self.get_element_text(Locators.homepage_signup_button)
        return signup_button_text

    def is_login_button_visible(self):
        assert self.is_element_visible(Locators.homepage_login_button), "Login button in Homepage is not visible"

    def click_login_button(self):
        self.click_element(Locators.homepage_login_button)

    def is_signup_button_visible(self):
        assert self.is_element_visible(Locators.homepage_signup_button), "Signup button in Homepage is not visible"

    def click_signup_button(self):
        self.click_element(Locators.homepage_signup_button)




