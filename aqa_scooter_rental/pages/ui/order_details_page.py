import allure
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from aqa_scooter_rental.locators.ui_locators import OrderLocators
from data import URLs
from selenium.webdriver.common.keys import Keys
from tests.conftest import browser


class OrderPage:

    @allure.step("Открытие браузера")
    def open_browser(self, browser):
        browser.get(URLs.MAIN_PAGE_URL)
        return self

    @allure.step("Клик по кнопке Заказать в шапке лендинга")
    def click_first_button(self, browser):
        browser.find_element(*OrderLocators.ORDER_BUTTON_HEADER).click()
        return self

    @allure.step("Клик по кнопке Заказать в центре")
    def click_second_button(self, browser):
        element = browser.find_element(*OrderLocators.ORDER_CENTER_BUTTON)
        browser.execute_script("arguments[0].scrollIntoView(true);", element)
        try:
            WebDriverWait(browser, 10).until(
                EC.element_to_be_clickable(element)
            )
            element.click()
        except TimeoutException:
            print("Timeout: Element not clickable")
        return self

    @allure.step("Заполнение поля Имя")
    def user_name(self, browser, name):
        browser.find_element(*OrderLocators.NAME).send_keys(name)
        return self

    @allure.step("Заполнение поля Фамилия")
    def user_last_name(self, browser, last_name):
        browser.find_element(*OrderLocators.LAST_NAME).send_keys(last_name)
        return self

    @allure.step("Заполнение поля Адрес")
    def user_address(self, browser, address):
        browser.find_element(*OrderLocators.ADDRESS).send_keys(address)
        return self

    @allure.step("Заполнение поля Метро")
    def metro(self, browser, metro):
        browser.find_element(*OrderLocators.METRO).send_keys(metro)
        browser.find_element(*OrderLocators.LIST_STATION).click()
        return self

    @allure.step("Заполнение поля Телефон")
    def user_phone(self, browser, phone):
        browser.find_element(*OrderLocators.NUMBER).send_keys(phone)
        return self

    @allure.step('Клик по кнопке "Далее" в форме информации о пользователе')
    def click_button_next(self, browser):
        browser.find_element(*OrderLocators.NEXT_BUTTON).click()
        return self

    @allure.step("Заполнение поля Дата доставки")
    def date_of_delivery(self, browser, data):
        (browser.find_element(*OrderLocators.DATE_DELIVERY)
         .send_keys(data, Keys.ENTER))
        return self

    @allure.step("Заполнение поля Время аренды")
    def rental_time(self, browser, day):
        browser.find_element(*OrderLocators.RENT_TIME).click()
        select_rent_time_locator = (OrderLocators.SELECT_RENT_TIME[0], OrderLocators.SELECT_RENT_TIME[1].format(day))
        browser.find_element(*select_rent_time_locator).click()
        return self

    @allure.step("Выбор цвета")
    def checkbox_color(self, browser, color):
        if color == 'чёрный жемчуг':
            browser.find_element(*OrderLocators.BLACK_COLOR_CHECKBOX).click()
        elif color == 'серая безысходность':
            browser.find_element(*OrderLocators.GREY_COLOR_CHECKBOX).click()
        return self

    @allure.step("Заполнение поля Комментарии к заказу")
    def comment_for_courier(self, browser, comment):
        browser.find_element(*OrderLocators.COMMENT).send_keys(comment)
        return self

    @allure.step("Клик по кнопке Заказать")
    def click_button_order(self, browser):
        browser.find_element(*OrderLocators.ORDER_BUTTON).click()
        return self

    @allure.step("Клик по кнопке 'Да' в окне подтверждения заказа")
    def click_button_confirmations(self, browser):
        browser.find_element(*OrderLocators.YES_BUTTON).click()
        return self

    @allure.step("Проверка текста в окне подтверждения заказа")
    def confirmation_window(self, browser):
        text = browser.find_element(*OrderLocators.ORDER_COMPLETED).text
        assert 'Заказ оформлен' in text
        return self

    @allure.step("Полный позитивный сценарий")
    def user_rent_order(self,
                        browser, name, last_name, address, metro, number,
                        delivery_date, rent_days, colour, comment):
        self.user_name(browser, name)
        self.user_last_name(browser, last_name)
        self.user_address(browser, address)
        self.metro(browser, metro)
        self.user_phone(browser, number)
        self.click_button_next(browser)
        self.date_of_delivery(browser, delivery_date)
        self.rental_time(browser, rent_days)
        self.checkbox_color(browser, colour)
        self.comment_for_courier(browser, comment)
        self.click_button_order(browser)
        self.click_button_confirmations(browser)
        self.confirmation_window(browser)
        return self


order_page = OrderPage()

