from selene import browser
from aqa_scooter_rental.locators.mobile_locators import LogInLocators, ListOrdersLocators
import data
from tests.mobile.conftest import static_courier_data


class MobilePages:
    def connecting_server(self):
        browser.element(LogInLocators.BUTTON_STAND).click()
        browser.element(LogInLocators.BACKEND_URL).send_keys(data.URLs.MAIN_PAGE_URL)
        browser.element(LogInLocators.OK_BUTTON).click()
        return self

    def login_courier(self, static_courier_data):
        browser.element(LogInLocators.LOGIN).type(static_courier_data["login"])
        browser.element(LogInLocators.PASSWORD).type(static_courier_data["password"])
        browser.element(LogInLocators.LOGIN_BUTTON).click()
        return self

    def my_orders(self):
        browser.element(ListOrdersLocators.MY_BUTTON_ORDER).click()
        return self

    def logout(self):
        browser.element(ListOrdersLocators.LOG_OUT_BUTTON).click()
        browser.element(ListOrdersLocators.CONFIRM_LOG_OUT).click()
        return self


mobile_pages = MobilePages()
