import json

import uuid


class Checking:
    """Методы для проверки ответов запросов"""

    @staticmethod
    def check_status_code(result, status_code):
        """Метод для проверки статус-кода"""
        assert status_code == result.status_code, (f"ОШИБКА, статус код неверный. Текущий статус-код: {result.status_code} "
                                                   f"Полный ответ: {result.text}")
        print(f"Успешно. Статус код равно: {str(result.status_code)}")


    @staticmethod
    def check_json_token(response, expected_value):
        """Метод для проверки наличия полей в ответе запроса"""
        token = json.loads(response.text)
        assert list(token) == expected_value, "ОШИБКА, в ответе отсутсвтуют некоторые поля"
        print("Успешно. Все поля в ответе присутствуют")


    @staticmethod
    def check_json_value(response, field_name, expected_value):
        """Метод для проверки значения поля в ответе запроса"""
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value, f"ОШИБКА, значение поля не соответсвует. Теущее значение: {check_info}"
        print(f"Успешно. Поле {field_name} верен: {check_info}")


    @staticmethod
    def check_json_search_word_in_value(response, field_name, search_word):
        """Метод для проверки вхождения заданного слова в ответе поля"""
        check = response.json()
        check_info = check.get(field_name)
        assert search_word in check_info, f"ОШИБКА, заданные значения не входят в ответ. Текущие значение: {check_info}"
        print(f"Успешно. Поле {field_name} содержит {check_info}")


    @staticmethod
    def check_json_empty_value(response, fields_name):
        """Метод проверки на пустоту поля"""
        check = response.json()
        for field in fields_name:
            check_info = check.get(field)
            assert check_info is not None and check_info != "", f"ОШИБКА, поле {field} пустое"

        print(f"Успешно. Поле(я) не пустое(ые).")

    @staticmethod
    def check_json_uuid(response, field_name):
        """Метод проверки на соответствие формату UUID"""
        check = response.json()
        check_info = check.get(field_name)
        try:
            uuid.UUID(check_info)
        except ValueError:
            assert False, "ОШИБКА, ответ не соответствует формату UUID"
        print(f'Поле {field_name} соответствуют формату UUID')



