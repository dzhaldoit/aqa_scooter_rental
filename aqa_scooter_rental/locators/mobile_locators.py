from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By


class ListOrdersLocators:
    ORDER_LIST_PAGE = [AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.yandex.samokat:id/textView']"]
    ADDRESS_ORDER = [AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.yandex.samokat:id/address_input']"]

    SUBMIT_BUTTON_ORDER = [AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.yandex.samokat:id/accept"]']
    CONFIRM_BUTTON_ORDER = [AppiumBy.XPATH, '//android.widget.Button[@resource-id='
                                            '"com.yandex.samokat:id/dialog_button_yes"]']

    SHOULD_BE_ORDER = [AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.yandex.samokat:id/textView2"]']
    MY_ORDERS_BUTTON = [AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.yandex.samokat:id/tab_mine"]']

    COMPLETED_ORDERS_BUTTON = [AppiumBy.XPATH, ('//android.widget.Button[@resource-id="com.yandex.samokat:'
                                                'id/accept"]')[1]]
    COMPLETED_ORDERS_ANSWER = [AppiumBy.XPATH, '//android.widget.Button[@resource-id='
                                               '"com.yandex.samokat:id/dialog_button_yes"']
    TEXT_COMPLETED_ORDERS = [AppiumBy.XPATH, ('//android.widget.Button[@resource-id='
                                              '"com.yandex.samokat:id/accept"]')[1]]
    TEXT_COMPLETED_ORDERS2 = [AppiumBy.XPATH, ('//android.widget.Button[@resource-id='
                                               '"com.yandex.samokat:id/accept"]')[2]]
    COMPLETED_ORDERS_BUTTON2 = [AppiumBy.XPATH, ('//android.widget.Button[@resource-id='
                                                 '"com.yandex.samokat:id/accept"]')[2]]

    LOG_OUT_BUTTON = [AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="com.yandex.samokat:id/logout_button"]']
    CONFIRM_LOG_OUT = [AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.yandex.samokat:id/dialog_button_yes"]']

    LOG_OUT_CONFIRM = [AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="com.yandex.samokat:id/auth_subtitle"]']


class LogInLocators:
    LOGIN = [AppiumBy.XPATH, "//android.widget.EditText[@resource-id='com.yandex.samokat:id/auth_login_input']"]
    PASSWORD = [AppiumBy.XPATH, "//android.widget.EditText[@resource-id='com.yandex.samokat:id/auth_password_input']"]
    LOGIN_BUTTON = [AppiumBy.XPATH, "//android.widget.Button[@resource-id='com.yandex.samokat:id/auth_login_button']"]

    BUTTON_STAND = [AppiumBy.XPATH, "//android.widget.ImageView[@resource-id='com.yandex.samokat:id/show_back']"]
    BACKEND_URL = [AppiumBy.XPATH, "//android.widget.EditText[@resource-id='com.yandex.samokat:id/url_edit']"]
    OK_BUTTON = [AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.yandex.samokat:id/ok_button"]']
    TEXT_LOGIN = [AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.yandex.samokat:id/textView"]']
