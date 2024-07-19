from bs4 import BeautifulSoup
import requests
import logging


# Some websites require legit headers to be sent in order to get a response while other's work better with fake headers
def fetch_response(url, headers):
    for header in headers:
        response = requests.get(url, headers=header)
        if response.status_code == 200:
            return response
    logging.error(f"Failed to fetch data: {response.status_code}")
    return None


# This function is used to get the first valid element from a list of selectors or a single selector
# Most websites work better with a fake User Agent, but websites like Amazon and Ebay give an error if a fake User Agent
# is used so we need to use a legit User Agent for them
def get_first_valid_element(element, selectors):
    if isinstance(selectors, list):
        for selector in selectors:
            tag = element.select_one(selector)
            if tag:
                return tag
    else:
        return element.select_one(selectors)
    return None


# The main function that scrapes the store based on the store configuration
def scrape_store(store_config, query, limit):
    products = []

    headers = [
        {'User-Agent': 'M'},

        {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Connection': 'keep-alive'
        }
    ]

    url = store_config['base_url'].format(query=query.replace(" ", "+"))
    response = fetch_response(url, headers)

    if not response:
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    product_elements = []

    # Handle multiple selectors for product elements
    product_selectors = store_config['product_selector']
    if isinstance(product_selectors, list):
        for selector in product_selectors:
            product_elements.extend(soup.select(selector))
    else:
        product_elements = soup.select(product_selectors)

    for product_element in product_elements:
        title_tag = get_first_valid_element(
            product_element, store_config['title_selector'])
        price_tag = get_first_valid_element(
            product_element, store_config['price_selector'])
        image_tag = product_element.select_one(store_config['image_selector'])
        link_tag = get_first_valid_element(
            product_element, store_config['link_selector']) or product_element

        # Skip the product if any required element is missing
        if not all([title_tag, price_tag, image_tag, link_tag]):
            continue

        product_details = {
            'title': (title_tag.text.strip()[:120] + '...') if len(title_tag.text.strip()) > 120 else title_tag.text.strip(),
            'price': price_tag.text.strip(),
            'image': image_tag['src'],
            'url': store_config['url_prefix'] + link_tag['href'],
            'store': store_config['store_name']
        }

        if product_details not in products:
            products.append(product_details)

        if len(products) >= limit:
            break

    return products
