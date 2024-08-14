import pytest
from allure_commons._allure import step
from appium import webdriver
from dotenv import load_dotenv
from selene import browser

import config
from aqa_scooter_rental.utils import attach


def pytest_addoption(parser):
    parser.addoption(
        "--context",
        default="bstack",
        help="Specify the test context"
    )


def pytest_configure(config):
    context = config.getoption("--context")
    env_file_path = f".env.{context}"

    load_dotenv(dotenv_path=env_file_path, verbose=True)


@pytest.fixture
def context(request):
    return request.config.getoption("--context")


@pytest.fixture
def static_courier_data():
    static_courier_data = {
        "login": "Mamon",
        "password": "1111"
    }
    return static_courier_data


@pytest.fixture(scope='function')
def mobile_management(context):
    options = config.to_driver_options(context=context)

    browser.config.driver = webdriver.Remote(options.get_capability('remote_url'), options=options)
    browser.config.timeout = 10.0

    yield

    with step('Add screenshot'):
        attach.mobile_screenshot()

    with step('Add xml'):
        attach.mobile_xml()

    with step('Close driver'):
        browser.quit()

    if context == 'bstack':
        with step('Add video'):
            attach.bstack_video()
