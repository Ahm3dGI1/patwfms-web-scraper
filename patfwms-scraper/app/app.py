from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from scrapers import scraper  # Import the scraping function
import logging


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


@app.route('/scrape', methods=['GET'])
def scrape_amazon_endpoint():
    query = request.args.get('query')
    country = request.args.get('country')

    if not query:
        return jsonify({'error': 'No query parameter provided'}), 400

    if not country:
        return jsonify({'error': 'No country parameter provided'}), 400

    try:
        products = scraper.scrape(query, country)
        return jsonify(products)
    except Exception as e:
        logging.error(f"Error during scraping: {e}")
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
