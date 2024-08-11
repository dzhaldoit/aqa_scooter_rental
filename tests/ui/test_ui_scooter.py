import allure
import pytest

from test_data.data import QuestionsAndAnswers, OrderDataUi
from aqa_scooter_rental.pages.ui.faq_page import faq_page
from aqa_scooter_rental.pages.ui.order_details_page import order_page
from aqa_scooter_rental.pages.ui.logo_page import logo_page


@allure.suite('Позитивный сценарий')
class TestOrderPage:
    @allure.title('Проверка позитивного сценария заказа самоката с первым набором данных')
    @allure.description('Проверяем флоу позитивного сценария с первым набором данных')
    def test_make_an_order_with_first_data(self):
        order_page.open_browser()
        order_page.click_second_button()
        order_page.user_rent_order(**OrderDataUi.FIRST_ORDER)
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

        faq_page.should_text_faq(question_text, question)
        faq_page.should_question_text_faq(answer_text, answer)
