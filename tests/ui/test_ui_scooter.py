import allure

from aqa_scooter_rental.pages.ui.faq_page import faq_page
from aqa_scooter_rental.pages.ui.logo_page import logo_page
from test_data.data import QuestionsAndAnswers


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


@allure.suite('Вопросы и ответы в FAQ')
class TestMainPage:

    @allure.title('Проверка выпадающего 1-о списка в разделе "Вопросы о важном"')
    @allure.description('Проверяем, что по клику на стрелочку с вопросом, открывается соответсвующий ответ')
    def test_check_question_and_answer_number_one(self):
        index, question, answer = QuestionsAndAnswers.QUESTIONS_AND_ANSWERS_LIST[0]
        faq_page.open_browser()
        faq_page.scroll_to_faq()
        question_text = faq_page.get_question(index)
        answer_text = faq_page.get_answers(index)

        faq_page.should_text_faq(question_text, question)
        faq_page.should_question_text_faq(answer_text, answer)

    @allure.title('Проверка выпадающего 2-о списка в разделе "Вопросы о важном"')
    @allure.description('Проверяем, что по клику на стрелочку с вопросом, открывается соответсвующий ответ')
    def test_check_question_and_answer_number_two(self):
        index, question, answer = QuestionsAndAnswers.QUESTIONS_AND_ANSWERS_LIST[1]
        faq_page.open_browser()
        faq_page.scroll_to_faq()
        question_text = faq_page.get_question(index)
        answer_text = faq_page.get_answers(index)

        faq_page.should_text_faq(question_text, question)
        faq_page.should_question_text_faq(answer_text, answer)

    @allure.title('Проверка выпадающего 3-о списка в разделе "Вопросы о важном"')
    @allure.description('Проверяем, что по клику на стрелочку с вопросом, открывается соответсвующий ответ')
    def test_check_question_and_answer_number_three(self):
        index, question, answer = QuestionsAndAnswers.QUESTIONS_AND_ANSWERS_LIST[2]
        faq_page.open_browser()
        faq_page.scroll_to_faq()
        question_text = faq_page.get_question(index)
        answer_text = faq_page.get_answers(index)

        faq_page.should_text_faq(question_text, question)
        faq_page.should_question_text_faq(answer_text, answer)

    @allure.title('Проверка выпадающего 4-о списка в разделе "Вопросы о важном"')
    @allure.description('Проверяем, что по клику на стрелочку с вопросом, открывается соответсвующий ответ')
    def test_check_question_and_answer_number_four(self):
        index, question, answer = QuestionsAndAnswers.QUESTIONS_AND_ANSWERS_LIST[3]
        faq_page.open_browser()
        faq_page.scroll_to_faq()
        question_text = faq_page.get_question(index)
        answer_text = faq_page.get_answers(index)

        faq_page.should_text_faq(question_text, question)
        faq_page.should_question_text_faq(answer_text, answer)

    @allure.title('Проверка выпадающего 5-о списка в разделе "Вопросы о важном"')
    @allure.description('Проверяем, что по клику на стрелочку с вопросом, открывается соответсвующий ответ')
    def test_check_question_and_answer_number_five(self):
        index, question, answer = QuestionsAndAnswers.QUESTIONS_AND_ANSWERS_LIST[4]
        faq_page.open_browser()
        faq_page.scroll_to_faq()
        question_text = faq_page.get_question(index)
        answer_text = faq_page.get_answers(index)

        faq_page.should_text_faq(question_text, question)
        faq_page.should_question_text_faq(answer_text, answer)

    @allure.title('Проверка выпадающего 6-о списка в разделе "Вопросы о важном"')
    @allure.description('Проверяем, что по клику на стрелочку с вопросом, открывается соответсвующий ответ')
    def test_check_question_and_answer_number_six(self):
        index, question, answer = QuestionsAndAnswers.QUESTIONS_AND_ANSWERS_LIST[5]
        faq_page.open_browser()
        faq_page.scroll_to_faq()
        question_text = faq_page.get_question(index)
        answer_text = faq_page.get_answers(index)

        faq_page.should_text_faq(question_text, question)
        faq_page.should_question_text_faq(answer_text, answer)

    @allure.title('Проверка выпадающего 7-о списка в разделе "Вопросы о важном"')
    @allure.description('Проверяем, что по клику на стрелочку с вопросом, открывается соответсвующий ответ')
    def test_check_question_and_answer_number_seven(self):
        index, question, answer = QuestionsAndAnswers.QUESTIONS_AND_ANSWERS_LIST[6]
        faq_page.open_browser()
        faq_page.scroll_to_faq()
        question_text = faq_page.get_question(index)
        answer_text = faq_page.get_answers(index)

        faq_page.should_text_faq(question_text, question)
        faq_page.should_question_text_faq(answer_text, answer)

    @allure.title('Проверка выпадающего 8-о списка в разделе "Вопросы о важном"')
    @allure.description('Проверяем, что по клику на стрелочку с вопросом, открывается соответсвующий ответ')
    def test_check_question_and_answer_number_eight(self):
        index, question, answer = QuestionsAndAnswers.QUESTIONS_AND_ANSWERS_LIST[7]
        faq_page.open_browser()
        faq_page.scroll_to_faq()
        question_text = faq_page.get_question(index)
        answer_text = faq_page.get_answers(index)

        faq_page.should_text_faq(question_text, question)
        faq_page.should_question_text_faq(answer_text, answer)
