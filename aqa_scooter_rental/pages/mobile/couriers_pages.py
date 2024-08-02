import requests
from selene import browser, be

from aqa_scooter_rental.locators.mobile_locators import LogInLocators, ListOrdersLocators
import data
from tests.conftest import currier_data_without_firstname


class TestMobilePages:

    def test_login_courier_successful(self, currier_data_without_firstname):
        requests.post(data.URLs.create_courier, data=currier_data_without_firstname)
        response_login = requests.post(data.URLs.login_courier, data=currier_data_without_firstname)
        print(response_login.json())


    def accept_orders(self):
        browser.element(ListOrdersLocators.ACCEPT_ORDERS_BUTTON).click()
        return self

    def connecting_server(self):
        browser.element(LogInLocators.BUTTON_STAND).click()
        browser.element(LogInLocators.BACKEND_URL).send_keys(data.URLs.MAIN_PAGE_URL)
        browser.element(LogInLocators.OK_BUTTON).click()
        return self

    def courier_login(self):
        browser.element(LogInLocators.LOGIN).send_keys()
        browser.element(LogInLocators.PASSWORD).send_keys()
        browser.element(LogInLocators.LOGIN_BUTTON).click()

        browser.element(LogInLocators.TEXT_LOGIN).should(be.visible)
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
