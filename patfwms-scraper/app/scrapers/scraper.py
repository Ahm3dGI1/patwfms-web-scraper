from scrapers.us import amazon
from scrapers.us import walmart
from scrapers.us import target
from scrapers.us import ebay

from scrapers.korea import coupang
from scrapers.korea import naver


class SORTING:
    RELEVANT = 0
    PRICE = 1


def scrape(query, country, limit=10, sort_by=SORTING.RELEVANT):
    if country == 'US':
        return amazon.scrape_amazon(query) + walmart.scrape_walmart(query) + target.scrape_target(query) + ebay.scrape_ebay(query)

    elif country == 'Korea':
        return coupang.scrape_coupang(query) + naver.scrape_naver(query)

    else:
        raise ValueError(f"Country '{country}' is not supported")
