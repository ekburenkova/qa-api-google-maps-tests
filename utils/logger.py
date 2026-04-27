import datetime
import os
from pathlib import Path

class Logger:
    """Запись логов в файл"""
    BASE_DIR = Path(__file__).resolve().parent.parent  # корень проекта
    LOG_DIR = BASE_DIR / "logs"

    LOG_DIR.mkdir(exist_ok=True)

    file_name = LOG_DIR / f"log{datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log"

    @classmethod
    def write_log_to_file(cls, data: str):
        with open(cls.file_name, 'a', encoding='utf-8') as logger_file:
            logger_file.write(data)

    @classmethod
    def add_request(cls, url: str, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        data_to_add = f"\n-----\n"
        data_to_add += f"Test: {test_name}\n"
        data_to_add += f"Time: {str(datetime.datetime.now())}\n"
        data_to_add += f"Method: {method}\n"
        data_to_add += f"URL: {url}\n"
        data_to_add += f"\n"

        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_response(cls, result):
        cookies_as_dict = dict(result.cookies)
        headers_as_dict = dict(result.headers)

        data_to_add = f"Response code: {result.status_code}\n"
        data_to_add += f"Response text: {result.text}\n"
        data_to_add += f"Headers: {headers_as_dict}\n"
        data_to_add += f"Cookies: {cookies_as_dict}\n"
        data_to_add += f"\n-----\n"

        cls.write_log_to_file(data_to_add)


