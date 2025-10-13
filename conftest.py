import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

from utilities.capture_screenshot import CaptureScreenshot


# Using pytest_add option hook method allow browser selection via command line
# The default browser is set to Chrome
# action = "store" this stores the browser name given in commandline
# help text is the explanation shown in the 'pytest --help' output.
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Browsers supported are: Chrome, Firefox, Edge and Safari(if MACOS)")


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser").lower()  # Get the browser name from the run command
    driver = None

    # Initialize the webdriver with browser option provided during execution
    if browser == 'chrome':
        driver = (webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install())))  # driver manager install method used to automatically download the correct driver for the given browser.

    elif browser == 'firefox':
        driver = (webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install())))

    elif browser == 'edge':
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    elif browser == 'safari':
        driver = webdriver.Safari()  # this is applicable only for MACOS and the SafariDriver is preinstalled in MAC.

    else:
        raise ValueError(f'Unsupported browser: {browser}')

    # Launch the browser and maximize the window.
    driver.maximize_window()
    driver.implicitly_wait(5)

    yield driver  # Returns the driver for testcase execution
    driver.quit()  # Closes the browser session after tests execution.


# Take screenshot when the testcase fails.
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == 'call' and rep.failed:
        driver = item.funcargs.get('driver', None)

    # Since the step def are not directly involving the driver fixture, steps to find driver indirectly
        if not driver:
            for fixture_value in item.funcargs.values():
                if hasattr(fixture_value, 'driver'):
                    driver = fixture_value.driver
                    break

        if driver and hasattr(driver, 'get_screenshot_as_png'):
            CaptureScreenshot.capture_screenshot_on_failure(driver, item)
        else:
            print(f'No screenshot taken since no valid driver for {item.name}')


# Setting up common test steps path globally
pytest_plugins = [
    "tests.step_definitions.test_steps_common"
]
