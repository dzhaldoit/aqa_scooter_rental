from aqa_scooter_rental.pages.mobile.couriers_pages import api_pages
from aqa_scooter_rental.pages.mobile.couriers_pages import mobile_pages
from tests.api_tests.conftest import currier_data



class TestMobile:
    def test_bstack_android(self, currier_data):
        api_pages.order_take_successful(currier_data)
        mobile_pages.connecting_server()
        mobile_pages.test_login_courier()
        mobile_pages.completed_orders()
        mobile_pages.logout()

