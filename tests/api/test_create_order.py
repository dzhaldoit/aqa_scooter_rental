import pytest
import allure
import requests
import json

from data import URLs, OrderData


@allure.suite("Тестирование API выбора цвета")
class TestCreateOrder:
    @allure.title(f"Тестирование создания заказа при выборе одного из цветов, обоих цветов, не указан цвет")
    @pytest.mark.parametrize('color', OrderData.color_scooter)
    def test_choose_color_get_order(self, color):
        payload = OrderData.order_data
        payload['color'] = color
        payload = json.dumps(OrderData.order_data)
        response = requests.post(URLs.creating_order, data=payload)
        response_json = response.json()

        assert response.status_code == 201 and 'track' in response_json.keys()