import os

import pytest
from pytest_bdd import scenarios, when, then, parsers

from pages.homepage import HomePage
from pages.loginpage import LoginPage
from pages.signuppage import SignUpPage
from utilities.capture_screenshot import CaptureScreenshot
from utilities.logger import get_logger
from utilities.constants import BASE_URL, LOGIN_URL, SIGNUP_URL, LOGIN_TITLE, SIGNUP_TITLE, HOME_TITLE

# Get the path to the feature file
scenarios('../features/homepage.feature')
logger = get_logger(__name__)


# ----------Fixtures--------------
@pytest.fixture
def home_page(driver):
    # Creating homepage object
    return HomePage(driver)


@pytest.fixture
def login_page(driver):
    # Creating loginpage object
    return LoginPage(driver)


@pytest.fixture
def signup_page(driver):
    # Creating signup page object
    return SignUpPage(driver)


@pytest.fixture
def take_screenshot(driver):
    # Creating CaptureScreenshot object
    return CaptureScreenshot(driver)


# ----------------Step definitions--------------
@when('The page is fully loaded')
def validate_page_is_loaded(home_page):
    logger.info("Waiting for the GUVI homepage to fully load")
    home_page.wait_for_page_load()


@then('The user should see the signup button')
def validate_signup_button_displayed(home_page, take_screenshot):
    logger.info("Validate the Sigup button is visible after GUVi homepage is loaded")
    assert home_page.get_signup_button_text() == 'Sign up', 'Sign up button not loaded'
    take_screenshot.capture_screenshot("Homepage_loaded")


@then('The Login button should be visible and clickable')
def validate_login_button(home_page, login_page, take_screenshot):
    logger.info("Verify the login button in home page is visible")
    assert home_page.is_login_button_visible(), "Login button in Homepage is not visible"
    take_screenshot.capture_screenshot("Homepage_login_button_visible")

    logger.info("Click on the login button in homepage")
    home_page.click_login_button()
    assert login_page.is_login_header_displayed(), "Login header not displayed"
    take_screenshot.capture_screenshot("LoginPage_loaded")


@then('The Sign up button should be visible and clickable')
def validate_signup_button(home_page, signup_page, take_screenshot):
    logger.info("Verify the signup button in home page is visible")
    assert home_page.is_signup_button_visible(), "Signup button in Homepage is not visible"
    take_screenshot.capture_screenshot("HomePage_signup_button_visible")

    logger.info("Click on the signup button in homepage")
    home_page.click_signup_button()
    signup_page.is_signup_header_displayed()
    take_screenshot.capture_screenshot("SignupPage_loaded")


@then(parsers.cfparse('Verify the "{webpage}" page title'))
def validate_webpage_title(webpage, home_page, login_page, signup_page, take_screenshot):
    logger.info(f"Validating the {webpage} page title")
    if webpage == 'home':
        home_page.validate_home_page_title(HOME_TITLE)
    elif webpage == 'login':
        login_page.validate_login_page_title(LOGIN_TITLE)
    elif webpage == 'signup':
        signup_page.validate_signup_page_title(SIGNUP_TITLE)
    else:
        raise ValueError(f'Page not found: {webpage}')
    take_screenshot.capture_screenshot(f"{webpage}_page_title_verified")


@then(parsers.cfparse('Verify the "{webpage}" page url'))
def validate_webpage_url(webpage, home_page, login_page, signup_page, take_screenshot):
    logger.info(f"Validating the {webpage} page url")
    if webpage == 'home':
        home_page.validate_home_page_url(BASE_URL)
    elif webpage == 'login':
        login_page.validate_login_page_url(LOGIN_URL)
    elif webpage == 'signup':
        signup_page.validate_signup_page_url(SIGNUP_URL)
    else:
        raise ValueError(f'Page not found: {webpage}')
    take_screenshot.capture_screenshot(f"{webpage}_page_URL_verified")


@then('Verify the Sign up page is loaded properly')
def verify_signup_page_loaded(signup_page, take_screenshot):
    logger.info("Verifying is sign up page loaded")
    signup_page.is_signup_header_displayed()
    take_screenshot.capture_screenshot('Signup_page_header_verified')


@then(parsers.cfparse('The {menu} option is visible'))
def verify_menu_items_visible(home_page, menu, take_screenshot):
    logger.info(f"Verifying {menu} option is visible")
    assert home_page.is_menu_in_homepage_visible(menu), f"Given {menu} is not visible in homepage"
    take_screenshot.capture_screenshot(f'{menu}_is_visible')


@then(parsers.cfparse('The {menu} is accessible'))
def verify_menu_items_accessible(home_page, menu, take_screenshot):
    logger.info(f"Verifying {menu} option is accessible")
    assert home_page.is_menu_in_homepage_accessible(menu), f"Given {menu} is not accessible in homepage"
    take_screenshot.capture_screenshot(f'{menu}_is_accessible')


@then('The Dobby GUVI assistant should be visible and clickable')
def validate_dobby_GUVI_assistant(home_page, take_screenshot):
    # Verifying the Dobby GUVI assistant is visible
    logger.info("Verifying the Dobby GUVI assistant is visible in Homepage")
    assert home_page.is_dobby_assistant_visible, "Dobby GUVI assistant is missing"

    logger.info("Clicking on Dobby assistant")
    home_page.click_dobby_assistant()
    take_screenshot.capture_screenshot('Clicking_on_Dobby_GUVI_Assistant')

    # Verifying the chat input textbox is visible in Dobby GUVI assistant
    logger.info("Verifying the chat input textbox is visible in Dobby GUVI assistant")
    home_page.switch_to_dobby_iframe()
    assert home_page.is_chat_input_textbox_visible(), f"Chat box is missing in Dobby GUVI assistant"
    take_screenshot.capture_screenshot('Dobby_chatbox_is_visible')
