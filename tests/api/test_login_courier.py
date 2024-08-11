import allure
import pytest
import requests
from jsonschema import validate

from aqa_scooter_rental.utils import helpers
from shemas import shemas
from test_data.data import *
from aqa_scooter_rental.utils.attach import response_logging, response_attaching


@allure.suite("Тестирование API авторизации курьера")
class TestLoginCurrier:

    @allure.title('Курьер может авторизоваться передав обязательные поля, ответ возвращает id')
    def test_login_courier_successful(self, currier_data_without_firstname, api_url):
        requests.post(api_url + Endpoints.create_courier, data=currier_data_without_firstname)
        response = requests.post(api_url + Endpoints.login_courier,
                                 data=currier_data_without_firstname)
        response_logging(response)
        response_attaching(response)

        assert response.status_code == 200
        assert response.json()["id"] != []
        validate(response.json(), shemas.post_required_fields)

    @allure.title('Тестирование, что если нет логина или пароля, запрос вернет ошибку')
    @pytest.mark.parametrize('key, value', [('login', ''), ('password', '')])
    def test_not_authoriz_without_login_or_password(self, currier_data, key, value, api_url):
        currier_data[key] = value
        response = requests.post(api_url + Endpoints.login_courier, data=currier_data)
        response_logging(response)
        response_attaching(response)

        assert response.status_code == 400
        assert response.json()["message"] == Response.response_no_data_input
        validate(response.json(), shemas.post_insufficient_data)

    @allure.title('Тестирование, что если не верный(не существующий) логин или пароль, запрос вернет ошибку')
    @pytest.mark.parametrize('key, value', [('login', helpers.GenerateString.generate_random_string(10)),
                                            ('password', helpers.GenerateString.generate_random_string(10))])
    def test_not_authoriz_bad_login_or_password(self, currier_data, key, value, api_url):
        requests.post(api_url + Endpoints.create_courier, data=currier_data)
        currier_data[key] = value
        response = requests.post(api_url + Endpoints.login_courier, data=currier_data)
        response_logging(response)
        response_attaching(response)

        assert response.status_code == 404
        assert response.json()["message"] == Response.response_account_not_found
        validate(response.json(), shemas.post_insufficient_data)
