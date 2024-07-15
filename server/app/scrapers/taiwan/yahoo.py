from bs4 import BeautifulSoup
import requests


def scrape_yahoo(query, limit, headers):
    # Construct URLs for search results using the user query
    url_base = f'https://tw.buy.yahoo.com/search/product?p={query.replace(" ", "+")}'

    # Send requests to fetch search results
    response_base = requests.get(url_base, headers=headers)

    if response_base.status_code != 200:
        print(
            f'Failed to fetch Walmart data on response 1: {response_base.status_code}')
        return []

    # Parse HTML content using BeautifulSoup
    soup_base = BeautifulSoup(response_base.text, 'html.parser')

    product_elements = soup_base.select('a', class_='sc-1drl28c-1')

    products = []
    # Extract product details
    for product_element in product_elements:

        title_tag = product_element.select_one('span', class_='.jZWZIY')

        price_tag = product_element.select_one(
            'span', class_='.hFXgfs')

        image_tag = product_element.select_one(
            'img', class_='.sc-knMnYM')

        link_tag = product_element

        if not all([title_tag, price_tag, image_tag, link_tag]):
            continue

        product_details = {
            'title': title_tag.text,
            'price': price_tag.text,
            'image': image_tag['src'],
            'url': link_tag['href'],
            'store': 'Yahoo'
        }

        if product_details not in products:
            products.append(product_details)

        if len(products) >= limit:
            break

    return products
