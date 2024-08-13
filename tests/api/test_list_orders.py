import allure

from shemas import shema
from test_data import data


@allure.suite("Тестирование API списка заказов")
class TestListOrder:
    @allure.title("Тестирование получения списка заказов")
    def test_order_list(self, api_url, api_request_and_validate):
        body = data.LimitPageOrders.limit_page_orders
        response = api_request_and_validate(api_url + data.Endpoints.creating_order,
                                            method='get',
                                            params=body,
                                            expected_status_code=200,
                                            schema=shema.get_order_list)

        assert type(response.json()["orders"]) == list
