from bs4 import BeautifulSoup
import requests


def scrape_amazon(searchText):
    c = 0
    url = f'https://www.amazon.com/s?k={searchText.replace(" ", "+")}'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36", "Accept-Encoding": "gzip, deflate", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print('Failed to fetch data:', response.status_code)
        return None

    soup = BeautifulSoup(response.text, 'lxml')

    products = []
    product_elements = soup.find_all('div', class_='s-result-item')

    for product_element in product_elements:
        image_tag = product_element.find('img', class_='s-image')
        name_tag = product_element.find('span', class_='a-size-medium')
        price_tag = product_element.find('span', class_='a-price')
        url_tag = product_element.find('a', class_='a-link-normal')

        if not all([image_tag, name_tag, price_tag, url_tag]):
            c += 1
            continue

        product = {
            'image': image_tag['src'],
            'name': name_tag.text.strip(),
            'price': price_tag.text.strip(),
            'url': 'https://www.amazon.com' + url_tag['href'],
            'site': 'Amazon'
        }

        if product['price'] == '':
            product['price'] = 'Not available in stock'
        products.append(product)

    print('failed:', c)

    return products


if __name__ == '__main__':
    products = scrape_amazon('Iphone 12')
    print(len(products))
