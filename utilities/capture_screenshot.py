import time

import allure
from allure_commons.types import AttachmentType


class CaptureScreenshot:

    def __init__(self, driver):
        self.driver = driver

    # Method to capture the screenshot
    def capture_screenshot(self, screenshot_name):
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )

    # Automatically captures the screenshot on tests failure
    # Keeping this as static method in order to call easily by pytest hook without creating object
    @staticmethod
    def capture_screenshot_on_failure(driver, item):
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name=f'Failure_{item.name}_{int(time.time())}',
                attachment_type=AttachmentType.PNG
            )
