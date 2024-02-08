from .proxy import Proxy


class AuthProxy(Proxy):
    def __init__(
        self,
        host: str,
        port: int,
        name: str,
        password: str,
    ) -> None:
        super().__init__(host, port)
        self.name = name
        self.password = password

    def get_address(self) -> dict:
        return {
            "http": f"http://{self.name}:{self.password}@{self.host}:{self.port}",  # noqa: E501
            "https": f"http://{self.name}:{self.password}@{self.host}:{self.port}",  # noqa: E501
        }
