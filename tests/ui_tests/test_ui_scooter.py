import allure
import pytest

from data import QuestionsAndAnswers, OrderDataUi
from aqa_scooter_rental.pages.ui.faq_page import faq_page
from aqa_scooter_rental.pages.ui.order_details_page import order_page
from aqa_scooter_rental.pages.ui.logo_page import logo_page


@allure.suite('Позитивный сценарий')
class TestOrderPage:
    @allure.title('Проверка позитивного сценария заказа самоката')
    @allure.description('Проверяем весь флоу позитивного сценария с двумя наборами данных')
    @pytest.mark.parametrize('button_method, data_order', [('click_first_button', OrderDataUi.FIRST_ORDER),
                                                           ('click_second_button', OrderDataUi.SECOND_ORDER)])
    def test_make_an_order(self, browser, data_order, button_method):
        # Открытие браузера
        order_page.open_browser(browser)
        # Клик по кнопке "Заказать" в шапке лендинга и в центре лендинга через параметр button_method
        getattr(order_page, button_method)(browser)
        # Заполнение полей для заказа, через параметр data_order
        order_page.user_rent_order(browser, **data_order)
        # Проверка окна подтверждения по тексту "Заказ оформлен
        order_page.confirmation_window(browser)


class TestURL:
    @allure.title('Проверка URL Логотипа "Самокат"')
    def test_main_page(self, browser):
        # Открытие браузера
        logo_page.open_browser(browser)
        # Клик по кнопке "Заказать" в шапке лендинга
        logo_page.click_order_button(browser)
        # Клик по логотипу "Самокат"
        logo_page.click_scooter_button(browser)
        # Проверка URL Логотипа "Самокат"
        logo_page.should_main_page_url(browser)

    @allure.title('Проверка URL Логотипа "Яндекс"')
    def test_dzen_url(self, browser):
        # Открытие браузера
        logo_page.open_browser(browser)
        # Клик по кнопке "Заказать" в шапке лендинга
        logo_page.click_dzen_button(browser)
        # Переключение в новую вкладку
        logo_page.switching_to_the_tab(browser)
        # Ожидаем загрузки страницы Дзен
        logo_page.wait_for_page_load(browser)
        # Проверка URL Логотипа "Самокат"
        logo_page.should_dzen_url(browser)


class TestMainPage:
    @allure.title('Проверка выпадающего списка в разделе "Вопросы о важном"')
    @allure.description('Проверяем, что по клику на стрелочку с вопросом, открывается соответсвующий ответ')
    @pytest.mark.parametrize('index, question, answer', QuestionsAndAnswers.QUESTIONS_AND_ANSWERS_LIST)
    def test_check_question_and_answer(self, browser, index, question, answer):
        faq_page.open_browser(browser)
        faq_page.scroll_to_faq(browser)
        question_text = faq_page.get_question(browser, index)
        answer_text = faq_page.get_answers(browser, index)
        # Проверяем, что текст вопроса соответствует ожидаемому
        assert question_text == question
        # Проверяем, что текст ответа соответствует ожидаемому
        assert answer_text == answer


