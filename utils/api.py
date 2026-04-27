from utils.httpmethods import HttpMethods

#Базовая URL и ключ
base_url = 'https://rahulshettyacademy.com'
key = "?key=qaclick123"

class GoogleMapsApi:
    """Методы для тестирования Google Maps API"""

    @staticmethod
    def create_place_payload():
        """Метод с генерацией тела запроса для создания локации"""
        create_payload = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            },
            "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }
        return create_payload

    @staticmethod
    def update_place_payload(place_id):
        """Метод с генерацией тела запроса для создания локации"""
        update_place_payload = {
            "place_id": place_id,
            "key": "qaclick123"
        }
        return update_place_payload

    @staticmethod
    def create_new_place(payload):
        """Метод для создания новой локации"""
        post_resource = "/maps/api/place/add/json" #Ресурс метода Post
        json_for_create_new_place = payload
        post_url = base_url + post_resource + key
        print(post_url)

        result_post = HttpMethods.post(post_url, json_for_create_new_place)
        print(result_post.text)
        return result_post


    @staticmethod
    def get_new_place(place_id):
        """Метод для проверки локации"""
        get_resource = "/maps/api/place/get/json" #Ресурс метода Get
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)
        result_get = HttpMethods.get(get_url)
        print(result_get.text)
        return result_get


    @staticmethod
    def put_new_address_to_place(place_id, update_field):
        """Метод для изменения полей локации"""
        put_resource = "/maps/api/place/update/json"  # Ресурс метода Put
        put_url = base_url + put_resource + key
        print(put_url)

        payload = GoogleMapsApi.update_place_payload(place_id)
        json_for_update_new_location = payload | update_field

        result_put = HttpMethods.put(put_url, json_for_update_new_location)
        print(result_put.text)
        return result_put


    @staticmethod
    def delete_new_place(place_id):
        """Метод для удаления локации"""
        delete_resource = "/maps/api/place/delete/json"  # Ресурс метода Put
        delete_url = base_url + delete_resource + key
        print(delete_url)

        json_for_delete_new_location = {
            "place_id": place_id,
        }

        result_delete = HttpMethods.delete(delete_url, json_for_delete_new_location)
        print(result_delete.text)
        return result_delete



