import json
from pathlib import Path as path
from scraper_logic import scraper


def scrape(query, country, limit=10):
    # Get the directory where the current script is located (needed to allow Vercel to find the stores.json file)
    base_path = path(__file__).resolve().parent

    with open(base_path/'stores.json') as f:
        configs = json.load(f)

    if country not in configs['countries']:
        raise ValueError(f"Country '{country}' is not supported")

    stores = configs['countries'][country]['stores']

    results = []
    for store_configs in stores.values():
        print(f"Scraping {store_configs['store_name']}...")
        results += scraper.scrape_store(store_configs, query, limit)
        print(f"Found {len(results)} products so far")

    return results
