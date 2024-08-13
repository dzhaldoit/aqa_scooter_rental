import allure
import pytest
import requests
from jsonschema import validate

from aqa_scooter_rental.utils import helpers
from aqa_scooter_rental.utils.attach import response_logging, response_attaching


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
    return 'https://qa-scooter.praktikum-services.ru/api/v1/'


@pytest.fixture()
def api_request_and_validate():
    def _api_request_and_validate(url,
                                  method=None,
                                  data=None,
                                  params=None,
                                  schema=None,
                                  expected_status_code=None):
        if method == 'get':
            response = requests.get(url, params=params)
        elif method == 'post':
            response = requests.post(url, json=data)
        else:
            raise ValueError('Неизвестный метод запроса')
        with allure.step(f"Проверка, API возвращает ожидаемый код статус для {url}"):
            assert response.status_code == expected_status_code
        if schema:
            with allure.step(f"Проверка структуры JSON-ответа для {url}"):
                validate(instance=response.json(), schema=schema)
        response_logging(response)
        response_attaching(response)
        return response

    return _api_request_and_validate
