from utils.api import GoogleMapsApi
import pytest
from utils.logger import Logger

@pytest.fixture
def create_place():
    """Фиксирвоанные данные для создания места"""
    payload = GoogleMapsApi.create_place_payload()
    response = GoogleMapsApi.create_new_place(payload)

    assert response.status_code == 200, f"ОШИБКА, создание фикстуры не произошло. Ответ: {response.text}"

    token = response.json()
    place_id = token.get("place_id")
    assert place_id is not None, "ОШИБКА, place_id не получен"
    return place_id


@pytest.fixture(scope="session", autouse=True)
def clear_logs():
    """Чистка логов перед каждым тестом"""
    log_dir = Logger.LOG_DIR

    if log_dir.exists():
        for file in log_dir.iterdir():
            if file.is_file():
                file.unlink()