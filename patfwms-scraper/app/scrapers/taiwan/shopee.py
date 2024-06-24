from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def scrape_shopee(query):
    # Initialize the Selenium WebDriver (using Chrome in this example)
    driver = webdriver.Chrome()  # Make sure to have chromedriver installed and in PATH

    # Construct URLs for search results using the user query
    url_base = f'https://shopee.tw/search?keyword={query.replace(" ", "%20")}'

    driver.get(url_base)

    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.shopee-search-item-result__item')))

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    product_elements = soup.select('.shopee-search-item-result__item')

    products = []
    # Extract product details
    for product_element in product_elements:
        title_tag = product_element.select_one('a span.w_iUH7')
        price_tag = product_element.select_one(
            'div[data-automation-id="product-price"]')
        image_tag = product_element.select_one('img')
        link_tag = product_element.find('a')

        if not all([title_tag, price_tag, image_tag, link_tag]):
            continue

        product_details = {
            'title': title_tag.text,
            'price': price_tag.text,
            'image': image_tag['src'],
            'url': 'https://shopee.tw' + link_tag['href'],
            'store': 'Shopee'
        }

        if product_details not in products:
            products.append(product_details)

    driver.quit()
    return products


print(scrape_shopee('keyboard'))
