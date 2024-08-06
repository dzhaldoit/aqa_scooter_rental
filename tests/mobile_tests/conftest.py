import os

import allure
import pytest
from dotenv import load_dotenv
from appium.options.android import UiAutomator2Options
from selene import browser
from appium import webdriver
from aqa_scooter_rental.utils import attach


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


context = os.getenv('context', 'bstack')
username = os.getenv('USER_NAME')
access_key = os.getenv('ACCESS_KEY')
remote_browser_url = os.getenv('REMOTE_BROWSER_URL')
bstack_app_id = os.getenv('BSTACK_APP_ID')


@pytest.fixture(scope='function')
def android_mobile_management():
    options = UiAutomator2Options().load_capabilities({
        # Specify device and os_version for testing
        "platformName": "android",
        "platformVersion": "12.0",
        "deviceName": "Samsung Galaxy S22 Ultra",

        # Set URL of the application under test
        "app": bstack_app_id,

        # Set other BrowserStack capabilities
        'bstack:options': {
            "projectName": "Android tests",
            "buildName": "browserstack-scooter-rent",
            "sessionName": "BStack scooter-rent",

            # Set your access credentials
            "userName": username,
            "accessKey": access_key
        }
    })

    driver = webdriver.Remote(
        command_executor=remote_browser_url,
        options=options
    )

    browser.config.timeout = 10.0
    browser.config.driver = driver

    yield browser.config.driver

    attach.bstack_screenshot()

    attach.bstack_page_source_xml()

    session_id = browser.driver.session_id

    browser.quit()

    attach.bstack_video(session_id)