from pytest_bdd import given
from utilities.logger import get_logger

logger = get_logger(__name__)

# ----------------Step definitions--------------
@given('The user opens the GUVI homepage')
def launch_webpage(driver):
    logger.info("Opening GUVI homepage")
    driver.get("https://www.guvi.in/")
