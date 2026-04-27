from utils.api import GoogleMapsApi
from utils.checking import Checking
import allure

@allure.epic("TЕСТЫ ПОЛНЫХ СЦЕНАРИЕВ POST-GET-PUT-DELETE")
class TestCreatePlace():
    """Тест полного сценария: Создание, изменение и удаление новой локации"""

    @allure.description("Создание, изменение и удаление новой локации. Проверка успешности полного сценария.")
    @allure.tag("positive")
    def test_full(self):
        print("ТЕСТ: Создание локации с валидными данными.\n")

        print("Метод POST - создание")
        with allure.step("POST. Создание новой локации"):
            payload = GoogleMapsApi.create_place_payload()
            result_post = GoogleMapsApi.create_new_place(payload)
            check_post = result_post.json()
            place_id = check_post['place_id']

        with allure.step("Проверки: статус-код, наличие поля, значение поля, пустота поля"):
            Checking.check_status_code(result_post, 200)
            Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
            Checking.check_json_empty_value(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
            Checking.check_json_value(result_post, 'status', 'OK')

        print("\nМетод GET - информация по новому месту")
        with allure.step("GET. Получение информации по новой локации"):
            result_get = GoogleMapsApi.get_new_place(place_id)

        with allure.step("Проверки: статус-код, наличие поля, значение поля, пустота поля"):
            Checking.check_status_code(result_get, 200)
            Checking.check_json_token(result_get,
                                      ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                       'language'])
            Checking.check_json_empty_value(result_get,
                                            ['location', 'accuracy', 'name', 'phone_number', 'address', 'types',
                                             'website',
                                             'language'])
            Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')


        print("\nМетод PUT - обновление адреса")
        with allure.step("PUT. Изменение данных о локации"):
            new_address = {"address": "100 Lenina street, RU"}
            result_put = GoogleMapsApi.put_new_address_to_place(place_id, new_address)

        with allure.step("Проверки: статус-код, наличие поля, значение поля"):
            Checking.check_status_code(result_put, 200)
            Checking.check_json_token(result_put, ["msg"])
            Checking.check_json_value(result_put, 'msg', 'Address successfully updated')



        print("\nМетод GET - информация по обновленному месту")
        with allure.step("GET. Получение информации по измененной локации"):
            result_get = GoogleMapsApi.get_new_place(place_id)

        with allure.step("Проверки: статус-код, наличие поля, значение поля, пустота поля"):
            Checking.check_status_code(result_get, 200)
            Checking.check_json_token(result_get,
                                      ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                                       'language'])
            Checking.check_json_empty_value(result_get,
                                            ['location', 'accuracy', 'name', 'phone_number', 'address', 'types',
                                             'website',
                                             'language'])
            Checking.check_json_value(result_get, 'address', '100 Lenina street, RU')


        print("\nМетод DELETE - удаление места")
        with allure.step("DELETE. Удаление созданной локации"):
            result_delete = GoogleMapsApi.delete_new_place(place_id)

        with allure.step("Проверки: статус-код, наличие поля, значение поля"):
            Checking.check_status_code(result_delete, 200)
            Checking.check_json_token(result_delete, ["status"])
            Checking.check_json_value(result_delete, 'status', 'OK')

        print("\nМетод GET - получение информации по удаленному месту")
        with allure.step("GET. Получение информации по удаленной локации"):
            result_get = GoogleMapsApi.get_new_place(place_id)

        with allure.step("Проверки: статус-код, наличие поля, значение поля"):
            Checking.check_status_code(result_get, 404)
            Checking.check_json_token(result_get, ["msg"])
            Checking.check_json_search_word_in_value(result_get, 'msg', "failed")



