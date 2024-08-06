import allure
from selene import browser, command
from selene.core.query import text_content
from data import URLs
from aqa_scooter_rental.locators.ui_locators import FaqLocators


class QuestionsPage:
    @allure.step("Открытие браузера")
    def open_browser(self):
        browser.open(URLs.MAIN_PAGE_URL)
        return self

    @allure.step("Скролл к вопросам")
    def scroll_to_faq(self):
        browser.element('.accordion').perform(command.js.scroll_into_view)
        return self

    @allure.step("Извлечение вопроса")
    def get_question(self, index):
        question_locator = FaqLocators.QUESTION[0].format(index)
        question = browser.element(question_locator)
        question.click()
        return question.get(query=text_content)

    @allure.step("Извлечение ответа")
    def get_answers(self, index):
        answers_locator = FaqLocators.ANSWER[0].format(index)
        answers = browser.element(answers_locator)
        return answers.get(query=text_content)


faq_page = QuestionsPage()


