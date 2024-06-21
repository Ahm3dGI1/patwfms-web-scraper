from bs4 import BeautifulSoup
import requests


def scrape_amazon(query):
    # Construct URLs for search results using the user query
    url = f'https://www.amazon.com/s?k={query.replace(" ", "+")}'

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
        print(f'Failed to fetch data: {response.status_code}')
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    product_elements = soup.select('.s-main-slot .s-result-item')

    print(f"Found {len(product_elements)} product elements.")

    products = []

    # Extract product details
    for product_element in product_elements:
        title_tag = product_element.select_one('span', class_='a-size-medium')

        price_whole_tag = product_element.select_one(
            'span', class_='a-price-whole')

        price_fraction_tag = product_element.select_one(
            'span', class_='a-price-fraction')

        image_tag = product_element.select_one('img', class_='s-image')

        link_tag = product_element.select_one('a', class_='a-link-normal')

        # Skip product if any of the required tags are missing
        if not all([image_tag, title_tag, price_whole_tag, price_fraction_tag, link_tag]):
            continue

        # Combine whole and fractional parts of the price
        price = f"{price_whole_tag.text.strip()}.{price_fraction_tag.text.strip()}"

        product = {
            'image': image_tag['src'],
            'name': title_tag.text.strip(),
            'price': price,
            'url': 'https://www.amazon.com' + link_tag['href'],
            'store': 'Amazon'
        }

        if product['price'] == '':
            product['price'] = 'Not available in stock'

        products.append(product)

    return products
