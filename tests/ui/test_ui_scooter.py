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
    def test_make_an_order(self, data_order, button_method):
        # Открытие браузера
        order_page.open_browser()
        # Клик по кнопке "Заказать" в шапке лендинга и в центре лендинга через параметр button_method
        getattr(order_page, button_method)()
        # Заполнение полей для заказа, через параметр data_order
        order_page.user_rent_order(**data_order)
        # Проверка окна подтверждения по тексту "Заказ оформлен
        order_page.confirmation_window()


@allure.suite('URL логотипа')
class TestURL:
    @allure.title('Проверка URL Логотипа "Самокат"')
    def test_main_page(self):
        # Открытие браузера
        logo_page.open_browser()
        # Клик по кнопке "Заказать" в шапке лендинга
        logo_page.click_order_button()
        # Клик по логотипу "Самокат"
        logo_page.click_scooter_button()
        # Проверка URL Логотипа "Самокат"
        logo_page.should_main_page_url()

    @allure.title('Проверка URL Логотипа "Яндекс"')
    def test_dzen_url(self):
        # Открытие браузера
        logo_page.open_browser()
        # Клик по кнопке "Заказать" в шапке лендинга
        logo_page.click_dzen_button()
        # Переключение в новую вкладку
        logo_page.switching_to_the_tab()
        # Проверка URL Логотипа "Самокат"
        logo_page.should_dzen_url()


@allure.suite('Вопросы в FAQ')
class TestMainPage:
    @allure.title('Проверка выпадающего списка в разделе "Вопросы о важном"')
    @allure.description('Проверяем, что по клику на стрелочку с вопросом, открывается соответсвующий ответ')
    @pytest.mark.parametrize('index, question, answer', QuestionsAndAnswers.QUESTIONS_AND_ANSWERS_LIST)
    def test_check_question_and_answer(self, index, question, answer):
        faq_page.open_browser()
        faq_page.scroll_to_faq()
        question_text = faq_page.get_question(index)
        answer_text = faq_page.get_answers(index)
        # Проверяем, что текст вопроса соответствует ожидаемому
        assert question_text == question
        # Проверяем, что текст ответа соответствует ожидаемому
        assert answer_text == answer
