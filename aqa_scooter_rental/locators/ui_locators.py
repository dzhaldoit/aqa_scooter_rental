
class FaqLocators:
    QUESTION = ["(.//div[@class='accordion__button'])[{}]"]
    ANSWER = ["(.//div[@class='accordion__panel'])[{}]"]


class OrderLocators:

    # Кнопка "Заказать"
    ORDER_BUTTON_HEADER = ["//button[text()='Заказать']"]
    ORDER_CENTER_BUTTON = ['(//button[text()="Заказать"])[2]']

    # Данные пользователя
    TEXT_WINDOW = ['//div[text()="Для кого самокат"]']
    NAME = ["//input[@placeholder='* Имя']"]
    LAST_NAME = ["//input[@placeholder='* Фамилия']"]
    ADDRESS = ["//input[@placeholder='* Адрес: куда привезти заказ']"]
    METRO = ["//input[@placeholder='* Станция метро']"]
    LIST_STATION = ["//li[@data-index='0']"]
    NUMBER = ["//input[@placeholder='* Телефон: на него позвонит курьер']"]
    NEXT_BUTTON = [".//button[text()='Далее']"]

    # Окно Про аренду
    TEXT_RENT = ['//div[text()="Про аренду"]']
    DATE_DELIVERY = ["//input[@placeholder='* Когда привезти самокат']"]
    RENT_TIME = ['//div[text()="* Срок аренды"]']
    SELECT_RENT_TIME = ['//div[text()="{}"]']
    BLACK_COLOR_CHECKBOX = ['//label[@for="black"]']
    GREY_COLOR_CHECKBOX = ['//label[@for="grey"]']
    COMMENT = ["//input[@placeholder='Комментарий для курьера']"]
    ORDER_BUTTON = ['//div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]']

    # Кнопка Да в сплывающем окне заказа подтверждения
    YES_BUTTON = [".//button[text()='Да']"]

    # Текс окна "Заказ оформлен"
    ORDER_COMPLETED = ['//div[contains(text(), "Заказ оформлен")]']


class LogoLocators:
    # Логотип шапки "Яндекс Самокат"
    SCOOTER_BUTTON = [".//a[@href='/']"]
    YANDEX_BUTTON = [".//a[@href='//yandex.ru']"]
