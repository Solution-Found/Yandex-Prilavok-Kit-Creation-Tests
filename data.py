# Заголовки запроса на создание нового пользователя
user_headers = {
    "Content-Type": "application/json"
}

# Заголовки запроса на создание нового пользовательского набора
kit_headers = {
    "Content-Type": "application/json",
    "Authorization": ""
}

# Тело запроса на создание нового пользователя
user_body = {
    "firstName": "Олег",
    "phone": "+79995555555",
    "address": "г. Москва, ул. Малая Полянка, д. 2"
}

# Тело запроса на создание нового пользовательского набора
kit_body = {
    "name": "test"
}
