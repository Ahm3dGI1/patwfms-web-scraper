from bs4 import BeautifulSoup
import requests


def scrape_walmart(query):
    # Construct URLs for search results using the user query
    url_base = f'https://www.walmart.com/search?q={query.replace(" ", "%20")}'
    url_by_price = f'https://www.walmart.com/search?q={query.replace(" ", "%20")}&sort=price_low'

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
            f'Failed to fetch Walmart data on response 1: {response_base.status_code}')
        return []

    if response_by_price.status_code != 200:
        print(
            f'Failed to fetch Walmart data on response 2: {response_by_price.status_code}')
        return []

    # Parse HTML content using BeautifulSoup
    soup_base = BeautifulSoup(response_base.text, 'html.parser')
    soup_by_price = BeautifulSoup(response_by_price.text, 'html.parser')

    product_elements = soup_base.select(
        'div', {'class': 'h-100 pr4-xl'}) + soup_by_price.select('div', {'class': 'h-100 pr4-xl'})

    products = []
    # Extract product details
    for product_element in product_elements:

        title_tag = product_element.select_one('a span.w_iUH7')

        price_tag = product_element.select_one(
            'div[data-automation-id="product-price"]')

        image_tag = product_element.select_one(
            'img[data-testid="productTileImage"]')

        link_tag = product_element.find('a', class_='hide-sibling-opacity')

        if not all([title_tag, price_tag, image_tag, link_tag]):
            continue

        product_details = {
            'title': title_tag.text,
            'price': price_tag.text,
            'image': image_tag['src'],
            'url': 'https://www.walmart.com' + link_tag['href'],
            'store': 'Walmart'
        }

        if product_details not in products:
            products.append(product_details)

    return products
