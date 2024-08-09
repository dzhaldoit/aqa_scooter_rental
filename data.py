import datetime


class URLs:
    MAIN_PAGE_URL = 'https://qa-scooter.praktikum-services.ru/'
    DZEN_URL = 'https://dzen.ru/?yredirect=true'

    # POST Orders - Создание заказа
    creating_order = f'{MAIN_PAGE_URL}api/v1/orders'

    # GET Orders - Получить заказ по его номеру
    order_get_number = f'{MAIN_PAGE_URL}api/v1/orders/track?t='

    # PUT Orders - Принять заказ
    order_accept = f'{MAIN_PAGE_URL}api/v1/orders/accept'

    # GET Orders - Получение списка заказов courierId
    get_list_orders = f'{MAIN_PAGE_URL}api/v1/orders?courierId='

    # POST Courier - Создание курьера
    create_courier = f'{MAIN_PAGE_URL}api/v1/courier'

    # POST Courier - Логин курьера в системе
    login_courier = f'{MAIN_PAGE_URL}api/v1/courier/login'

    # DELETE Courier - Удаление курьера
    delete_courier = f'{MAIN_PAGE_URL}api/v1/courier/'


class OrderData:

    order_data = {
        "firstName": "Наруто",
        "lastName": "Удзумаки",
        "address": "Каноха",
        "metroStation": "9",
        "phone": "+7 999 999 99 99",
        "rentTime": 5,
        "deliveryDate": datetime.date.today().day,
        "comment": "Не звонить!",
        "color": []
        }

    color_scooter = [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ]


class Response:
    response_account_not_found = 'Учетная запись не найдена'
    response_no_data_input = "Недостаточно данных для входа"
    response_no_data_account = 'Недостаточно данных для создания учетной записи'
    response_login_used = 'Этот логин уже используется. Попробуйте другой.'
    response_registration_successful = '{"ok":true}'


class LimitPageOrders:
    limit_page_orders = {
        "limit": "5",
        "page": "0"
    }


class OrderDataUi:
    # Данные для заказа самоката
    FIRST_ORDER = {
        'name': 'Михаил',
        'last_name': 'Зубенко',
        'address': 'Мафиозникого 2',
        'metro': 'Свиблово',
        'number': '+1234567890',
        'delivery_date': '04.07.2024',
        'rent_days': 'сутки',
        'colour': 'чёрный жемчуг',
        'comment': 'Позвонить за 5 минут'
    }

    SECOND_ORDER = {
        'name': 'Абрам',
        'last_name': 'Линкольн',
        'address': 'То тут то там',
        'metro': 'Крылатское',
        'number': '+3424123123',
        'delivery_date': '01.07.2024',
        'rent_days': 'двое суток',
        'colour': 'серая безысходность',
        'comment': 'Не звонить!'
    }



class QuestionsAndAnswers:
    # Блок Вопросы о важном на Главной странице
    QUESTIONS_AND_ANSWERS_LIST = [
        (1, 'Сколько это стоит? И как оплатить?',
            'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
        (2, 'Хочу сразу несколько самокатов! Так можно?',
            'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, '
            'можете просто сделать несколько заказов — один за другим.'),
        (3, 'Как рассчитывается время аренды?',
            'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. '
            'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. '
            'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
        (4, 'Можно ли заказать самокат прямо на сегодня?',
            'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
        (5, 'Можно ли продлить заказ или вернуть самокат раньше?',
            'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
        (6, 'Вы привозите зарядку вместе с самокатом?',
            'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — '
            'даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),
        (7, 'Можно ли отменить заказ?',
            'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
        (8, 'Я жизу за МКАДом, привезёте?',
            'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
    ]


class IdCourier:
    id_courier = "363538"