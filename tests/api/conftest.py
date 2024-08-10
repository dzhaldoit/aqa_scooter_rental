import json

import allure
import pytest
import requests
from allure_commons._allure import step
from allure_commons.types import AttachmentType

from aqa_scooter_rental.utils import helpers
from test_data import data


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


@pytest.fixture
def api_url():
    return 'https://qa-scooter.praktikum-services.ru/'

