from selenium.webdriver.common.by import By


#Locators class to define locators of all pages in single place.

class Locators:
    #Locators of home page
    courses_menu = (By.XPATH, "//ul/a[text()= 'Courses']")               #XPATH
    live_classes_menu = (By.XPATH, "//div[@id='liveclasses']")            #XPATH
    practices_menu = (By.XPATH, "//div[@id='practices']")                #XPATH
    resources_menu = (By.XPATH, "//div[@id='resources']")                #XPATH
    solutions_menu = (By.XPATH, "//div[@id='solutions']")                #XPATH
    homepage_login_button = (By.XPATH, "//a[@id= 'login-btn']")                   #XPATH
    homepage_signup_button = (By.XPATH, "//a[text() = 'Sign up']")                #XPATH
    dobby_notification = (By.XPATH, "//div[@id = 'ym-auto-pop-up-notification']")   #XPATH
    dobby_header = (By.XPATH, "//div[@id = 'ym-auto-pop-up-header']")      #XPATH
    dobby_description = (By.ID, "ym-auto-pop-up-description")              #ID

    #Locators of Login page
    login_header = (By.XPATH, "//div[@class = 'login-heading']")         #XPATH
    email_textbox = (By.XPATH, "//input[@id = 'email']")                 #XPATH
    password_textbox = (By.XPATH, "//input[@id = 'password']")           #XPATH
    login_page_login_button = (By.XPATH, "//a[@id = 'login-btn']")        #XPATH

    #Locators of Sign up page
    signup_page_header = (By.XPATH, "//h2[text() = 'Sign Up']")                      #XPATH
    fullname_textbox = (By.XPATH, "//input[@id= 'name']")                            #XPATH
    signup_page_email_textbox = (By.XPATH, "//input[@id= 'email']")                  #XPATH
    signup_page_password_textbox = (By.XPATH, "//input[@id = 'password']")           #XPATH
    mobile_number_textbox = (By.XPATH, "//input[@id= 'mobileNumber']")               #XPATH
    signup_page_signup_button = (By.XPATH, "//a[@id= 'signup-btn']")                 #XPATH




