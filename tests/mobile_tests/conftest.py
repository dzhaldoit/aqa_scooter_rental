# import os
#
# import allure
# import pytest
# from dotenv import load_dotenv
# from appium.options.android import UiAutomator2Options
# from selene import browser
# from appium import webdriver
# from aqa_scooter_rental.utils import attach
#
#
# @pytest.fixture(scope="session", autouse=True)
# def load_env():
#     load_dotenv()
#
#
# context = os.getenv('context', 'bstack')
# username = os.getenv('USER_NAME')
# access_key = os.getenv('ACCESS_KEY')
# remote_browser_url = os.getenv('REMOTE_BROWSER_URL')
# bstack_app_id = os.getenv('BSTACK_APP_ID')
#
#
# @pytest.fixture(scope='function')
# def android_mobile_management():
#     options = UiAutomator2Options().load_capabilities({
#         # Specify device and os_version for testing
#         "platformName": "android",
#         "platformVersion": "12.0",
#         "deviceName": "Samsung Galaxy S22 Ultra",
#
#         # Set URL of the application under test
#         "app": bstack_app_id,
#
#         # Set other BrowserStack capabilities
#         'bstack:options': {
#             "projectName": "Android tests",
#             "buildName": "browserstack-scooter-rent",
#             "sessionName": "BStack scooter-rent",
#
#             # Set your access credentials
#             "userName": username,
#             "accessKey": access_key
#         }
#     })
#     browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)
#
#     browser.config.timeout = 10.0
import allure
import pytest
import os

from appium.options.android import UiAutomator2Options
from appium import webdriver
from selene import browser, support
from dotenv import load_dotenv
from aqa_scooter_rental.utils import attach


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


context = os.getenv('context', 'bstack')
username = os.getenv('USER_NAME')
access_key = os.getenv('ACCESS_KEY')
remote_browser_url = os.getenv('REMOTE_BROWSER_URL')
bstack_app_id = os.getenv('BSTACK_APP_ID')


@pytest.fixture(scope='function')
def mobile_management():
    load_dotenv()
    with allure.step('Configurate options'):
        options = UiAutomator2Options().load_capabilities({
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

                "userName": username,
                "accessKey": access_key,
            }
        })

    browser.config.driver = webdriver.Remote(
        remote_browser_url,
        options=options)
    browser.config.timeout = float(os.getenv("TIMEOUT"))

    yield browser.config.driver

    attach.bstack_screenshot()

    attach.bstack_page_source_xml()

    session_id = browser.driver.session_id

    browser.quit()

    attach.bstack_video(session_id)