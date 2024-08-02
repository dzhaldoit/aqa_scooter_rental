import pytest
from selenium import webdriver
import helpers


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Firefox()
    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture
def currier_data():
    data_currier = helpers.GenerateDataCourier()
    return data_currier.generate_data_courier()


@pytest.fixture
def couriers_data():
    data_currier = helpers.GenerateDataCourier()
    data_currier_2 = helpers.GenerateDataCourier()
    return data_currier.generate_data_courier_static_login(), data_currier_2.generate_data_courier_static_login()


@pytest.fixture
def currier_data_without_firstname(currier_data):
    currier_data['firstName'] = ''
    return currier_data



