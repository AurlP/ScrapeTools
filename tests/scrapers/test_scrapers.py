from requests import Response
from unittest.mock import Mock
from unittest.mock import patch


from scrape_tools.scrapers import Scraper
from scrape_tools.cache import Cache


def test_scrape():
    scraper = Scraper(
        cache=Mock(Cache), proxy=None, retry_cooldown=0, max_tries=5
    )
    mocked_response_200 = Mock(Response)
    mocked_response_200.ok = True
    mocked_response_200.status_code = 200
    with patch.object(
        Scraper,
        "scrape_from_web",
        side_effect=[None, None, None, mocked_response_200],
    ) as patched_request_from_web:
        scraper.scrape(
            method="ANY",
            url="any_url",
            cache_file_id="any_file_id",
            response_type="json",
        )
    assert patched_request_from_web.call_count == 4


def test_scrape__cache_exists():
    class MockedCache(Mock):
        def should_scrap(*args):
            return True

    with patch.object(Scraper, "load_from_cache") as patched_request_from_cache:
        with patch.object(Scraper, "scrape_from_web") as patched_retry:
            scraper = Scraper(
                cache=MockedCache(), proxy=None, retry_cooldown=0, max_tries=5
            )
            scraper.scrape(
                cache_file_id="any_file_id",
                url="any_url",
                method="ANY",
                response_type="json",
            )
            assert patched_retry.call_count == 1
            assert patched_request_from_cache.call_count == 0


def test_scrape__no_cache():
    class MockedCache(Mock):
        def should_scrap(*args):
            return False

    with patch.object(Scraper, "load_from_cache") as patched_request_from_cache:
        with patch.object(Scraper, "scrape_from_web") as patched_retry:
            scraper = Scraper(
                cache=MockedCache(), proxy=None, retry_cooldown=0, max_tries=5
            )
            scraper.scrape(
                cache_file_id="any_file_id",
                url="any_url",
                method="ANY",
                response_type="json",
            )
            assert patched_retry.call_count == 0
            assert patched_request_from_cache.call_count == 1
