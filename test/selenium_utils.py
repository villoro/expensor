"""
    Utilities to get a selenium web driver and to open the dash app.
    This is only meant for testing purpouses
"""

import os

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

SELENIUM_PATH_IN_TRAVIS = '/home/travis/selenium/chromedriver'

def get_chrome_webdriver(headless, driver_path=None):
    """
        Get a chrome webdriver.

        Args:
            headless:	bool to allow headless mode

        Returns:		chrome web driver
    """

    if headless:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox") #This make Chromium reachable
        options.add_argument("--no-default-browser-check") #Overrides default choices
        options.add_argument("--disable-default-apps")
        options.add_argument("--window-size=1920x1080")

        # Allow custom path for webdriver
        if driver_path is not None:
            return webdriver.Chrome(driver_path, chrome_options=options)

        # If none provided use default
        return webdriver.Chrome(chrome_options=options)

    # If headless then use local webdriver
    return webdriver.Chrome()


def open_dash(headless=False):
    """
        Starts a chrome web driver and opens the dash app. Then it waits until the app is loaded

        Args:
            headless:	bool to allow headless mode

        Returns:		chrome web driver
    """

    # If run from travis it is better to run it headless
    if "/home/travis/" in os.getcwd():
        driver = get_chrome_webdriver(headless=True, driver_path=SELENIUM_PATH_IN_TRAVIS)

    # If not, allow both options
    else:
        driver = get_chrome_webdriver(headless)

    # Open dash app
    driver.get("http://localhost:8050/")

    # Wait until dash is opened
    for _ in range(30):
        sleep(1)

        if 'Updating...' not in driver.title:
            break

    return driver
