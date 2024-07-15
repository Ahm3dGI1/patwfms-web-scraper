from bs4 import BeautifulSoup
import requests


def scrape_fravega(query, limit, headers):
    # Construct URLs for search results using the user query
    url = f'https://www.fravega.com/l/?keyword={query.replace(" ", "+")}'

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f'Failed to fetch Fravega data: {response.status_code}')
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    product_elements = soup.select('li')

    products = []

    # Extract product_details details
    for product_element in product_elements:
        title_tag = product_element.select_one(
            'span', class_='sc-ca346929-0')

        price_whole_tag = product_element.select_one(
            'span', class_='sc-1d9b1d9e-0')

        image_tag = product_element.select_one('img', class_='')

        link_tag = product_element.select_one(
            'a', class_='sc-812c6cb5-0')

        # Skip product_details if any of the required tags are missing
        if not all([image_tag, title_tag, price_whole_tag, link_tag]):
            continue

        # Combine whole and fractional parts of the price
        price = f"{price_whole_tag.text.strip()}"

        product_details = {
            'title': title_tag.text.strip(),
            'price': price,
            'image': image_tag['src'],
            'url': 'https://www.fravega.com/' + link_tag['href'],
            'store': 'Fravega'
        }

        if len(product_details['title']) > 120:
            product_details['title'] = product_details['title'][:120] + '...'

        if product_details not in products:
            products.append(product_details)

        if len(products) >= limit:
            break

    return products
