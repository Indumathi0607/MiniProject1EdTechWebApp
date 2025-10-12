from selenium.webdriver.common.by import By


# Locators class to define locators of all pages in single place.

class Locators:
    # Locators of home page
    courses_menu = (By.XPATH, "(//a[text() = 'Courses'])[2]")  # XPATH
    live_classes_menu = (By.XPATH, "//div[@id='liveclasses']")  # XPATH
    practices_menu = (By.XPATH, "//div[@id='practices']")  # XPATH
    resources_menu = (By.XPATH, "//div[@id='resources']")  # XPATH
    products_menu = (By.XPATH, "//div[@id='solutions']")  # XPATH
    homepage_login_button = (By.XPATH, "//a[@id= 'login-btn']")  # XPATH
    homepage_signup_button = (By.XPATH, "//a[text() = 'Sign up']")  # XPATH
    dobby_iframe = (By.XPATH, "//iframe[@title= 'chat window']") #XPATH
    dobby_image = (By.XPATH, "//img[@id = 'chateleon-container-gif-0']") #XPATH
    chat_input = (By.XPATH, "//div[@class= 'chat-form']")  # XPATH
    paid_courses_menu = (By.XPATH, "//div[text() = 'Paid Courses']")  # XPATH
    live_online_class_submenu = (By.XPATH, "(//p[text()= 'LIVE Online Intensive Program + Placement Guidance'])[2]")  # XPATH
    codekata_submenu = (By.XPATH, "(//p[text() = 'CodeKata'])[2]") #XPATH
    success_story_submenu = (By.XPATH, "(//a[text()='Success Stories'])[2]") #XPATH
    hackerkid_submenu = (By.XPATH, "(//p[text() = 'HackerKID'])[2]") #XPATH


    # Locators of Login page
    login_header = (By.XPATH, "//div[@class = 'login-heading']")  # XPATH
    email_textbox = (By.XPATH, "//input[@id = 'email']")  # XPATH
    password_textbox = (By.XPATH, "//input[@id = 'password']")  # XPATH
    login_page_login_button = (By.XPATH, "//a[@id = 'login-btn']")  # XPATH
    invalid_login_error = (
    By.XPATH, "//input[@type = 'password']/following-sibling::div[contains(@class, 'invalid-feedback')]")  # XPATH
    invalid_email_error = (By.XPATH, "//div[@class = 'invalid-feedback is-invalid']")  # XPATH

    # Locators of Sign up page
    signup_page_header = (By.XPATH, "//h2[text() = 'Sign Up']")  # XPATH
    fullname_textbox = (By.XPATH, "//input[@id= 'name']")  # XPATH
    signup_page_email_textbox = (By.XPATH, "//input[@id= 'email']")  # XPATH
    signup_page_password_textbox = (By.XPATH, "//input[@id = 'password']")  # XPATH
    mobile_number_textbox = (By.XPATH, "//input[@id= 'mobileNumber']")  # XPATH
    signup_page_signup_button = (By.XPATH, "//a[@id= 'signup-btn']")  # XPATH

    # Locators of MyCourses page
    my_course_menu = (By.XPATH, "//div[text() = 'My Courses ']")  # XPATH
    profile_icon = (By.XPATH, "(//img[@id = 'dropdown_contents'])[1]")  # XPATH
    sign_out_button = (By.XPATH, "//ul[@id = 'drop_contents']//li//div[text() = 'Sign Out']")  # XPATH
