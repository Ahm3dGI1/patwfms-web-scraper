from bs4 import BeautifulSoup
import requests


def scrape_target(query, limit, headers):
    # Construct URLs for search results using the user query
    url_base = f'https://www.target.com/s?searchTerm={query.replace(" ", "+")}'

    # Send requests to fetch search results
    response_base = requests.get(url_base, headers=headers)

    if response_base.status_code != 200:
        print(
            f'Failed to fetch Target data on response 1: {response_base.status_code}')
        return []

    # Parse HTML content using BeautifulSoup
    soup_base = BeautifulSoup(response_base.text, 'html.parser')

    product_elements = soup_base.select('div.sc-e56884d9-0')

    products = []
    # Extract product details
    for product_element in product_elements:

        title_tag = product_element.select_one(
            'a.sc-676073c3-0.sc-e1ae665c-1.fLytdP.bRxnjG.h-display-block.h-text-bold.h-text-bs')

        price_tag = product_element.select_one(
            'div[data-test="@web/ProductCard/ProductCardPrice/Price"]')

        image_tag = product_element.select_one(
            'picture[data-test="@web/ProductCard/ProductCardImage/primary"] img')

        link_tag = product_element.find(
            'a', class_='sc-676073c3-0.fCfUJD.h-display-block')

        if not all([title_tag, price_tag, image_tag, link_tag]):
            continue

        product_details = {
            'title': title_tag.text,
            'price': price_tag.text,
            'image': image_tag['src'],
            'url': 'https://www.target.com' + link_tag['href'],
            'store': 'Target'
        }

        if len(product_details['title']) > 120:
            product_details['title'] = product_details['title'][:120] + '...'

        if product_details not in products:
            products.append(product_details)

        if len(products) >= limit:
            break

    return products
