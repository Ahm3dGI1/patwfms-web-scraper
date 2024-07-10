from bs4 import BeautifulSoup
import requests


def scrape_naver(query, limit):
    # Construct URLs for search results using the user query
    url_base = f'https://search.shopping.naver.com/search/all?query={query.replace(" ", "%20")}'

    # Use any browser's user agent to bypass 418 "I'm a teapot" status code
    headers = {
        'User-Agent': 'M',
    }

    # Send requests to fetch search results
    response_base = requests.get(url_base, headers=headers)

    if response_base.status_code != 200:
        print(
            f'Failed to fetch Walmart data on response 1: {response_base.status_code}')
        return []

    # Parse HTML content using BeautifulSoup
    soup_base = BeautifulSoup(response_base.text, 'html.parser')

    product_elements = soup_base.select(
        'div', {'class': 'adProduct_item__1zC9h'}) + soup_base.select('div', {'class': 'product_item__MDtDF'})

    products = []
    # Extract product details
    for product_element in product_elements:

        title_tag = product_element.select_one('.product_link__TrAac')
        if not title_tag:
            title_tag = product_element.select_one('.adProduct_link__NYTV9')

        price_tag = product_element.select_one(
            '.price_num__S2p_v em')

        image_tag = product_element.select_one(
            'img')

        link_tag = product_element.select_one('.product_link__TrAac')

        if not link_tag:
            link_tag = product_element.select_one('.adProduct_link__NYTV9')

        if not all([title_tag, price_tag, image_tag, link_tag]):
            continue

        product_details = {
            'title': title_tag.text,
            'price': price_tag.text,
            'image': image_tag['src'],
            'url': link_tag['href'],
            'store': 'Naver'
        }

        if product_details not in products:
            products.append(product_details)

        if len(products) >= limit:
            break

    return products
