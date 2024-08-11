import allure
from selene import command, be
from selene.core.query import text_content
from selenium.webdriver.common.keys import Keys
from aqa_scooter_rental.locators.ui_locators import OrderLocators
from tests.ui.conftest import browser


class OrderPage:

    @allure.step("Открытие браузера")
    def open_browser(self):
        browser.open("/")
        return self

    @allure.step("Клик по кнопке Заказать в шапке лендинга")
    def click_first_button(self):
        browser.element(*OrderLocators.ORDER_BUTTON_HEADER).click()
        return self

    @allure.step("Клик по кнопке Заказать в центре")
    def click_second_button(self):
        element = browser.element(*OrderLocators.ORDER_CENTER_BUTTON)
        element.perform(command.js.scroll_into_view)
        element.click()

        return self

    @allure.step("Заполнение поля Имя")
    def user_name(self, name):
        browser.element(*OrderLocators.TEXT_WINDOW).should(be.visible)
        browser.element(*OrderLocators.NAME).send_keys(name)
        return self

    @allure.step("Заполнение поля Фамилия")
    def user_last_name(self, last_name):
        browser.element(*OrderLocators.LAST_NAME).send_keys(last_name)
        return self

    @allure.step("Заполнение поля Адрес")
    def user_address(self, address):
        browser.element(*OrderLocators.ADDRESS).type(address)
        return self

    @allure.step("Заполнение поля Метро")
    def metro(self, metro):
        browser.element(*OrderLocators.METRO).should(be.visible)
        browser.element(*OrderLocators.METRO).type(metro)
        browser.element(*OrderLocators.LIST_STATION).should(be.clickable).click()
        return self

    @allure.step("Заполнение поля Телефон")
    def user_phone(self, phone):
        browser.element(*OrderLocators.NUMBER).send_keys(phone)
        return self

    @allure.step('Клик по кнопке "Далее" в форме информации о пользователе')
    def click_button_next(self):
        browser.element(*OrderLocators.NEXT_BUTTON).click()
        return self

    @allure.step("Заполнение поля Дата доставки")
    def date_of_delivery(self, data):
        browser.element(*OrderLocators.TEXT_RENT).should(be.visible)
        (browser.element(*OrderLocators.DATE_DELIVERY)
         .send_keys(data, Keys.ENTER))
        return self

    @allure.step("Заполнение поля Время аренды")
    def rental_time(self, day):
        browser.element(*OrderLocators.RENT_TIME).click()
        select_rent_time_locator = (OrderLocators.SELECT_RENT_TIME[0].format(day),)
        browser.element(*select_rent_time_locator).click()
        return self

    @allure.step("Выбор цвета")
    def checkbox_color(self, color):
        if color == 'чёрный жемчуг':
            browser.element(*OrderLocators.BLACK_COLOR_CHECKBOX).click()
        elif color == 'серая безысходность':
            browser.element(*OrderLocators.GREY_COLOR_CHECKBOX).click()
        return self

    @allure.step("Заполнение поля Комментарии к заказу")
    def comment_for_courier(self, comment):
        browser.element(*OrderLocators.COMMENT).send_keys(comment)
        return self

    @allure.step("Клик по кнопке Заказать")
    def click_button_order(self):
        browser.element(*OrderLocators.ORDER_BUTTON).click()
        return self

    @allure.step("Клик по кнопке 'Да' в окне подтверждения заказа")
    def click_button_confirmations(self):
        browser.element(*OrderLocators.YES_BUTTON).click()
        return self

    @allure.step("Проверка текста в окне подтверждения заказа")
    def confirmation_window(self):
        text = browser.element(*OrderLocators.ORDER_COMPLETED).get(query=text_content)
        assert 'Заказ оформлен' in text
        return self

    @allure.step("Полный позитивный сценарий")
    def user_rent_order(self,
                        name, last_name, address, metro, number,
                        delivery_date, rent_days, colour, comment):
        self.user_name(name)
        self.user_last_name(last_name)
        self.user_address(address)
        self.metro(metro)
        self.user_phone(number)
        self.click_button_next()
        self.date_of_delivery(delivery_date)
        self.rental_time(rent_days)
        self.checkbox_color(colour)
        self.comment_for_courier(comment)
        self.click_button_order()
        self.click_button_confirmations()
        self.confirmation_window()
        return self


order_page = OrderPage()
