from utils.api import GoogleMapsApi
from utils.checking import Checking
from conftest import create_place
import allure

@allure.epic("ТЕСТЫ GET")
class TestGetPlace:
    """Тесты по получению информации по локациям"""

    @allure.description("Получение информации по существующей локации. Проверка успешого получения информации со всеми нужными полями"
                        "и совпадением значений обязательных полей")
    @allure.tag("positive")
    def test_get_place_with_valid_id(self, create_place):
        print("ТЕСТ: Получение информации по существующей локации")
        with allure.step("Создание локации через fixture"):
            place_id = create_place

        with allure.step("GET. Получение информации по локации"):
            result_get = GoogleMapsApi.get_new_place(place_id)

        with allure.step("Проверки: статус-код, наличие поля, значение поля, пустота поля"):
            Checking.check_status_code(result_get, 200)
            Checking.check_json_token(result_get,
                                      ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                       'language'])
            Checking.check_json_empty_value(result_get,
                                      ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                       'language'])
            payload = GoogleMapsApi.create_place_payload()
            Checking.check_json_value(result_get, 'address', payload['address'])
            Checking.check_json_value(result_get, 'name', payload['name'])
            Checking.check_json_value(result_get, 'location', payload['location'])

    @allure.description("Получение информации по несуществующей локации. Проверка ошибки при попытке получить информацию по несуществующей"
                        "локации")
    @allure.tag("negative")
    def test_get_place_by_invalid_id(self):
        print("ТЕСТ: Получение информации по несуществующей локации")

        with allure.step("GET. Получение информации по локации"):
            place_id = "1234"
            result_get = GoogleMapsApi.get_new_place(place_id)

        with allure.step("Проверки: статус-код, наличие поля, значение поля"):
            Checking.check_status_code(result_get, 404)
            Checking.check_json_token(result_get, ['msg'])
            Checking.check_json_search_word_in_value(result_get, 'msg', "failed")


