import socket
from stem import Signal
from stem.control import Controller

from .auth_proxy import AuthProxy


class TorProxy(AuthProxy):
    def __init__(
        self,
        host: str,
        port: int,
        name: str,
        password: str,
        control_port: int = 9051,
    ) -> None:
        super().__init__(host, port, name, password)
        self.control_port = control_port

    # needed if the ip is renewed from an other container
    def get_container_ip(self):
        return socket.gethostbyname(self.host)

    def renew_ip(self):
        print(f"Renewing ip for {self.name} (port {self.port})")
        with Controller.from_port(
            address=self.get_container_ip(), port=self.control_port
        ) as c:
            c.authenticate(password=self.password)
            c.signal(Signal.NEWNYM)
