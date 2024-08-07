from aqa_scooter_rental.pages.mobile.couriers_page import mobile_pages


class TestMobile:
    def test_bstack_android(self, mobile_management, static_courier_data):
        mobile_pages.connecting_server()
        mobile_pages.login_courier(static_courier_data)
        mobile_pages.my_orders()
        mobile_pages.logout()
