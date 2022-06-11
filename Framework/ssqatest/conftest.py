import pytest
import os
from selenium import webdriver


@pytest.fixture(scope="class")
def init_driver(request):
    browser_options = ["chrome", "ch", "firefox", "ff"]
    browser = os.getenv("BROWSER").lower()
    if not browser:
        raise Exception("The environment variable 'BROWSER' must be set.")
    if browser not in browser_options:
        raise Exception(
            f"Browser {browser} is not on the acceptable browsers list."
            f"Acceptable browswers include {browser_options}"
        )
    elif browser in ["chrome", "ch"]:
        driver = webdriver.Chrome()
    elif browser in ["firefox", "ff"]:
        driver = webdriver.Firefox()
    request.cls.driver = driver
    yield
    driver.quit()
