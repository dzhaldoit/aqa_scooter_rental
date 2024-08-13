import allure
import pytest

from aqa_scooter_rental.utils import helpers
from shemas import shema
from test_data.data import *


@allure.suite("Тестирование API авторизации курьера")
class TestLoginCurrier:

    @allure.title('Курьер может авторизоваться передав обязательные поля, ответ возвращает id')
    def test_login_courier_successful(self, currier_data_without_firstname, api_url, api_request_and_validate):
        api_request_and_validate(api_url + Endpoints.create_courier,
                                 method='post',
                                 data=currier_data_without_firstname,
                                 schema=shema.post_create,
                                 expected_status_code=201)

        response = api_request_and_validate(api_url + Endpoints.login_courier,
                                            method='post',
                                            data=currier_data_without_firstname,
                                            schema=shema.post_required_fields,
                                            expected_status_code=200)

        assert response.json()["id"] != []

    @allure.title('Тестирование, что если нет логина или пароля, запрос вернет ошибку')
    @pytest.mark.parametrize('key, value', [('login', ''), ('password', '')])
    def test_not_authoriz_without_login_or_password(self, currier_data, key, value, api_url, api_request_and_validate):
        currier_data[key] = value
        response = api_request_and_validate(api_url + Endpoints.login_courier,
                                            method='post',
                                            data=currier_data,
                                            schema=shema.post_insufficient_data,
                                            expected_status_code=400)

        assert response.json()["message"] == Response.response_no_data_input

    @allure.title('Тестирование, что если не верный(не существующий) логин или пароль, запрос вернет ошибку')
    @pytest.mark.parametrize('key, value', [('login', helpers.GenerateString.generate_random_string(10)),
                                            ('password', helpers.GenerateString.generate_random_string(10))])
    def test_not_authoriz_bad_login_or_password(self, currier_data, key, value, api_url, api_request_and_validate):
        api_request_and_validate(api_url + Endpoints.create_courier,
                                 method='post',
                                 data=currier_data,
                                 schema=shema.post_create,
                                 expected_status_code=201)

        currier_data[key] = value
        response = api_request_and_validate(api_url + Endpoints.login_courier,
                                            method='post',
                                            data=currier_data,
                                            schema=shema.post_insufficient_data,
                                            expected_status_code=404)

        assert response.json()["message"] == Response.response_account_not_found
