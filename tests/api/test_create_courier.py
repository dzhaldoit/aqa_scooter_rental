import allure
import pytest
from jsonschema import validate

from shemas import shema
from test_data import data
from test_data.data import *


@allure.suite("Тестирование API создание курьера")
class TestCourierCreate:

    @allure.title("Тестирование успешного создания курьера при передаче всех полей, "
                  "возвращается корректный код и текст ответа")
    def test_create_courier_successful(self, currier_data, api_url, api_request_and_validate):
        response = api_request_and_validate(api_url + Endpoints.create_courier,
                                            method='post',
                                            data=currier_data,
                                            schema=shema.post_create,
                                            expected_status_code=201)

        assert response.text == Response.response_registration_successful

    @allure.title("Тестирование успешного создания курьера, "
                  "при передаче только обязательных полей(логин,пароль)")
    def test_create_courier_success(self, currier_data_without_firstname, api_url, api_request_and_validate):
        response = api_request_and_validate(api_url + Endpoints.create_courier,
                                            method='post',
                                            data=currier_data_without_firstname,
                                            schema=shema.post_create,
                                            expected_status_code=201)

        assert response.status_code == 201
        assert response.text == Response.response_registration_successful
        validate(response.json(), shema.post_create)

    @allure.title("Тестирование, что нельзя создать двух одинаковых курьеров")
    def test_not_create_double_courier(self, currier_data, api_url, api_request_and_validate):
        api_request_and_validate(api_url + Endpoints.create_courier,
                                 method='post',
                                 data=currier_data,
                                 expected_status_code=201)
        response = api_request_and_validate(api_url + Endpoints.create_courier,
                                            method='post',
                                            data=currier_data,
                                            schema=shema.post_is_used,
                                            expected_status_code=409)

        assert response.json()["message"] == Response.response_login_used

    @allure.title("Тестирование, что нельзя создать двух курьеров с одинаковым логином")
    def test_not_create_double_login_courier(self, couriers_data, api_url, api_request_and_validate):
        response = api_request_and_validate(api_url + Endpoints.create_courier,
                                            method='post',
                                            data=couriers_data[0],
                                            schema=shema.post_is_used,
                                            expected_status_code=409)

        assert response.json()["message"] == Response.response_login_used

    @allure.title('Тестирование, что если нет логина или пароля, запрос вернет ошибку')
    @pytest.mark.parametrize('key, value', [('login', ''), ('password', '')])
    def test_not_create_without_login_or_password(self, currier_data, key, value, api_url, api_request_and_validate):
        currier_data[key] = value
        response = api_request_and_validate(api_url + Endpoints.create_courier,
                                            method='post',
                                            data=currier_data,
                                            expected_status_code=400,
                                            schema=shema.post_insufficient_data)

        assert response.json()["message"] == data.Response.response_no_data_account
