from ..constants import (
    STATUS_CODE,
    URL,
    CONTENT,
    ENCODING,
    RESPONSE_TYPE,
    HTML_RESPONSE,
    JSON_RESPONSE,
)

from typing import Union


class CachedResponse:
    def __init__(
        self,
        status_code: int,
        url: str,
        content: Union[dict, str],
        encoding: str,
        response_type: str,
    ) -> None:
        self._status_code = status_code
        self._url = url
        self._content = content
        self._encoding = encoding
        self._response_type = response_type
        self._json = None
        self._text = None
        if response_type == HTML_RESPONSE:
            self.text = content
        if response_type == JSON_RESPONSE:
            self.json = content

    @property
    def status_code(self) -> int:
        return self._status_code

    @status_code.setter
    def status_code(self, status_code: int) -> None:
        self._status_code = status_code

    @property
    def url(self) -> str:
        return self._url

    @url.setter
    def url(self, url: str) -> None:
        self._url = url

    @property
    def content(self) -> dict:
        return self._content

    @content.setter
    def content(self, content: dict) -> None:
        self._content = content

    @property
    def encoding(self) -> str:
        return self._encoding

    @encoding.setter
    def encoding(self, encoding: str) -> None:
        self._encoding = encoding

    @property
    def response_type(self) -> str:
        return self._response_type

    @response_type.setter
    def response_type(self, response_type: str) -> None:
        self._response_type = response_type

    @property
    def json(self) -> dict:
        return self._json

    @json.setter
    def json(self, json: dict) -> None:
        self._json = json

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, text: str) -> None:
        self._text = text

    @classmethod
    def from_cache(cls, cache_file_content: dict) -> "CachedResponse":
        return cls(
            cache_file_content.get(STATUS_CODE),
            cache_file_content.get(URL),
            cache_file_content.get(CONTENT),
            cache_file_content.get(ENCODING),
            cache_file_content.get(RESPONSE_TYPE),
        )

    def json(self) -> dict:
        return {
            STATUS_CODE: self.status_code,
            URL: self.url,
            CONTENT: self.content,
            ENCODING: self.encoding,
            RESPONSE_TYPE: self.response_type,
        }
