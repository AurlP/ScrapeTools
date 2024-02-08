from .scraper import Scraper
from ..cache import Cache
from ..proxies import TorProxy


class TorScraper(Scraper):
    def __init__(
        self,
        cache: Cache,
        proxy: TorProxy,
        retry_cooldown: int = 5,
        max_tries: int = 1,
    ) -> None:
        super().__init__(cache, proxy, retry_cooldown, max_tries)

    def on_retry(self) -> None:
        super().on_retry()
        self.proxy.renew_ip()
