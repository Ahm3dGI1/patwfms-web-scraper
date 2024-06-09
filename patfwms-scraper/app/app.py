# patfwms-scraper/app/app.py

from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from scrapers.amazon import scrape_amazon  # Import the scraping function

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


@app.route('/scrape_amazon', methods=['GET'])
def scrape_amazon_endpoint():
    query = request.args.get('query')
    if not query:
        return jsonify({'error': 'No query parameter provided'}), 400

    products = scrape_amazon(query)
    return jsonify(products)


if __name__ == '__main__':
    app.run(debug=True)
