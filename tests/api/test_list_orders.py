import allure

from aqa_scooter_rental.utils import helpers
from jsonschema import validate
from shemas import shemas


@allure.suite("Тестирование API списка заказов")
class TestListOrder:
    @allure.title("Тестирование получения списка заказов")
    def test_order_list(self):
        body = helpers.GetOrder.set_param_order_list(self)
        response = helpers.GetOrder.get_orders_list(body)

        assert 200 == response.status_code
        assert type(response.json()["orders"]) == list
        validate(response.json(), shemas.get_order_list)
