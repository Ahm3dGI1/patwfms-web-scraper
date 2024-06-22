from scrapers.us import amazon
from scrapers.us import walmart
from scrapers.us import target
from scrapers.us import ebay


class SORTING:
    RELEVANT = 0
    PRICE = 1


def scrape(query, country, limit=10, sort_by=SORTING.RELEVANT):
    if country == 'us':
        return amazon.scrape_amazon(query) + walmart.scrape_walmart(query) + target.scrape_target(query) + ebay.scrape_ebay(query)

    else:
        raise ValueError(f"Country '{country}' is not supported")
