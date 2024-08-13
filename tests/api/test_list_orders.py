import allure
import requests
from jsonschema import validate

from aqa_scooter_rental.utils import helpers
from aqa_scooter_rental.utils.attach import response_logging, response_attaching
from shemas import shema
from test_data import data


@allure.suite("Тестирование API списка заказов")
class TestListOrder:
    @allure.title("Тестирование получения списка заказов")
    def test_order_list(self, api_url):
        body = data.LimitPageOrders.limit_page_orders
        response = requests.get(api_url + data.Endpoints.creating_order, params=body)
        response_logging(response)
        response_attaching(response)

        assert 200 == response.status_code
        assert type(response.json()["orders"]) == list
        validate(response.json(), shema.get_order_list)
