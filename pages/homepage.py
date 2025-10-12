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
        return self.is_element_visible(Locators.homepage_login_button)

    def click_login_button(self):
        self.click_element(Locators.homepage_login_button)

    def is_signup_button_visible(self):
        return self.is_element_visible(Locators.homepage_signup_button)

    def click_signup_button(self):
        self.click_element(Locators.homepage_signup_button)

    def is_menu_in_homepage_visible(self, menu_item):
        if menu_item == 'Courses':
            menu_item = Locators.courses_menu
        elif menu_item == 'LIVE Classes':
            menu_item = Locators.live_classes_menu
        elif menu_item == 'Practice':
            menu_item = Locators.practices_menu
        elif menu_item == 'Resources':
            menu_item = Locators.resources_menu
        elif menu_item == 'Products':
            menu_item = Locators.products_menu
        else:
            raise ValueError(f"Given {menu_item} is not a valid menu item")
        return self.is_element_visible(menu_item)

    def is_menu_in_homepage_accessible(self, menu_item):
        if menu_item == 'Courses':
            element_to_click = Locators.courses_menu
            element_to_validate = Locators.paid_courses_menu
        elif menu_item == 'LIVE Classes':
            element_to_click = Locators.live_classes_menu
            element_to_validate = Locators.live_online_class_submenu
        elif menu_item == 'Practice':
            element_to_click = Locators.practices_menu
            element_to_validate = Locators.codekata_submenu
        elif menu_item == 'Resources':
            element_to_click = Locators.resources_menu
            element_to_validate = Locators.success_story_submenu
        elif menu_item == 'Products':
            element_to_click = Locators.products_menu
            element_to_validate = Locators.hackerkid_submenu
        else:
            raise ValueError(f'Given {menu_item} is not a valid option')

        self.click_element(element_to_click)
        return self.is_element_visible(element_to_validate)

    def is_dobby_assistant_visible(self):
        return self.is_element_visible(Locators.dobby_image)

    def click_dobby_assistant(self):
        self.click_element(Locators.dobby_image)

    def is_chat_input_textbox_visible(self):
        return self.is_element_visible(Locators.chat_input)

    def switch_to_dobby_iframe(self):
        self.switch_to_iframe(Locators.dobby_iframe)

