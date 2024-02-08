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
