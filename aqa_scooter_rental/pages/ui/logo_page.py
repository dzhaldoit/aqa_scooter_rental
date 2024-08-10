import allure
from selene import browser, have
from test_data.data import URLs
from aqa_scooter_rental.locators.ui_locators import OrderLocators, LogoLocators


class LogoPage:

    @allure.step("Открытие браузера")
    def open_browser(self):
        browser.open(URLs.MAIN_PAGE_URL)
        return self

    @allure.step("Клик по кнопке Заказать в шапке лендинга")
    def click_order_button(self):
        browser.element(*OrderLocators.ORDER_BUTTON_HEADER).click()
        return self

    @allure.step("Клик по лого 'Самокат'")
    def click_scooter_button(self):
        browser.element(*LogoLocators.SCOOTER_BUTTON).click()
        return self

    @allure.step("Клик по лого 'Дзен'")
    def click_dzen_button(self):
        browser.element(*LogoLocators.YANDEX_BUTTON).click()
        return self

    @allure.step("Переключение вкладки")
    def switching_to_the_tab(self):
        browser.switch_to_tab(1)
        return self

    @allure.step("Проверка URL вкладки 'Дзен'")
    def should_dzen_url(self):
        browser.should(have.url(URLs.DZEN_URL))
        return self

    @allure.step("Проверка URL после клика по логотипу 'Самокат'")
    def should_main_page_url(self):
        browser.should(have.url(URLs.MAIN_PAGE_URL))
        return self


logo_page = LogoPage()
