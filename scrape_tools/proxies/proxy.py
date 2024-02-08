class Proxy:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port

    def get_address(self) -> dict:
        return {
            "http": f"{self.host}:{self.port}",
            "https": f"{self.host}:{self.port}",
        }

    def renew_ip(self) -> None:
        pass
