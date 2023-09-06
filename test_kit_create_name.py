import api_requests
import data


# Функция получения токена авторизации пользователя
def get_token():
    # В переменную response сохраняется результат запроса на создание нового пользователя
    response = api_requests.create_new_user()
    # Функция возвращает токен
    return response.json()["authToken"]


# Функция составления заголовков запроса на создание набора пользователя
def get_kit_headers():
    # В переменную auth_token сохраняется результат выполнения функции получения токена авторизации пользователя
    auth_token = get_token()
    # В переменную current_headers помещается копия заголовков запроса из файла data
    current_headers = data.kit_headers.copy()
    # В заголовки добавляется токен авторизации
    current_headers["Authorization"] = "Bearer " + auth_token
    # Функция возвращает заголовки запроса с токеном авторизации
    return current_headers


# Функция составления тела запроса на создание набора пользователя с тестовым значением name
def get_kit_body(name):
    # В переменную current_body помещается копия тела запроса из файла data
    current_body = data.kit_body.copy()
    # Параметр name получает новое значение
    current_body["name"] = name
    # Функция возвращает тело запроса с новым значением параметра name
    return current_body


# Функция составления тела запроса на создание набора пользователя с отсутствием параметра name
def get_kit_body_without_name():
    # В переменную current_body помещается копия тела запроса из файла data
    current_body = data.kit_body.copy()
    # Параметр name удаляется из тела запроса
    current_body.pop("name")
    # Функция возвращает тело запроса без параметра name
    return current_body


# Функция для позитивных проверок
def positive_assert(test_name):
    # В переменную test_kit_headers помещаются необходимые для теста заголовки запроса
    test_kit_headers = get_kit_headers()
    # В переменную test_kit_body помещается необходимое для теста тело запроса
    test_kit_body = get_kit_body(test_name)
    # В переменную test_response сохраняется результат запроса на создание набора пользователя
    test_response = api_requests.create_new_user_kit(test_kit_headers, test_kit_body)

    # Проверяется, что код ответа равен 201
    assert test_response.status_code == 201
    # Проверяется, что в ответе поле name совпадает с полем name в запросе
    assert test_response.json()["name"] == test_name


# Функция для негативных проверок без проверок тела ответа
def negative_assert(test_name):
    # В переменную test_kit_headers помещаются необходимые для теста заголовки запроса
    test_kit_headers = get_kit_headers()
    # В переменную test_kit_body помещается необходимое для теста тело запроса
    test_kit_body = get_kit_body(test_name)
    # В переменную test_response сохраняется результат запроса на создание набора пользователя
    test_response = api_requests.create_new_user_kit(test_kit_headers, test_kit_body)

    # Проверяется, что код ответа равен 400
    assert test_response.status_code == 400


# Функция для негативных проверок с проверкой тела ответа
def negative_no_parameter_assert():
    # В переменную test_kit_headers помещаются необходимые для теста заголовки запроса
    test_kit_headers = get_kit_headers()
    # В переменную test_kit_body помещается необходимое для теста тело запроса
    test_kit_body = get_kit_body_without_name()
    # В переменную test_response сохраняется результат запроса на создание набора пользователя
    test_response = api_requests.create_new_user_kit(test_kit_headers, test_kit_body)

    # Проверяется, что код ответа равен 400
    assert test_response.status_code == 400
    # Проверяется, что значение параметра code в теле ответа соответствует документации API
    assert test_response.json()["code"] == 400
    # Проверяется, что значение параметра message в теле ответа соответствует документации API
    assert test_response.json()["message"] == "Не все необходимые параметры были переданы"


# Тест 1. Успешное создание пользовательского набора. Параметр name состоит из 1 символа
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")


# Тест 2. Успешное создание пользовательского набора. Параметр name состоит из 511 символов
def test_create_kit_511_letters_in_name_get_success_response():
    positive_assert(("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                              "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                              "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                              "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                              "abcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                              "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                              "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                              "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                              "abcdabcdabcdabcdabcdabcdabcdabC"))


# Тест 3. Ошибка. Параметр name состоит из пустой строки
def test_create_kit_empty_name_get_error_response():
    negative_assert("")


# Тест 4. Ошибка. Параметр name состоит из 512 символов
def test_create_kit_512_letters_in_name_get_error_response():
    negative_assert(("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                              "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                              "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                              "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                              "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                              "dAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                              "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                              "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                              "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                              "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"))


# Тест 5. Успешное создание пользовательского набора. Параметр name состоит из английских букв
def test_create_kit_english_letters_in_name_get_success_response():
    positive_assert("QWErty")


# Тест 6. Успешное создание пользовательского набора. Параметр name состоит из русских букв
def test_create_kit_russian_letters_in_name_get_success_response():
    positive_assert("Мария")


# Тест 7. Успешное создание пользовательского набора. Параметр name состоит из строки спецсимволов
def test_create_kit_has_special_symbols_in_name_get_success_response():
    positive_assert("\"№%@\",")


# Тест 8. Успешное создание пользовательского набора. Параметр name состоит из слов с пробелами
def test_create_kit_has_spaces_in_name_get_success_response():
    positive_assert(" Человек и КО ")


# Тест 9. Успешное создание пользовательского набора. Параметр name состоит из строки цифр
def test_create_kit_has_numbers_in_name_get_success_response():
    positive_assert("123")


# Тест 10. Ошибка. Запрос без параметра name
def test_create_kit_no_parameters_get_error_response():
    negative_no_parameter_assert()


# Тест 11. Ошибка. Тип параметра name: число
def test_create_kit_number_type_get_error_response():
    negative_assert(123)
