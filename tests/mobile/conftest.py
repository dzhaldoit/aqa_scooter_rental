import pytest
from selene import browser
from appium import webdriver
from dotenv import load_dotenv
from aqa_scooter_rental.utils import attach
from allure_commons._allure import step


def pytest_addoption(parser):
    parser.addoption('--context', default='bstack')


def pytest_configure(config):
    context = config.getoption("--context")
    env_file = f'.env.{context}'
    load_dotenv(dotenv_path=env_file)


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
    with step('Configurate options'):
        from project import config_app
        options = config_app.to_driver_options(context=context)
        browser.config.driver = webdriver.Remote(options.get_capability('remote_url'), options=options)

    yield

    with step('Add screenshot'):
        attach.bstack_screenshot()

    with step('Add html'):
        attach.bstack_page_source_xml()

    with step('Close driver'):
        browser.quit()

    if context == 'bstack':
        with step('Add video'):
            attach.bstack_video()
