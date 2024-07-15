from bs4 import BeautifulSoup
import requests


def scrape_coupang(query, limit, headers):
    # Construct URLs for search results using the user query
    url_base = f'https://www.coupang.com/np/search?component=&q={query.replace(" ", "+")}'

    # Send requests to fetch search results
    response_base = requests.get(url_base, headers=headers)

    if response_base.status_code != 200:
        print(
            f'Failed to fetch Walmart data on response 1: {response_base.status_code}')
        return []

    # Parse HTML content using BeautifulSoup
    soup_base = BeautifulSoup(response_base.text, 'html.parser')

    product_elements = soup_base.select('li', {'class': 'search-product'})

    products = []
    # Extract product details
    for product_element in product_elements:

        title_tag = product_element.select_one('div.name')

        price_tag = product_element.select_one(
            'strong.price-value')

        image_tag = product_element.select_one(
            'img.search-product-wrap-img')

        link_tag = product_element.find('a', class_='search-product-link')

        if not all([title_tag, price_tag, image_tag, link_tag]):
            continue

        product_details = {
            'title': title_tag.text,
            'price': price_tag.text,
            'image': image_tag['src'],
            'url': 'https://www.coupang.com' + link_tag['href'],
            'store': 'Coupang'
        }

        if product_details not in products:
            products.append(product_details)

        if len(products) >= limit:
            break

    return products
