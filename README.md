# Prices Across The World For Minerva Students (PATWFMS)

Welcome to the Prices Across The World For Minerva Students (PATWFMS) project! This application allows Minerva students to compare product prices across different countries, making it easier for them to make informed purchasing decisions while traveling.

## Table of Contents

- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)

## Project Structure

PATWFMS-WEB-SCRAPER
<br>├── patwfms-scraper
<br>│   ├── app
<br>│   │   ├── scrapers
<br>│   │   │   ├── argentina
<br>│   │   │   ├── germany
<br>│   │   │   ├── india
<br>│   │   │   ├── japan
<br>│   │   │   ├── korea
<br>│   │   │   ├── taiwan
<br>│   │   │   ├── us
<br>│   │   │   │   ├── amazon.py
<br>│   │   │   │   ├── bestbuy.py
<br>│   │   │   │   ├── ebay.py
<br>│   │   │   │   ├── target.py
<br>│   │   │   │   ├── walmart.py
<br>│   │   │   │   ├── __init__.py
<br>│   │   │   ├── scraper.py
<br>│   │   │   ├── __pycache__
<br>│   │   ├── app.py
<br>├── requirements.txt
<br>├── patwfms-react
<br>│   ├── node_modules
<br>│   ├── src
<br>│   │   ├── components
<br>│   │   │   ├── api.ts
<br>│   │   │   ├── NavBar.css
<br>│   │   │   ├── NavBar.tsx
<br>│   │   │   ├── Product.css
<br>│   │   │   ├── Product.tsx
<br>│   │   │   ├── ProductGrid.tsx
<br>│   │   │   ├── SearchHandler.css
<br>│   │   │   ├── SearchHandler.tsx
<br>│   │   │   ├── StoreCheck.css
<br>│   │   │   ├── StoreCheck.tsx
<br>│   │   ├── providers
<br>│   │   │   ├── CountryProvider.tsx
<br>│   │   │   ├── Router.tsx
<br>│   │   ├── App.css
<br>│   │   ├── App.tsx
<br>│   │   ├── main.tsx
<br>│   │   ├── vite-env.d.ts
<br>│   ├── .eslintrc.cjs
<br>│   ├── .gitignore
<br>│   ├── index.html
<br>│   ├── package-lock.json
<br>│   ├── package.json
<br>│   ├── README.md
<br>│   ├── tsconfig.json
<br>│   ├── tsconfig.node.json
<br>│   ├── vite.config.ts
<br>├── venv
<br>├── README.md


## Setup and Installation

### Backend Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/PATWFMS-WEB-SCRAPER.git
   cd PATWFMS-WEB-SCRAPER/patwfms-scraper
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
   
4. **Run the Flask application:**

   ```bash
   cd app
   python app.py
   ```

### Frontend Setup
1. **Navigate to the React application directory:**

   ```bash
   cd patwfms-react
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

2. Use the search bar to enter a product name and select a country.

3. View and compare the product prices across different stores in the selected country.

## API Endpoints

### `/scrape`
- **Method:** GET
- **Description:** Scrapes product data from different stores based on the query and country parameters.
- **Parameters:**
  - `query` (required): The search query for the product.
  - `country` (required): The country code (e.g., "US", "IN").

#### Example Request:
```bash
curl "http://localhost:5000/scrape?query=laptop&country=US"
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
