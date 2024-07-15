from bs4 import BeautifulSoup
import requests


def scrape_mercadolibre(query, limit, headers):
    # Construct URLs for search results using the user query
    url = f'https://listado.mercadolibre.com.ar/{query.replace(" ", "-")}'

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f'Failed to fetch Mercadolibre data: {response.status_code}')
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    product_elements = soup.select('li')

    products = []

    # Extract product_details details
    for product_element in product_elements:
        title_tag = product_element.select_one(
            'h2', class_='ui-search-item__title')

        price_whole_tag = product_element.select_one(
            'span', class_='andes-money-amount__fraction')

        image_tag = product_element.select_one('img', class_='s-image')

        link_tag = product_element.select_one(
            'a', class_='ui-search-link__title-card')

        # Skip product_details if any of the required tags are missing
        if not all([image_tag, title_tag, price_whole_tag, link_tag]):
            continue

        # Combine whole and fractional parts of the price
        price = f"{price_whole_tag.text.strip()}"

        product_details = {
            'title': title_tag.text.strip(),
            'price': price,
            'image': image_tag['src'],
            'url': link_tag['href'],
            'store': 'Mercadolibre'
        }

        if len(product_details['title']) > 120:
            product_details['title'] = product_details['title'][:120] + '...'

        if product_details not in products:
            products.append(product_details)

        if len(products) >= limit:
            break

    return products
