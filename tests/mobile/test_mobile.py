import allure
from aqa_scooter_rental.pages.mobile.couriers_page import mobile_pages


@allure.suite("Тестирование авторизации курьера")
class TestMobile:
    @allure.title('Тестирование авторизации курьера в приложении')
    def test_authorization(self, mobile_management, static_courier_data):
        with allure.step("Открытие вкладки"):
            mobile_pages.connecting_server()
        with allure.step("Авторизация курьера"):
            mobile_pages.login_courier(static_courier_data)
        with allure.step("Мои заказы"):
            mobile_pages.my_orders()

    def test_my_orders(self, mobile_management, static_courier_data):
        with allure.step("Открытие вкладки"):
            mobile_pages.connecting_server()
        with allure.step("Авторизация курьера"):
            mobile_pages.login_courier(static_courier_data)
        with allure.step("Мои заказы"):
            mobile_pages.my_orders()

    def test_logout(self, mobile_management, static_courier_data):
        with allure.step("Открытие вкладки"):
            mobile_pages.connecting_server()
        with allure.step("Авторизация курьера"):
            mobile_pages.login_courier(static_courier_data)
        with allure.step("Выход"):
            mobile_pages.logout()
