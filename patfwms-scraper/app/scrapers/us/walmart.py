from bs4 import BeautifulSoup
import requests


def scrape_walmart(query):
    # Construct URLs for search results using the user query
    url1 = f'https://www.walmart.com/search?q={query.replace(" ", "%20")}'
    url2 = f'https://www.walmart.com/search?q={query.replace(" ", "%20")}&sort=price_low'

    # Define headers to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Connection': 'keep-alive'
    }

    # Send requests to fetch search results
    response1 = requests.get(url1, headers=headers)
    response2 = requests.get(url2, headers=headers)

    if response1.status_code != 200:
        print(f'Failed to fetch data on response 1: {response1.status_code}')
        return None

    if response2.status_code != 200:
        print(f'Failed to fetch data on response 2: {response2.status_code}')
        return None

    # Parse HTML content using BeautifulSoup
    soup1 = BeautifulSoup(response1.text, 'html.parser')
    soup2 = BeautifulSoup(response2.text, 'html.parser')

    product_elements = soup1.select(
        'div', {'class': 'h-100 pr4-xl'}) + soup2.select('div', {'class': 'h-100 pr4-xl'})

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

        products.append(product_details)

    return products
