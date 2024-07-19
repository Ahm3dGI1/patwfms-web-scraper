# Prices Across The World For Minerva Students (PATWFMS)

Welcome to the Prices Across The World For Minerva Students (PATWFMS) project! This application allows Minerva students to compare product prices across different countries, making it easier for them to make informed purchasing decisions while traveling.

## Table of Contents

- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)


## Setup and Installation

### Backend Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Ahm3dGI1/PATWFMS-WEB-SCRAPER.git
   cd PATWFMS-WEB-SCRAPER/server
   ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure stores.json:**

   Ensure the stores.json file is correctly populated with the necessary store configurations.

   Json sample:
   ```json
   {
      "countries":{
         "us":{
            "stores":{
               "amazon": {
                  "store_name": "Amazon",
                  "base_url": "https://www.amazon.com/s?k={query}",
                  "product_selector": "div.s-result-item",
                  "title_selector": "span.a-size-medium",
                  "price_selector": "span.a-offscreen",
                  "image_selector": "img.s-image",
                  "link_selector": "a.a-link-normal",
                  "url_prefix": "https://www.amazon.com"
               }
            }
         }
      }
   }
   ```
   
5. **Run the Flask application:**

   ```bash
   cd app
   python app.py
   ```

### Frontend Setup
1. **Navigate to the React application directory:**

   ```bash
   cd client
   ```

2. **Install the required packages:**

    ```bash
    npm install
    ```

3. **Run the React application:**

   ```bash
   npm run dev
   ```

## Usage

1. Open your browser and go to http://localhost:5173.

2. Use the search bar to enter a product name, select the maximum number of products from each store, and select a country.

3. View and compare the product prices across different stores in the selected country.

## API Endpoints

### `/scrape`
- **Method:** GET
- **Description:** Scrapes product data from different stores based on the query and country parameters.
- **Parameters:**
  - `query` (required): The search query for the product.
  - `country` (required): The country code (e.g., "US", "IN").
  - `limit` (required): number of products per store.

#### Example Request:
```bash
curl "http://localhost:5000/scrape?query=laptop&country=US&limit=10"
```
#### Example Response

```json
[
  {
    "title": "Example Product",
    "price": "$999.99",
    "image": "https://example.com/product.jpg",
    "url": "https://example.com/product",
    "store": "Amazon"
  }
]
```

## Contributing

We welcome contributions from the community! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.
