import allure
import helpers


@allure.suite("Тестирование API списка заказов")
class TestListOrder:
    @allure.title("Тестирование получения списка заказов")
    def test_order_list(self):
        body = helpers.GetOrder.set_param_order_list(self)
        response_data = helpers.GetOrder.get_orders_list(body)
        assert 200 == response_data.status_code and type(response_data.json()["orders"]) == list