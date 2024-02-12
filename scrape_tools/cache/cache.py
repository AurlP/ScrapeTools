import json
import os
from requests import Response

from ..constants import (
    STATUS_CODE,
    URL,
    CONTENT,
    ENCODING,
    RESPONSE_TYPE,
    HTML_RESPONSE,
    JSON_RESPONSE,
)
from ..responses import CachedResponse, ErrorResponse

FILE_TYPE = "json"
ERROR_FILE_PREFIX = "error"


class Cache:
    def __init__(self, cache_dir: str) -> None:
        self.cache_dir = cache_dir
        os.makedirs(cache_dir, exist_ok=True)

    def save(
        self, cache_file_id: str, response: Response, response_type: str
    ) -> None:
        if response.ok:
            file_name = self.get_file_name(cache_file_id)
        else:
            file_name = (
                f"{ERROR_FILE_PREFIX}_{self.get_file_name(cache_file_id)}"
            )
        with open(os.path.join(self.cache_dir, file_name), "w") as f:
            json.dump(self.format_response(response, response_type), f)

    def save_error(
        self, cache_file_id: str, error_response: ErrorResponse
    ) -> None:
        file_name = f"{ERROR_FILE_PREFIX}_{self.get_file_name(cache_file_id)}"
        with open(os.path.join(self.cache_dir, file_name), "w") as f:
            json.dump(error_response.json(), f)

    def load(self, cache_file_id: str) -> CachedResponse:
        with open(
            os.path.join(self.cache_dir, self.get_file_name(cache_file_id)), "r"
        ) as f:
            cached_file_content = json.load(f)
            return CachedResponse.from_cache(cached_file_content)

    def should_scrap(self, cache_file_id: str) -> bool:
        return not os.path.exists(
            os.path.join(self.cache_dir, self.get_file_name(cache_file_id))
        )

    @staticmethod
    def get_file_name(cache_file_id: str) -> str:
        return f"{cache_file_id}.{FILE_TYPE}"

    def format_response(self, response: Response, response_type: str) -> dict:
        if response_type == JSON_RESPONSE:
            return {
                RESPONSE_TYPE: JSON_RESPONSE,
                STATUS_CODE: response.status_code,
                URL: response.url,
                CONTENT: response.json(),
                ENCODING: response.encoding,
            }
        elif response_type == HTML_RESPONSE:
            return {
                RESPONSE_TYPE: HTML_RESPONSE,
                STATUS_CODE: response.status_code,
                URL: response.url,
                CONTENT: response.text,
                ENCODING: response.encoding,
            }
        # else:
        #     raise ValueError("Please enter a valid response type")
