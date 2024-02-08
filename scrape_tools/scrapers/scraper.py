from requests import Session, Response
from requests.exceptions import RequestException

from time import sleep

from typing import Union

from ..cache import Cache
from ..proxies import Proxy
from ..responses import CachedResponse


class Scraper:
    def __init__(
        self,
        cache: Cache,
        proxy: Proxy = None,
        retry_cooldown: int = 5,
        max_tries: int = 1,
    ) -> None:
        self.cache = cache
        self.retry_cooldown = retry_cooldown
        self.max_tries = max_tries
        self.proxy = proxy
        self.init_session(proxy)

    def init_session(self, proxy: Proxy) -> Session:
        self.session = Session()
        if proxy is not None:
            self.session.proxies.update(proxy.get_address())

    def load_from_cache(self, cache_file_id: str) -> None:
        return self.cache.load(cache_file_id)

    def scrape_from_web(
        self, cache_file_id: str, method: str, url: str, *args, **kwargs
    ) -> Response:
        try:
            return self.session.request(method, url, *args, **kwargs)
        except RequestException as e:
            self.cache.save_error(cache_file_id, e)
            return None

    def scrape(
        self,
        cache_file_id: str,
        method: str,
        url: str,
        response_type: str,
        *args,
        **kwargs
    ) -> Union[Response, CachedResponse, None]:
        if self.cache.should_scrap(cache_file_id):
            tries = 0
            should_stop = False
            while tries < self.max_tries and not should_stop:
                response = self.scrape_from_web(
                    cache_file_id, method, url, *args, **kwargs
                )
                if response is not None:
                    if response.ok:
                        should_stop = True
                    else:
                        tries += 1
                        self.on_retry()
                else:
                    tries += 1
                    self.on_retry()
            if response is not None:
                self.cache.save(cache_file_id, response, response_type)
            return response
        else:
            return self.load_from_cache(cache_file_id)

    def on_retry(self) -> None:
        print("retrying")
        sleep(self.retry_cooldown)
