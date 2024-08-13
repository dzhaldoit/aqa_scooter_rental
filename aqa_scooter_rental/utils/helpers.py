import random
import string

import allure


class GenerateString:
    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    def generate_random_integer(length):
        letters = string.digits
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string


class GenerateDataCourier:
    @allure.step('Генерация логина, пароля, имени курьера')
    def generate_data_courier(self):
        login = GenerateString.generate_random_string(5)
        password = GenerateString.generate_random_integer(4)
        first_name = GenerateString.generate_random_string(5)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        return payload

    @allure.step('Генерация пароля и имени курьера, статичный логин')
    def generate_data_courier_static_login(self):
        password = GenerateString.generate_random_string(10)
        first_name = GenerateString.generate_random_string(10)

        payload = {
            "login": "Naruto",
            "password": password,
            "firstName": first_name
        }

        return payload
