import os
from scrape_tools.cache import Cache

from unittest.mock import Mock
from unittest.mock import patch

from ..conftest import FAKE_CACHE_DIR


def test_folder_creation():
    Cache(cache_dir=FAKE_CACHE_DIR)
    assert os.path.exists(FAKE_CACHE_DIR)


def test_save__ok_html():
    cache = Cache(cache_dir=FAKE_CACHE_DIR)
    mocked_response = Mock()
    mocked_response.ok = True

    with patch.object(
        Cache, "format_response", return_value={"any_elem": "any_value"}
    ):
        cache.save(
            cache_file_id="any_ok_file_id",
            response=mocked_response,
            response_type="html",
        )

    assert os.path.exists(os.path.join(FAKE_CACHE_DIR, "any_ok_file_id.json"))


def test_save__ok_json():
    cache = Cache(cache_dir=FAKE_CACHE_DIR)
    mocked_response = Mock()
    mocked_response.ok = True

    with patch.object(
        Cache, "format_response", return_value={"any_elem": "any_value"}
    ):
        cache.save(
            cache_file_id="any_ok_file_id",
            response=mocked_response,
            response_type="json",
        )

    assert os.path.exists(os.path.join(FAKE_CACHE_DIR, "any_ok_file_id.json"))


def test_save__error_json():
    cache = Cache(cache_dir=FAKE_CACHE_DIR)

    mocked_error_response = Mock()
    mocked_error_response.ok = False

    with patch.object(
        Cache, "format_response", return_value={"any_elem": "any_value"}
    ):
        cache.save(
            cache_file_id="any_error_file_id",
            response=mocked_error_response,
            response_type="json",
        )

    assert os.path.exists(
        os.path.join(FAKE_CACHE_DIR, "error_any_error_file_id.json")
    )


def test_save__error_html():
    cache = Cache(cache_dir=FAKE_CACHE_DIR)

    mocked_error_response = Mock()
    mocked_error_response.ok = False

    with patch.object(
        Cache, "format_response", return_value={"any_elem": "any_value"}
    ):
        cache.save(
            cache_file_id="any_error_file_id",
            response=mocked_error_response,
            response_type="html",
        )

    assert os.path.exists(
        os.path.join(FAKE_CACHE_DIR, "error_any_error_file_id.json")
    )


def test_load():
    cache = Cache(cache_dir=FAKE_CACHE_DIR)
    mocked_response = Mock()
    mocked_response.ok = True

    with patch.object(
        Cache,
        "format_response",
        return_value={
            "url": "any_url",
            "status_code": 200,
            "content": {"any_elem": "any_value"},
            "encoding": "any_encoding",
            "response_type": "json",
        },
    ):
        cache.save(
            cache_file_id="any_ok_file_id_to_load",
            response=mocked_response,
            response_type="json",
        )
        cached_object = cache.load("any_ok_file_id_to_load")

        assert cached_object.json == {"any_elem": "any_value"}


def test_should_scrap():
    cache = Cache(FAKE_CACHE_DIR)

    mocked_response = Mock()
    mocked_response.ok = True

    with patch.object(
        Cache,
        "format_response",
        return_value={
            "url": "any_url",
            "status_code": 200,
            "content": {"any_elem": "any_value"},
            "encoding": "any_encoding",
            "response_type": "json",
        },
    ):
        cache.save(
            cache_file_id="should_not_scrap",
            response=mocked_response,
            response_type="json",
        )
    assert not cache.should_scrap("should_not_scrap")


def test_get_file_id():
    cache = Cache(FAKE_CACHE_DIR)
    assert cache.get_file_name("any_file_name") == "any_file_name.json"
