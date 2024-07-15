import json
from scrapers import scraper


def scrape(query, country, limit=10):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
               'Accept-Language': 'en-US,en;q=0.9',
               'Accept-Encoding': 'gzip, deflate, br',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'Connection': 'keep-alive'}

    with open('server/app/scrapers/stores.json') as f:
        configs = json.load(f)

    if country not in configs['countries']:
        raise ValueError(f"Country '{country}' is not supported")

    stores = configs['countries'][country]['stores']

    results = []
    for store_configs in stores.values():
        print(f"Scraping {store_configs['store_name']}...")
        results += scraper.scrape_store(store_configs, query, limit, headers)
        print(f"Found {len(results)} products so far")

    return results
