from bs4 import BeautifulSoup
import requests


def scrape_target(query):

    title = 0
    price = 0
    image = 0
    link = 0
    # Construct URLs for search results using the user query
    url_base = f'https://www.target.com/s?searchTerm={query.replace(" ", "+")}'
    url_by_price = f'https://www.walmart.com/search?q={query.replace(" ", "+")}&facetedValue=5y6yk&ignoreBrandExactness=true&sortBy=PriceLow&moveTo=product-list-grid'

    # Define headers to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Connection': 'keep-alive'
    }

    # Send requests to fetch search results
    response_base = requests.get(url_base, headers=headers)
    response_by_price = requests.get(url_by_price, headers=headers)

    if response_base.status_code != 200:
        print(
            f'Failed to fetch data on response 1: {response_base.status_code}')
        return None

    if response_by_price.status_code != 200:
        print(
            f'Failed to fetch data on response 2: {response_by_price.status_code}')
        return None

    # Parse HTML content using BeautifulSoup
    soup_base = BeautifulSoup(response_base.text, 'html.parser')
    soup_by_price = BeautifulSoup(response_by_price.text, 'html.parser')

    product_elements = soup_base.select(
        'div.sc-e56884d9-0') + soup_by_price.select('div.sc-e56884d9-0')

    products = []
    # Extract product details
    for product_element in product_elements:

        title_tag = product_element.select_one(
            'a.sc-676073c3-0.sc-e1ae665c-1.fLytdP.bRxnjG.h-display-block.h-text-bold.h-text-bs')

        price_tag = product_element.select_one(
            'div[data-test="@web/ProductCard/ProductCardPrice/Price"]')

        image_tag = product_element.select_one(
            'picture[data-test="@web/ProductCard/ProductCardImage/primary"] img')

        link_tag = product_element.find(
            'a', class_='sc-676073c3-0.fCfUJD.h-display-block')

        if not all([title_tag, price_tag, image_tag, link_tag]):
            continue

        product_details = {
            'title': title_tag.text,
            'price': price_tag.text,
            'image': image_tag['src'],
            'url': 'https://www.target.com' + link_tag['href'],
            'store': 'target'
        }

        products.append(product_details)
    return products
