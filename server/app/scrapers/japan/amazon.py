from bs4 import BeautifulSoup
import requests


def scrape_amazon(query, limit, headers):
    # Construct URLs for search results using the user query
    url = f'https://www.amazon.co.jp/s?k={query.replace(" ", "+")}'

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f'Failed to fetch Amazon data: {response.status_code}')
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    product_elements = soup.select('.s-main-slot .s-result-item')

    products = []

    # Extract product_details details
    for product_element in product_elements:
        title_tag = product_element.select_one('span', class_='a-size-medium')

        price_whole_tag = product_element.select_one(
            'span', class_='a-price-whole')

        image_tag = product_element.select_one('img', class_='s-image')

        link_tag = product_element.select_one('a', class_='a-link-normal')

        # Skip product_details if any of the required tags are missing
        if not all([image_tag, title_tag, price_whole_tag, link_tag]):
            continue

        # Combine whole and fractional parts of the price
        price = f"{price_whole_tag.text.strip()}"

        product_details = {
            'title': title_tag.text.strip(),
            'price': price,
            'image': image_tag['src'],
            'url': 'https://www.amazon.co.jp' + link_tag['href'],
            'store': 'Amazon'
        }

        if len(product_details['title']) > 120:
            product_details['title'] = product_details['title'][:120] + '...'

        if 'SponsoredSponsored You’re seeing this ad based on the' in product_details['title'] or 'Customers frequently viewed' in product_details['title'] or 'Debug info copied.' in product_details['title']:
            continue
        if product_details not in products:
            products.append(product_details)

        if len(products) >= limit:
            break

    return products
