from scrapers.us import amazon
from scrapers.us import walmart
from scrapers.us import target
from scrapers.us import ebay

from scrapers.korea import coupang
from scrapers.korea import naver
from scrapers.korea import ssg

from scrapers.japan import rakuten
from scrapers.japan import amazon

from scrapers.taiwan import yahoo

from scrapers.india import amazon

from scrapers.argentina import fravega
from scrapers.argentina import mercadolibre

from scrapers.germany import amazon
from scrapers.germany import otto


def scrape(query, country, limit=10):
    if country == 'US':
        return amazon.scrape_amazon(query, limit) + walmart.scrape_walmart(query, limit) + target.scrape_target(query, limit) + ebay.scrape_ebay(query, limit)

    elif country == 'Korea':
        return coupang.scrape_coupang(query, limit) + naver.scrape_naver(query, limit) + ssg.scrape_ssg(query, limit)

    elif country == 'Japan':
        return rakuten.scrape_rakuten(query, limit) + amazon.scrape_amazon(query, limit)

    elif country == 'Taiwan':
        return yahoo.scrape_yahoo(query, limit)

    elif country == 'India':
        return amazon.scrape_amazon(query, limit)

    elif country == 'Argentina':
        return fravega.scrape_fravega(query, limit) + mercadolibre.scrape_mercadolib(query, limit)

    elif country == 'Germany':
        return amazon.scrape_amazon(query, limit) + otto.scrape_otto(query, limit)

    else:
        raise ValueError(f"Country '{country}' is not supported")
