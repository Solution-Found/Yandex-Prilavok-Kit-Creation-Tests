import requests
import config
import data


# Функция запроса на создание нового пользователя
def create_new_user():
    # Составление URL запроса
    return requests.post(config.URL_SERVICE + config.CREATE_USER_PATH, headers=data.user_headers, json=data.user_body)


# Функция запроса на создание нового пользовательского набора
def create_new_user_kit(headers, body):
    # Составление URL запроса
    return requests.post(config.URL_SERVICE + config.CREATE_KIT_PATH, headers=headers, json=body)
