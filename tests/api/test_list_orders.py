import allure
from jsonschema import validate

from aqa_scooter_rental.utils import helpers
from aqa_scooter_rental.utils.attach import response_logging, response_attaching
from shemas import shemas


@allure.suite("Тестирование API списка заказов")
class TestListOrder:
    @allure.title("Тестирование получения списка заказов")
    def test_order_list(self):
        get_order_instance = helpers.GetOrder()
        body = get_order_instance.set_param_order_list()
        response = helpers.GetOrder.get_orders_list(body)
        response_logging(response)
        response_attaching(response)

        assert 200 == response.status_code
        assert type(response.json()["orders"]) == list
        validate(response.json(), shemas.get_order_list)
