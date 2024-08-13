from appium.webdriver.common.appiumby import AppiumBy
from selene import browser

from test_data import data
from tests.mobile.conftest import static_courier_data


class MobilePages:

    def __init__(self):
        self.LOG_OUT_BUTTON = AppiumBy.ID, 'com.yandex.samokat:id/logout_button'
        self.CONFIRM_LOG_OUT = AppiumBy.ID, 'com.yandex.samokat:id/dialog_button_yes'
        self.LOGIN = AppiumBy.ID, "com.yandex.samokat:id/auth_login_input"
        self.PASSWORD = AppiumBy.ID, "com.yandex.samokat:id/auth_password_input"
        self.LOGIN_BUTTON = AppiumBy.ID, "com.yandex.samokat:id/auth_login_button"
        self.BUTTON_STAND = AppiumBy.ID, "com.yandex.samokat:id/show_back"
        self.BACKEND_URL = AppiumBy.ID, "com.yandex.samokat:id/url_edit"
        self.OK_BUTTON = AppiumBy.ID, 'com.yandex.samokat:id/ok_button'

    def connecting_server(self):
        browser.element(self.BUTTON_STAND).click()
        browser.element(self.BACKEND_URL).send_keys(data.URLs.MAIN_PAGE_URL)
        browser.element(self.OK_BUTTON).click()
        return self

    def login_courier(self, static_courier_data):
        browser.element(self.LOGIN).type(static_courier_data["login"])
        browser.element(self.PASSWORD).type(static_courier_data["password"])
        browser.element(self.LOGIN_BUTTON).click()
        return self

    def logout(self):
        browser.element(self.LOG_OUT_BUTTON).click()
        browser.element(self.CONFIRM_LOG_OUT).click()
        return self


mobile_pages = MobilePages()
