from us.amazon import scrape_amazon
from us.walmart import scrape_walmart


def scrape(query):
    return scrape_amazon(query) + scrape_walmart(query)
