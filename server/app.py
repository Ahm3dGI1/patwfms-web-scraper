from flask import Flask, request, jsonify
from flask_cors import CORS
from scraper_logic import scrape_handler
import logging

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


def validate_request_args(args):
    query = args.get('query')
    country = args.get('country', '').lower()
    limit = args.get('limit')

    if not query:
        return 'No query parameter provided', None, None, None

    if not country:
        return 'No country parameter provided', None, None, None

    try:
        limit = int(limit)
    except (TypeError, ValueError):
        return 'Invalid limit parameter provided', None, None, None

    return None, query, country, limit


@app.route('/scrape', methods=['GET'])
def scrape_endpoint():
    print("Scraping")
    error, query, country, limit = validate_request_args(request.args)

    if error:
        return jsonify({'error': error}), 400

    try:
        products = scrape_handler.scrape(query, country, limit)
        return jsonify(products)
    except Exception as e:
        logging.error(f"Error during scraping: {e}", exc_info=True)
        return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run(debug=True)
