from bs4 import BeautifulSoup
import requests


def scrape_walmart(query, limit, headers):
    # Construct URLs for search results using the user query
    url_base = f'https://www.walmart.com/search?q={query.replace(" ", "%20")}'

    # Send requests to fetch search results
    response_base = requests.get(url_base, headers=headers)

    if response_base.status_code != 200:
        print(
            f'Failed to fetch Walmart data on response 1: {response_base.status_code}')
        return []

    # Parse HTML content using BeautifulSoup
    soup_base = BeautifulSoup(response_base.text, 'html.parser')

    product_elements = soup_base.select('div', {'class': 'h-100 pr4-xl'})

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

        if len(product_details['title']) > 120:
            product_details['title'] = product_details['title'][:120] + '...'

        if product_details not in products:
            products.append(product_details)

        if len(products) >= limit:
            break

    return products