from bs4 import BeautifulSoup
import requests


def scrape_otto(query, limit, headers):
    # Construct URLs for search results using the user query
    url = f'https://www.otto.de/suche/{query.replace(" ", "%20")}'

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f'Failed to fetch Amazon data: {response.status_code}')
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    product_elements = soup.select('article')

    products = []

    # Extract product_details details
    for product_element in product_elements:
        title_tag = product_element.select_one(
            'p', class_='find_tile__name pl_copy100')

        price_whole_tag = product_element.select_one(
            'span', class_='find_tile__priceValue')

        image_tag = product_element.select_one(
            'img', class_='find_tile__productImage')

        link_tag = product_element.select_one(
            'a', class_='find_tile__productLink')

        # Skip product_details if any of the required tags are missing
        if not all([title_tag, price_whole_tag, image_tag, link_tag]):
            continue

        # Combine whole and fractional parts of the price
        price = f"{price_whole_tag.text.strip()}"

        product_details = {
            'title': title_tag.text.strip(),
            'price': price,
            'image': image_tag['src'],
            'url': 'https://www.otto.de' + link_tag['href'],
            'store': 'Otto'
        }

        if len(product_details['title']) > 120:
            product_details['title'] = product_details['title'][:120] + '...'

        if product_details not in products:
            products.append(product_details)

        if len(products) >= limit:
            break

    return products
