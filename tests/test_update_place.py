from utils.api import GoogleMapsApi
from utils.checking import Checking
from conftest import create_place
import allure

@allure.epic("ТЕСТЫ UPDATE")
class TestUpdatePlace:
    """Тесты по изменению полей локаций"""

    @allure.description("Изменение на валидный address в существующей локации. Проверка успешного изменения поля")
    @allure.tag("positive")
    def test_update_address_valid(self, create_place):
        print("ТЕСТ: Изменение на валидный адрес в существующей локации")

        with allure.step("Создание локации через fixture"):
            place_id = create_place

        with allure.step("PUT. Изменение данных о локации"):
            new_address = {"address": "100 Lenina street, RU"}
            result_put = GoogleMapsApi.put_new_address_to_place(place_id, new_address)

        with allure.step("Проверки: статус-код, наличие поля, значение поля"):
            Checking.check_status_code(result_put, 200)
            Checking.check_json_token(result_put, ["msg"])
            Checking.check_json_value(result_put, 'msg', 'Address successfully updated')

        with allure.step("GET. Получение информации по локации"):
            result_get = GoogleMapsApi.get_new_place(place_id)

        with allure.step("Проверки: статус-код, наличие поля, значение поля, пустота поля"):
            Checking.check_status_code(result_get, 200)
            Checking.check_json_token(result_get,
                                      ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                       'language'])
            Checking.check_json_empty_value(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types',])
            Checking.check_json_value(result_get, 'address', '100 Lenina street, RU')

    @allure.description("Изменение address на невалидный тип данных int. Проверка ошибки при попытке изменить тип данных на невалидный")
    @allure.tag("negative")
    def test_update_address_invalid_int(self, create_place):
        print("ТЕСТ: Изменение address на невалидный тип данных int")

        with allure.step("Создание локации через fixture"):
            place_id = create_place

        with allure.step("PUT. Изменение данных о локации"):
            new_address = {"address": 1234}
            result_put = GoogleMapsApi.put_new_address_to_place(place_id, new_address)

        with allure.step("Проверки: статус-код, наличие поля, пустота поля"):
            Checking.check_status_code(result_put, 404)
            Checking.check_json_token(result_put, ["msg"])
            Checking.check_json_empty_value(result_put, ["msg"])

