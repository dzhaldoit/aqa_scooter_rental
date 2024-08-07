import allure
import pytest
import requests
import data
import helpers


@allure.suite("Тестирование API авторизации курьера")
class TestLoginCurrier:

    @allure.title('Курьер может авторизоваться передав обязательные поля, ответ возвращает id')
    def test_login_courier_successful(self, currier_data_without_firstname):
        requests.post(data.URLs.create_courier, data=currier_data_without_firstname)
        response_login = requests.post(data.URLs.login_courier, data=currier_data_without_firstname)
        assert response_login.status_code == 200 and response_login.json()["id"] != []

    @allure.title('Тестирование, что если нет логина или пароля, запрос вернет ошибку')
    @pytest.mark.parametrize('key, value', [('login', ''), ('password', '')])
    def test_not_authoriz_without_login_or_password(self, currier_data, key, value):
        currier_data[key] = value
        currier_resp = requests.post(data.URLs.login_courier, data=currier_data)
        assert currier_resp.status_code == 400 and currier_resp.json()[
            "message"] == data.Response.response_no_data_input

    @allure.title('Тестирование, что если не верный(не существующий) логин или пароль, запрос вернет ошибку')
    @pytest.mark.parametrize('key, value', [('login', helpers.GenerateString.generate_random_string(10)),
                                            ('password', helpers.GenerateString.generate_random_string(10))])
    def test_not_authoriz_bad_login_or_password(self, currier_data, key, value):
        requests.post(data.URLs.create_courier, data=currier_data)
        currier_data[key] = value
        currier_resp = requests.post(data.URLs.login_courier, data=currier_data)
        assert currier_resp.status_code == 404 and currier_resp.json()[
            "message"] == data.Response.response_account_not_found
