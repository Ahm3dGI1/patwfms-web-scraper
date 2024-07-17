from bs4 import BeautifulSoup
import requests


def scrape_store(store_config, query, limit):
    product_elements = []
    products = []

    headers = [
        {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
         'Accept-Language': 'en-US,en;q=0.9',
         'Accept-Encoding': 'gzip, deflate, br',
         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
         'Connection': 'keep-alive'},

        {'User-Agent': 'M'}
    ]

    for i in range(2):
        url = store_config['base_url'].format(query=query.replace(" ", "+"))

        response = requests.get(url, headers=headers[i])

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

            image_tag = product_element.select_one(
                store_config['image_selector'])

            link_tag = None
            if not store_config['link_selector']:
                link_tag = product_element
            else:
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
