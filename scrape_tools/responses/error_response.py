from ..constants import ERROR, URL


class ErrorResponse:
    def __init__(
        self,
        url: str,
        error: str,
    ) -> None:
        self.url = url
        self._error = error

    @property
    def url(self) -> str:
        return self._url

    @url.setter
    def url(self, url: str) -> None:
        self._url = url

    @property
    def error(self) -> str:
        return self._error

    @error.setter
    def error(self, error: str) -> None:
        self._error = error

    def json(self) -> dict:
        return {
            URL: self.url,
            ERROR: self.error,
        }
