import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

from utility.capture_screenshot import CaptureScreenshot


#Using pytest_addoption hook method allow browser selection via command line
#The default browser is set to Chrome
#action = "store" this stores the browser name given in commandline
#help text is the explanation shown in the 'pytest --help' output.
def pytest_addoption(parser):
    parser.addoption("--browser", action = "store", default = "chrome",
                     help="Browsers supported are: Chrome, Firefox, Edge and Safari(if MACOS)")

@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser").lower()
    driver = None

    # Initialize the webdriver with browser option provided during execution
    if browser == 'chrome':
        driver = (webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))) #driver manager install method used to automatically download the correct driver for the given browser.

    elif browser == 'firefox':
        driver = (webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install())))

    elif browser == 'edge':
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    elif browser == 'safari':
        driver = webdriver.Safari() #this is applicable only for MACOS and the SafariDriver is preinstalled in MAC.

    else:
        raise ValueError(f'Unsupported browser: {browser}')

    # Launch the browser and maximize the window.
    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver # Returns the driver for testcase execution
    driver.quit() #Closes the browser session after test execution.

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == 'call' and rep.failed:
        driver = item.funcargs.get('driver', None)
        CaptureScreenshot.capture_screenshot_on_failure(item, driver)