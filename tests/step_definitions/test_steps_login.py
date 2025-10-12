import os

import pytest
from pytest_bdd import scenarios, when, then, parsers

from pages.homepage import HomePage
from pages.loginpage import LoginPage
from pages.mycoursespage import MyCoursesPage
from utility.capture_screenshot import CaptureScreenshot
from utility.logger import get_logger

# Get the path to the feature file
scenarios('../features/login.feature')
logger = get_logger(__name__)


# ----------Fixtures--------------
@pytest.fixture
def home_page(driver):
    # Creating homepage object
    return HomePage(driver)


@pytest.fixture
def login_page(driver):
    # Creating loginpage page object
    return LoginPage(driver)


@pytest.fixture
def my_courses_page(driver):
    # Creating my courses page object
    return MyCoursesPage(driver)


@pytest.fixture
def take_screenshot(driver):
    # Creating CaptureScreenshot object
    return CaptureScreenshot(driver)


# ----------------Step definitions--------------
@when('Clicking on Login button')
def click_on_login_button(home_page):
    logger.info('Clicking on login button in Home page')
    home_page.click_login_button()


@then(parsers.cfparse('Enter the {email}'))
def enter_email_address(login_page, email):
    logger.info('Entering email address')
    login_page.enter_email_address(email)


@then(parsers.cfparse('validate the email {expected_error} is displayed'))
def validate_invalid_email_error(login_page, expected_error, take_screenshot):
    logger.info('Validating error message for invalid email input')
    actual_error = login_page.get_invalid_email_error()
    assert actual_error == expected_error, f"Error mismatch. Expected: {expected_error} and actual: {actual_error}"
    take_screenshot.capture_screenshot('Invalid_email_error_shown')


@then(parsers.cfparse('Enter "{email}" and "{password}"'))
def enter_login_credentials(login_page, email, password, take_screenshot):
    logger.info('Entering email and password')
    # Handling empty email and password
    email = "" if email == "EMPTY" else email.strip()
    password = "" if password == "EMPTY" else password.strip()

    login_page.enter_email_address(email)
    login_page.enter_password(password)
    login_page.click_login_button()
    take_screenshot.capture_screenshot('Login_button_clicked')


@then(parsers.cfparse('validate the login {expected_error} is displayed'))
def validate_invalid_login_error(login_page, expected_error, take_screenshot):
    logger.info('Validating error message for invalid credentials')
    actual_error = login_page.get_invalid_login_error()
    assert actual_error == expected_error, f"Error mismatch. Expected: {expected_error} and actual: {actual_error}"
    take_screenshot.capture_screenshot('Login_error_captured')


@then('Login should be successful')
def validate_login_is_success(my_courses_page, take_screenshot):
    logger.info('Validating is login success with valid credentials')
    assert my_courses_page.is_my_courses_menu_visible, "My courses menu is not visible"
    take_screenshot.capture_screenshot('Login_success')

@then('The user should be able to logout successfully')
def verify_logout_is_success(home_page, my_courses_page, take_screenshot):
    logger.info('Validating navigation back to home page after sign out')
    my_courses_page.click_profile_icon()
    my_courses_page.select_sign_out_option()
    take_screenshot.capture_screenshot('Clicked_on_sign_out_option')

    assert home_page.is_signup_button_visible(), "Signup button in Homepage is not visible"
    take_screenshot.capture_screenshot('Sign_out_success')
