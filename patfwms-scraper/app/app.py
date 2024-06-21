# patfwms-scraper/app/app.py

from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from scrapers.scrapeManager import scrape  # Import the scraping function

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


@app.route('/scrape', methods=['GET'])
def scrape_amazon_endpoint():
    query = request.args.get('query')
    country = request.args.get('country')
    if not query:
        return jsonify({'error': 'No query parameter provided'}), 400

    products = scrape(country, query)
    return jsonify(products)


if __name__ == '__main__':
    app.run(debug=True)
