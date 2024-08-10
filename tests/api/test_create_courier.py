import pytest
import allure
import requests

import data
from data import Response, URLs


@allure.suite("Тестирование API создание курьера")
class TestCourierCreate:

    @allure.title("Тестирование успешного создания курьера при передаче всех полей, "
                  "возвращается корректный код и текст ответа")
    def test_create_courier_successful(self, currier_data):
        response = requests.post(URLs.create_courier, data=currier_data)
        assert response.status_code == 201 and response.text == Response.response_registration_successful

    @allure.title("Тестирование успешного создания курьера, "
                  "при передаче только обязательных полей(логин,пароль)")
    def test_create_courier_success(self, currier_data_without_firstname):
        response = requests.post(URLs.create_courier, data=currier_data_without_firstname)
        assert response.status_code == 201 and response.text == Response.response_registration_successful

    @allure.title("Тестирование, что нельзя создать двух одинаковых курьеров")
    def test_not_create_double_courier(self, currier_data):
        requests.post(URLs.create_courier, data=currier_data)
        response2 = requests.post(URLs.create_courier, data=currier_data)

        assert response2.status_code == 409 and response2.json()["message"] == Response.response_login_used

    @allure.title("Тестирование, что нельзя создать двух курьеров с одинаковым логином")
    def test_not_create_double_login_courier(self, couriers_data):
        requests.post(URLs.create_courier, data=couriers_data[0])
        response2 = requests.post(URLs.create_courier, data=couriers_data[1])

        assert response2.status_code == 409 and response2.json()["message"] == Response.response_login_used

    @allure.title('Тестирование, что если нет логина или пароля, запрос вернет ошибку')
    @pytest.mark.parametrize('key, value', [('login', ''), ('password', '')])
    def test_not_create_without_login_or_password(self, currier_data, key, value):
        currier_data[key] = value
        currier_resp = requests.post(URLs.create_courier, data=currier_data)
        assert (currier_resp.status_code == 400 and
                currier_resp.json()["message"] == data.Response.response_no_data_account)
