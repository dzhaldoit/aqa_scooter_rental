import pytest
from allure_commons._allure import step
from appium import webdriver
from dotenv import load_dotenv
from selene import browser

from aqa_scooter_rental.utils import attach

load_dotenv(dotenv_path='.env.bstack')


@pytest.fixture
def static_courier_data():
    static_courier_data = {
        "login": "Mamon",
        "password": "1111"
    }
    return static_courier_data


@pytest.fixture(scope='function')
def mobile_management():
    with step('Configurate options'):
        from project import config_app
        options = config_app.to_driver_options()
        browser.config.driver = webdriver.Remote(options.get_capability('remote_url'), options=options)

    yield

    with step('Add screenshot'):
        attach.bstack_screenshot()

    with step('Add html'):
        attach.bstack_page_source_xml()

    with step('Close driver'):
        browser.quit()

    with step('Add video'):
        attach.bstack_video()
