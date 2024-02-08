import os
import pytest
import shutil

FAKE_CACHE_DIR = "./tests/fake_cache_dir"


@pytest.fixture(autouse=True)
def clean_fake_cache():
    if os.path.exists(FAKE_CACHE_DIR):
        shutil.rmtree(FAKE_CACHE_DIR)
