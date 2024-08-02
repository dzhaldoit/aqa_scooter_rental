import allure
import requests
from selene import browser

from aqa_scooter_rental.locators.mobile_locators import LogInLocators, ListOrdersLocators
import data
from tests.conftest import currier_data
from data import URLs


class TestMobileApi:
    @allure.title('Создаем курьера/авторизуемся/получаем заказ')
    def test_login_courier_successful(self, currier_data):
        # Создаем курьера
        requests.post(data.URLs.create_courier, data=currier_data)

        # Создаем и получаем трек номер заказа
        payload = data.OrderData.order_data
        id_order = requests.post(data.URLs.creating_order, data=payload)
        id_order = id_order.json()["track"]

        # Получаем id заказа
        get_order = requests.get(data.URLs.order_get_number + str(id_order))
        get_order = get_order.json()["order"]["id"]
        print(get_order)

        # Получаем идентификатор курьера
        response_id = requests.post(data.URLs.login_courier, data=currier_data)
        response_id = response_id.json()["id"]
        print(response_id)

        get_courier = f'{URLs.MAIN_PAGE_URL}api/v1/orders/accept/{get_order}?courierId={response_id}'
        print(requests.put(get_courier).json())

        return self


class TestMobilePages:

    def login_courier(self, currier_data):
        browser.element(LogInLocators.LOGIN).type(
            TestMobileApi.test_login_courier_successful.currier_data["firstName"])
        browser.element(LogInLocators.PASSWORD).type(
            TestMobileApi.test_login_courier_successful.currier_data["password"])
        browser.element(LogInLocators.LOGIN_BUTTON).click()
        return self


    def connecting_server(self):
        browser.element(LogInLocators.BUTTON_STAND).click()
        browser.element(LogInLocators.BACKEND_URL).send_keys(data.URLs.MAIN_PAGE_URL)
        browser.element(LogInLocators.OK_BUTTON).click()
        return self

    def confirm_order(self):
        browser.element(ListOrdersLocators.COMPLETED_ORDERS_BUTTON).click()
        browser.element(ListOrdersLocators.COMPLETED_ORDERS_ANSWER).click()
        browser.element(ListOrdersLocators.TEXT_COMPLETED_ORDERS).click()
        browser.element(ListOrdersLocators.TEXT_COMPLETED_ORDERS2).click()
        browser.element(ListOrdersLocators.COMPLETED_ORDERS_BUTTON2).click()
        return self

    def completed_orders(self):
        browser.element(ListOrdersLocators.COMPLETED_ORDERS_BUTTON).click()
        browser.element(ListOrdersLocators.COMPLETED_ORDERS_ANSWER).click()
        browser.element(ListOrdersLocators.TEXT_COMPLETED_ORDERS).click()
        browser.element(ListOrdersLocators.TEXT_COMPLETED_ORDERS2).click()
        browser.element(ListOrdersLocators.COMPLETED_ORDERS_BUTTON2).click()
        return self

    def logout(self):
        browser.element(ListOrdersLocators.LOG_OUT_BUTTON).click()
        browser.element(ListOrdersLocators.CONFIRM_LOG_OUT).click()
        browser.element(ListOrdersLocators.LOG_OUT_CONFIRM).click()
        return self
