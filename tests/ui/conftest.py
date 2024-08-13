import os

import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from aqa_scooter_rental.utils import attach

DEFAULT_BROWSER_VERSION = "125.0"


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='125.0'
    )


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    selenoid_capabilities = {
        "browserName": "firefox",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    login = os.getenv("LOGIN")
    password = os.getenv("PASSWORD")
    url = os.getenv("SELENOID_URL")

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@{url}wd/hub",
        options=options)

    browser.config.driver = driver
    browser.config.driver_options = options

    browser.config.base_url = 'https://qa-scooter.praktikum-services.ru'

    browser.config.timeout = 10.0
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield browser

    attach.web_screenshot(browser)
    attach.web_html(browser)
    attach.web_video(browser)

    browser.quit()
