import allure
import pytest
from selene import be, have

from test_data.data import QuestionsAndAnswers, OrderDataUi
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
        order_page.open_browser()
        getattr(order_page, button_method)()
        order_page.user_rent_order(**data_order)
        order_page.confirmation_window()


@allure.suite('URL логотипа')
class TestURL:
    @allure.title('Проверка URL Логотипа "Самокат"')
    def test_main_page(self):
        logo_page.open_browser()
        logo_page.click_order_button()
        logo_page.click_scooter_button()
        logo_page.should_main_page_url()

    @allure.title('Проверка URL Логотипа "Яндекс"')
    def test_dzen_url(self):
        logo_page.open_browser()
        logo_page.click_dzen_button()
        logo_page.switching_to_the_tab()
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

        question_text.should(be.equal_to(question))
        answer_text.should(be.equal_to(answer))
