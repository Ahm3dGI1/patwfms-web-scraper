from bs4 import BeautifulSoup
import requests


def scrape_ebay(query, limit, headers):
    # Construct URLs for search results using the user query
    url_base = f'https://www.ebay.com/sch/i.html?_from=R40&_nkw={query.replace(" ", "+")}'

    # Send requests to fetch search results
    response_base = requests.get(url_base, headers=headers)

    if response_base.status_code != 200:
        print(
            f'Failed to fetch Ebay data on response 1: {response_base.status_code}')
        return []

    # Parse HTML content using BeautifulSoup
    soup_base = BeautifulSoup(response_base.text, 'html.parser')

    product_elements = soup_base.select(
        'li', {'class': 's-item__wrapper'})

    products = []
    # Extract product details
    for product_element in product_elements:

        title_tag = product_element.select_one('div.s-item__title span')

        price_tag = product_element.select_one('span.s-item__price')

        image_tag = product_element.select_one('img')

        link_tag = product_element.find('a', class_='s-item__link')

        if not all([title_tag, price_tag, image_tag, link_tag]):
            continue

        product_details = {
            'title': title_tag.text,
            'price': price_tag.text,
            'image': image_tag['src'],
            'url': link_tag['href'],
            'store': 'Ebay'
        }

        if product_details['title'] == 'Shop on eBay':
            continue

        if len(product_details['title']) > 120:
            product_details['title'] = product_details['title'][:120] + '...'

        if product_details not in products:
            products.append(product_details)

        if len(products) >= limit:
            break

    return products
