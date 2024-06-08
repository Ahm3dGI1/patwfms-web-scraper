from bs4 import BeautifulSoup
import requests
import time
import random


def scrape_amazon(search_text):
    """
    Scrapes Amazon search results for the given search text and returns product details.

    Args:
        search_text (str): The text to search for on Amazon.

    Returns:
        list: A list of dictionaries containing product details.
    """

    url = f'https://www.amazon.com/s?k={search_text.replace(" ", "+")}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Connection': 'keep-alive'
    }

    retries = 5
    for attempt in range(retries):
        response = requests.get(url, headers=headers)

        # Retry on 503 Service Unavailable
        if response.status_code == 503:
            print(
                f"Received 503, retrying... (Attempt {attempt + 1}/{retries})")
            time.sleep(random.uniform(5, 10))  # Random delay before retrying
            continue
        elif response.status_code != 200:
            print(f'Failed to fetch data: {response.status_code}')
            return None

        soup = BeautifulSoup(response.text, 'html.parser')
        products = []
        product_elements = soup.select('.s-main-slot .s-result-item')

        print(f"Found {len(product_elements)} product elements.")

        if not product_elements:
            print('No products found')
            return products

        # Extract product details
        for product_element in product_elements:
            image_tag = product_element.find('img', class_='s-image')
            name_tag = product_element.find('span', class_='a-size-medium')
            price_whole_tag = product_element.find(
                'span', class_='a-price-whole')
            price_fraction_tag = product_element.find(
                'span', class_='a-price-fraction')
            url_tag = product_element.find('a', class_='a-link-normal')

            # Skip product if any of the required tags are missing
            if not all([image_tag, name_tag, price_whole_tag, price_fraction_tag, url_tag]):
                continue

            # Combine whole and fractional parts of the price
            price = f"{price_whole_tag.text.strip()}.{price_fraction_tag.text.strip()}"

            product = {
                'image': image_tag['src'],
                'name': name_tag.text.strip(),
                'price': price,
                'url': 'https://www.amazon.com' + url_tag['href'],
                'site': 'Amazon'
            }

            if product['price'] == '':
                product['price'] = 'Not available in stock'

            products.append(product)

        return products

    print("Max retries reached. Could not fetch data.")
    return None
