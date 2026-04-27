from utils.api import GoogleMapsApi
from utils.checking import Checking
from conftest import create_place
import allure

@allure.epic("ТЕСТЫ DELETE")
class TestDeletePlace:
    """Тесты по удалению локаций"""

    @allure.description("Удаление существующей локации. Проверка успешного удаления существующей локации")
    @allure.tag("positive")
    def test_delete_new_place(self, create_place):
        print("ТЕСТ: Удаление существующей локации")

        with allure.step("Создание локации через fixture"):
            place_id = create_place


        with allure.step("DELETE. Удаление созданной локации"):
            result_delete = GoogleMapsApi.delete_new_place(place_id)

        with allure.step("Проверки: статус-код, наличие поля, значение поля"):
            Checking.check_status_code(result_delete, 200)
            Checking.check_json_token(result_delete, ["status"])
            Checking.check_json_value(result_delete, 'status', 'OK')

        with allure.step("GET. Получение информации по удаленной локации"):
            result_get = GoogleMapsApi.get_new_place(place_id)

        with allure.step("Проверки: статус-код, наличие поля, значение поля"):
            Checking.check_status_code(result_get, 404)
            Checking.check_json_token(result_get, ["msg"])
            Checking.check_json_search_word_in_value(result_get, 'msg', "failed")

    @allure.description("Удаление несуществующей локации. Проверка ошибки при удалении несуществующей локации")
    @allure.tag("negative")
    def test_delete_non_existent_place(self, create_place):
        print("ТЕСТ: Удаление несуществующей локации")

        with allure.step("DELETE. Удаление созданной локации"):
            place_id = "1234"
            result_delete = GoogleMapsApi.delete_new_place(place_id)

        with allure.step("Проверки: статус-код, наличие поля, значение поля"):
            Checking.check_status_code(result_delete, 404)
            Checking.check_json_token(result_delete, ["msg"])
            Checking.check_json_search_word_in_value(result_delete, 'msg', "failed")


    @allure.description("Идемпотентность удаления локации. Проверка ошибки при дублировании удаления локации")
    @allure.tag("negative")
    def test_delete_idempotency(self, create_place):
        print("ТЕСТ: Идемпотентность удаления локации")
        with allure.step("Создание локации через fixture"):
            place_id = create_place

        with allure.step("DELETE. Удаление созданной локации"):
            result_delete = GoogleMapsApi.delete_new_place(place_id)

        with allure.step("Проверки: статус-код, наличие поля, значение поля"):
            Checking.check_status_code(result_delete, 200)
            Checking.check_json_token(result_delete, ["status"])
            Checking.check_json_search_word_in_value(result_delete, 'status', "OK")

        with allure.step("DELETE. Повторное удаление созданной локации"):
            result_delete_2 = GoogleMapsApi.delete_new_place(place_id)

        with allure.step("Проверки: статус-код, наличие поля, значение поля"):
            Checking.check_status_code(result_delete_2, 404)
            Checking.check_json_token(result_delete_2, ["msg"])
            Checking.check_json_search_word_in_value(result_delete_2, 'msg', "failed")
