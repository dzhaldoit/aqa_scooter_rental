import allure
import pytest
import requests
from jsonschema import validate

from shemas import shemas
from test_data import data
from test_data.data import *
from aqa_scooter_rental.utils.attach import response_logging, response_attaching


@allure.suite("Тестирование API создание курьера")
class TestCourierCreate:

    @allure.title("Тестирование успешного создания курьера при передаче всех полей, "
                  "возвращается корректный код и текст ответа")
    def test_create_courier_successful(self, currier_data, api_url):
        response = requests.post(api_url + Endpoints.create_courier, data=currier_data)
        response_logging(response)
        response_attaching(response)

        assert response.status_code == 201
        assert response.text == Response.response_registration_successful
        validate(response.json(), shemas.post_create)

    @allure.title("Тестирование успешного создания курьера, "
                  "при передаче только обязательных полей(логин,пароль)")
    def test_create_courier_success(self, currier_data_without_firstname, api_url):
        response = requests.post(api_url + Endpoints.create_courier, data=currier_data_without_firstname)
        response_logging(response)
        response_attaching(response)

        assert response.status_code == 201
        assert response.text == Response.response_registration_successful
        validate(response.json(), shemas.post_create)

    @allure.title("Тестирование, что нельзя создать двух одинаковых курьеров")
    def test_not_create_double_courier(self, currier_data, api_url):
        requests.post(api_url + Endpoints.create_courier, data=currier_data)
        response = requests.post(api_url + Endpoints.create_courier, data=currier_data)
        response_logging(response)
        response_attaching(response)

        assert response.status_code == 409
        assert response.json()["message"] == Response.response_login_used
        validate(response.json(), shemas.post_is_used)

    @allure.title("Тестирование, что нельзя создать двух курьеров с одинаковым логином")
    def test_not_create_double_login_courier(self, couriers_data, api_url):
        requests.post(api_url + Endpoints.create_courier, data=couriers_data[0])
        response = requests.post(api_url + Endpoints.create_courier, data=couriers_data[1])
        response_logging(response)
        response_attaching(response)

        assert response.status_code == 409
        assert response.json()["message"] == Response.response_login_used
        validate(response.json(), shemas.post_is_used)

    @allure.title('Тестирование, что если нет логина или пароля, запрос вернет ошибку')
    @pytest.mark.parametrize('key, value', [('login', ''), ('password', '')])
    def test_not_create_without_login_or_password(self, currier_data, key, value, api_url):
        currier_data[key] = value
        response = requests.post(api_url + Endpoints.create_courier, data=currier_data)
        response_logging(response)
        response_attaching(response)

        assert response.status_code == 400
        assert response.json()["message"] == data.Response.response_no_data_account
        validate(response.json(), shemas.post_insufficient_data)
