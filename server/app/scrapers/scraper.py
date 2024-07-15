from bs4 import BeautifulSoup
import requests


def scrape_store(store_config, query, limit, headers):
    """
    Scrapes data from a store based on the provided store configuration.

    Args:
        query (str): The search query for the product.
        limit (int): The maximum number of products to fetch.
        headers (dict): The HTTP headers to use for the request.
        store_config (dict): The configuration for the store from the config file.

    Returns:
        List[dict]: A list of dictionaries with product details.
    """
    url = store_config['base_url'].format(query=query.replace(" ", "+"))
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(
            f"Failed to fetch {store_config['store_name']} data: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    # Handle multiple selectors for product elements
    product_elements = []
    if isinstance(store_config['product_selector'], list):
        for selector in store_config['product_selector']:
            product_elements.extend(soup.select(selector))
    else:
        product_elements = soup.select(store_config['product_selector'])

    products = []

    for product_element in product_elements:
        # Handle multiple selectors for title, price, and link
        title_tag = None
        for selector in (store_config['title_selector'] if isinstance(store_config['title_selector'], list) else [store_config['title_selector']]):
            title_tag = product_element.select_one(selector)
            if title_tag:
                break

        price_tag = None
        for selector in (store_config['price_selector'] if isinstance(store_config['price_selector'], list) else [store_config['price_selector']]):
            price_tag = product_element.select_one(selector)
            if price_tag:
                break

        image_tag = product_element.select_one(store_config['image_selector'])
        link_tag = None
        for selector in (store_config['link_selector'] if isinstance(store_config['link_selector'], list) else [store_config['link_selector']]):
            link_tag = product_element.select_one(selector)
            if link_tag:
                break

        if not all([title_tag, price_tag, image_tag, link_tag]):
            continue

        product_details = {
            'title': title_tag.text.strip(),
            'price': price_tag.text.strip(),
            'image': image_tag['src'],
            'url': store_config['url_prefix'] + link_tag['href'],
            'store': store_config['store_name']
        }

        if len(product_details['title']) > 120:
            product_details['title'] = product_details['title'][:120] + '...'

        if product_details not in products:
            products.append(product_details)

        if len(products) >= limit:
            break

    return products
