import json
import allure

from shemas import shema
from test_data.data import OrderData, Endpoints


@allure.suite("Тестирование API выбора цвета")
class TestCreateOrder:

    @allure.title("Тестирование создания заказа при выборе одного цвета")
    def test_choose_one_color_get_order(self, api_url, api_request_and_validate):
        color = OrderData.color_scooter[0]
        payload = OrderData.order_data
        payload['color'] = color
        payload = json.dumps(payload)
        response = api_request_and_validate(api_url + Endpoints.creating_order,
                                            method='post',
                                            params=payload,
                                            expected_status_code=201,
                                            schema=shema.post_choose_color)

        assert 'track' in response.json().keys()

    @allure.title("Тестирование создания заказа при выборе обоих цветов")
    def test_choose_both_colors_get_order(self, api_url, api_request_and_validate):
        color = OrderData.color_scooter[2]
        payload = OrderData.order_data
        payload['color'] = color
        payload = json.dumps(payload)
        response = api_request_and_validate(api_url + Endpoints.creating_order,
                                            method='post',
                                            params=payload,
                                            expected_status_code=201,
                                            schema=shema.post_choose_color)

        assert 'track' in response.json().keys()

    @allure.title("Тестирование создания заказа при не указанном цвете")
    def test_choose_no_color_get_order(self, api_url, api_request_and_validate):
        color = OrderData.color_scooter[3]
        payload = OrderData.order_data
        payload['color'] = color
        payload = json.dumps(payload)
        response = api_request_and_validate(api_url + Endpoints.creating_order,
                                            method='post',
                                            params=payload,
                                            expected_status_code=201,
                                            schema=shema.post_choose_color)

        assert 'track' in response.json().keys()
