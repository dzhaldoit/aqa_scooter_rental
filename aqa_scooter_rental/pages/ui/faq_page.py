import allure
from selene import browser, command
from selene.core.query import text_content


class QuestionsPage:
    @allure.step("Открытие браузера")
    def open_browser(self):
        browser.open("/")
        return self

    @allure.step("Скролл к вопросам")
    def scroll_to_faq(self):
        browser.element(".accordion").perform(command.js.scroll_into_view)
        return self

    @allure.step("Извлечение вопроса")
    def get_question(self, index):
        question_locator = '#accordion__heading-{}'.format(index)
        question = browser.element(question_locator)
        question.click()
        return question.get(query=text_content)

    @allure.step("Извлечение ответа")
    def get_answers(self, index):
        answers_locator = '#accordion__panel-{}'.format(index)
        answers = browser.element(answers_locator)
        return answers.get(query=text_content)

    @allure.step("Проверка совпадения текста ответа")
    def should_question_text_faq(self, question_text, question):
        assert question_text == question
        return

    @allure.step("Проверка совпадения теста и вопроса")
    def should_text_faq(self, answer_text, answer):
        assert answer_text == answer
        return


faq_page = QuestionsPage()
