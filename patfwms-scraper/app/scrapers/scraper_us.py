from us.amazon import scrape_amazon
from us.walmart import scrape_walmart
from us.target import scrape_target
from us.ebay import scrape_ebay


def scrape(query):
    return scrape_amazon(query) + scrape_walmart(query) + scrape_target(query) + scrape_ebay(query)
