import allure
import requests
from selene import browser, be

from aqa_scooter_rental.locators.mobile_locators import LogInLocators, ListOrdersLocators
import data
from tests.api_tests.conftest import currier_data
from data import URLs


class ApiReceivingOrderPages:
    @allure.title('Создаем курьера/авторизуемся/получаем заказ')
    def order_take_successful(self, currier_data):
        # Создаем курьера
        requests.post(data.URLs.create_courier, data=currier_data)
        print(currier_data["login"])
        print(currier_data["password"])

        # Создаем и получаем трек номер заказа
        payload = data.OrderData.order_data
        id_order = requests.post(data.URLs.creating_order, data=payload)
        id_order = id_order.json()["track"]

        # Получаем id заказа
        get_order = requests.get(data.URLs.order_get_number + str(id_order))
        get_order = get_order.json()["order"]["id"]

        # Получаем идентификатор курьера
        response_id = requests.post(data.URLs.login_courier, data=currier_data)
        response_id = response_id.json()["id"]

        # Принимаем заказ
        get_courier = f'{URLs.MAIN_PAGE_URL}api/v1/orders/accept/{get_order}?courierId={response_id}'
        requests.put(get_courier)
        return self


class MobilePages:
    def connecting_server(self):
        browser.element(LogInLocators.BUTTON_STAND).click()
        browser.element(LogInLocators.BACKEND_URL).send_keys(data.URLs.MAIN_PAGE_URL)
        browser.element(LogInLocators.OK_BUTTON).click()
        return self

    def test_login_courier(self, currier_data):
        browser.element(LogInLocators.LOGIN).type(
            ApiReceivingOrderPages.order_take_successful.currier_data["login"])
        browser.element(LogInLocators.PASSWORD).type(
            ApiReceivingOrderPages.order_take_successful.currier_data["password"])
        browser.element(LogInLocators.LOGIN_BUTTON).click()
        return self

    def completed_orders(self):
        browser.element(ListOrdersLocators.MY_ORDERS_BUTTON).click()
        browser.element(ListOrdersLocators.COMPLETED_ORDERS_BUTTON).click()
        browser.element(ListOrdersLocators.COMPLETED_ORDERS_ANSWER).should(be.visible).click()
        browser.element(ListOrdersLocators.COMPLETED_ORDERS_BUTTON).click()
        browser.element(ListOrdersLocators.COMPLETED_ORDERS_ANSWER).should(be.visible).click()

        return self

    def logout(self):
        browser.element(ListOrdersLocators.LOG_OUT_BUTTON).click()
        browser.element(ListOrdersLocators.CONFIRM_LOG_OUT).click()
        browser.element(ListOrdersLocators.LOG_OUT_CONFIRM).have.text('Войти')
        return self


api_pages = ApiReceivingOrderPages()
mobile_pages = MobilePages()

