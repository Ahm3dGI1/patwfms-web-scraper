from bs4 import BeautifulSoup
import requests


def scrape_mercadolibre(query, limit):
    # Construct URLs for search results using the user query
    url = f'https://listado.mercadolibre.com.ar/{query.replace(" ", "-")}'

    # Define headers to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Connection': 'keep-alive'
    }

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
