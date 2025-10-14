from pages.basepage import BasePage
from pages.locators import Locators


class MyCoursesPage(BasePage):

    def is_my_courses_menu_visible(self):
        return self.is_element_visible(Locators.my_course_menu)

    def click_profile_icon(self):
        self.click_element(Locators.profile_icon)

    def select_sign_out_option(self):
        self.click_element(Locators.sign_out_button)
