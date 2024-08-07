from appium.webdriver.common.appiumby import AppiumBy


class ListOrdersLocators:
    MY_BUTTON_ORDER = AppiumBy.ID, 'com.yandex.samokat:id/tab_mine'
    LOG_OUT_BUTTON = AppiumBy.ID, 'com.yandex.samokat:id/logout_button'
    CONFIRM_LOG_OUT = AppiumBy.ID, 'com.yandex.samokat:id/dialog_button_yes'


class LogInLocators:
    LOGIN = AppiumBy.ID, "com.yandex.samokat:id/auth_login_input"
    PASSWORD = AppiumBy.ID, "com.yandex.samokat:id/auth_password_input"
    LOGIN_BUTTON = AppiumBy.ID, "com.yandex.samokat:id/auth_login_button"

    BUTTON_STAND = AppiumBy.ID, "com.yandex.samokat:id/show_back"
    BACKEND_URL = AppiumBy.ID, "com.yandex.samokat:id/url_edit"
    OK_BUTTON = AppiumBy.ID, 'com.yandex.samokat:id/ok_button'
