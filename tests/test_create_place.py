from utils.api import GoogleMapsApi
from utils.checking import Checking
import allure

@allure.epic("ТЕСТЫ POST")
class TestCreatePlace:
    """Тесты по созданию локаций"""
    payload = GoogleMapsApi.create_place_payload()

    @allure.description("Создание локации с валидными данными. Проверка успешного создания.")
    @allure.tag("positive")
    def test_create_new_place(self):

        print("ТЕСТ: Создание локации с валидными данными.")

        with allure.step("POST. Создание новой локации"):
            result_post = GoogleMapsApi.create_new_place(self.payload)

        with allure.step("Проверки: статус-код, наличие поля, значение поля, пустота поля, соответствие uuid"):
            Checking.check_status_code(result_post, 200)
            Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
            Checking.check_json_empty_value(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
            Checking.check_json_value(result_post, 'status', 'OK')
            Checking.check_json_uuid(result_post, "place_id")

    @allure.description("Создание локации с пустым полем name. Проверка ошибки при создании с пустым полем.")
    @allure.tag("negative")
    def test_create_place_with_empty_name(self):
        print("ТЕСТ: Создание локации с пустым обязательным полем name")

        with allure.step("POST. Создание новой локации"):
            self.payload['name'] = ''
            result_post = GoogleMapsApi.create_new_place(self.payload)

        with allure.step("Проверки: статус-код, наличие поля, пустота поля"):
            Checking.check_status_code(result_post, 400)
            Checking.check_json_token(result_post, ['msg'])
            Checking.check_json_empty_value(result_post, ['msg'])

    @allure.description("Создание локации без поля location. Проверка ошибки создания без обязательного поля")
    @allure.tag("negative")
    def test_create_place_without_location(self):
        print("ТЕСТ: Создание локации без поля location")

        with allure.step("POST. Создание новой локации"):
            del self.payload['location']
            result_post = GoogleMapsApi.create_new_place(self.payload)

        with allure.step("Проверки: статус-код, наличие поля, пустота поля"):
            Checking.check_status_code(result_post, 400)
            Checking.check_json_token(result_post, ['msg'])
            Checking.check_json_empty_value(result_post, ['msg'])







