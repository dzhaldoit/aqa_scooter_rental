import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from data import URLs
from tests.conftest import browser
from aqa_scooter_rental.locators.ui_locators import FaqLocators


class QuestionsPage:
    @allure.step("Открытие браузера")
    def open_browser(self, browser):
        browser.get(URLs.MAIN_PAGE_URL)
        return self

    @allure.step("Скролл к вопросам")
    def scroll_to_faq(self, browser):
        element = browser.find_element(By.CLASS_NAME, "accordion")
        browser.execute_script("arguments[0].scrollIntoView(true);", element)
        return self

    @allure.step("Извлечение вопроса")
    def get_question(self, browser, index):
        question_locator = (FaqLocators.QUESTION[0], FaqLocators.QUESTION[1].format(index))
        question = WebDriverWait(browser, 3).until(ec.element_to_be_clickable(question_locator))
        question.click()
        return question.text

    @allure.step("Извлечение ответа")
    def get_answers(self, browser, index):
        answers_locator = (FaqLocators.ANSWER[0], FaqLocators.ANSWER[1].format(index))
        answers = browser.find_element(*answers_locator)
        return answers.text


faq_page = QuestionsPage()



