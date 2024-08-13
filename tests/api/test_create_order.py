import json

import allure
import pytest
import requests
from jsonschema import validate

from aqa_scooter_rental.utils.attach import response_logging, response_attaching
from shemas import shema
from test_data.data import OrderData, Endpoints


@allure.suite("Тестирование API выбора цвета")
class TestCreateOrder:
    @allure.title(f"Тестирование создания заказа при выборе одного из цветов, обоих цветов, не указан цвет")
    @pytest.mark.parametrize('color', OrderData.color_scooter)
    def test_choose_color_get_order(self, color, api_url):
        payload = OrderData.order_data
        payload['color'] = color
        payload = json.dumps(OrderData.order_data)
        response = requests.post(api_url + Endpoints.creating_order, data=payload)
        response_logging(response)
        response_attaching(response)

        assert response.status_code == 201
        assert 'track' in response.json().keys()
        validate(response.json(), shema.post_choose_color)
