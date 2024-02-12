# Scrape Tools

Scrape Tools is a Python module designed to simplify web scraping tasks. It provides a set of tools and utilities to extract data from web pages efficiently and easily.

## Features

- Caching option.
- Built-in functionalities for handling rate limiting and IP blocking.
- Extendable architecture for adding new scraping strategies.

## Installation

Install Scrape Tools using pip:

```bash
pip3 install git+https://github.com/Pleased2Code/ScrapeTools.git@main
```

## Example

```python
from scrape_tools import Cache, Scraper

if __name__ == "__main__":
    cache = Cache(cache_dir="./data")
    proxy = None
    scraper = Scraper(cache=cache, proxy=proxy)

    scraper.scrape(
        cache_file_id="cache_file",
        method="GET",
        url="https://httpbin.org/ip",
        response_type="json",
    )
```
