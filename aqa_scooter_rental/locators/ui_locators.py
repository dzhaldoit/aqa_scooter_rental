from selenium.webdriver.common.by import By


class FaqLocators:
    QUESTION = [By.XPATH, "(.//div[@class='accordion__button'])[{}]"]
    ANSWER = [By.XPATH, "(.//div[@class='accordion__panel'])[{}]"]


class OrderLocators:

    # Кнопка "Заказать"
    ORDER_BUTTON_HEADER = [By.XPATH, "//button[text()='Заказать']"]
    ORDER_CENTER_BUTTON = [By.XPATH, '(//button[text()="Заказать"])[2]']

    # Данные пользователя
    NAME = [By.XPATH, "//input[@placeholder='* Имя']"]
    LAST_NAME = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    ADDRESS = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    METRO = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    LIST_STATION = [By.XPATH, "//li[@data-index='0']"]
    NUMBER = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    NEXT_BUTTON = [By.XPATH, ".//button[text()='Далее']"]

    # Окно Про аренду
    DATE_DELIVERY = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    RENT_TIME = [By.XPATH, '//div[text()="* Срок аренды"]']
    SELECT_RENT_TIME = [By.XPATH, '//div[text()="{}"]']
    BLACK_COLOR_CHECKBOX = [By.XPATH, '//label[@for="black"]']
    GREY_COLOR_CHECKBOX = [By.XPATH, '//label[@for="grey"]']
    COMMENT = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]
    ORDER_BUTTON = [By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]']

    # Кнопка Да в сплывающем окне заказа подтверждения
    YES_BUTTON = [By.XPATH, ".//button[text()='Да']"]

    # Текс окна "Заказ оформлен"
    ORDER_COMPLETED = [By.XPATH, '//div[contains(text(), "Заказ оформлен")]']


class LogoLocators:
    # Логотип шапки "Яндекс Самокат"
    SCOOTER_BUTTON = [By.XPATH, ".//a[@href='/']"]
    YANDEX_BUTTON = [By.XPATH, ".//a[@href='//yandex.ru']"]
