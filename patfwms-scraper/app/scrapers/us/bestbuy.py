from bs4 import BeautifulSoup
import requests


def scrape_bestbuy(query):
    # Construct URLs for search results using the user query
    url_base = f'https://www.bestbuy.com/site/searchpage.jsp?st={query.replace(" ", "+")}'
    url_by_price = f'https://www.bestbuy.com/site/searchpage.jsp?id=pcat17071&sp=%2Bcurrentprice%20skuidsaas&st={query.replace(" ", "+")}'

    # Define headers to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Connection': 'keep-alive'
    }

    # Send requests to fetch search results
    response_base = requests.get(url_base, headers=headers)
    response_by_price = requests.get(url_by_price, headers=headers)

    if response_base.status_code != 200:
        print(
            f'Failed to fetch data on response_base: {response_base.status_code}')
        return None

    if response_by_price.status_code != 200:
        print(
            f'Failed to fetch data on response_by_price: {response_by_price.status_code}')
        return None

    # Parse HTML content using BeautifulSoup
    soup_base = BeautifulSoup(response_base.text, 'html.parser')
    soup_by_price = BeautifulSoup(response_by_price.text, 'html.parser')

    product_elements = soup_base.select(
        'div', {'class': 'embedded-sku'}) + soup_by_price.select('div', {'class': 'embedded-sku'})

    print(len(product_elements))

    products = []
    # Extract product details
    for product_element in product_elements:

        title_tag = product_element.select_one('h4', {'class': 'sku-title'})

        price_tag = product_element.select_one(
            'div', class_='priceView-hero-price priceView-customer-price')

        image_tag = product_element.select_one(
            'img', class_="product-image")

        link_tag = product_element.select_one('a', class_='image-link')

        if not all([title_tag, price_tag, image_tag, link_tag]):
            continue

        product_details = {
            'title': title_tag.text,
            'price': price_tag.text,
            'image': image_tag['src'],
            'url': 'https://www.walmart.com' + link_tag['href'],
            'store': 'Walmart'
        }

        products.append(product_details)

    return products


print(scrape_bestbuy('logitech keyboard')[-1])
