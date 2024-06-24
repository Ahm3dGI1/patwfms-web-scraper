# Prices Across The World For Minerva Students (PATWFMS)

Welcome to the Prices Across The World For Minerva Students (PATWFMS) project! This application allows Minerva students to compare product prices across different countries, making it easier for them to make informed purchasing decisions while traveling.

## Table of Contents

- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Scraper Functions](#scraper-functions)
- [Client Application](#client-application)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

PATWFMS-WEB-SCRAPER
├── patwfms-scraper
│   ├── app
│   │   ├── scrapers
│   │   │   ├── argentina
│   │   │   ├── germany
│   │   │   ├── india
│   │   │   ├── japan
│   │   │   ├── korea
│   │   │   ├── taiwan
│   │   │   ├── us
│   │   │   │   ├── amazon.py
│   │   │   │   ├── bestbuy.py
│   │   │   │   ├── ebay.py
│   │   │   │   ├── target.py
│   │   │   │   ├── walmart.py
│   │   │   │   ├── __init__.py
│   │   │   ├── scraper.py
│   │   │   ├── __pycache__
│   │   ├── app.py
├── requirements.txt
├── patwfms-react
│   ├── node_modules
│   ├── src
│   │   ├── components
│   │   │   ├── api.ts
│   │   │   ├── NavBar.css
│   │   │   ├── NavBar.tsx
│   │   │   ├── Product.css
│   │   │   ├── Product.tsx
│   │   │   ├── ProductGrid.tsx
│   │   │   ├── SearchHandler.css
│   │   │   ├── SearchHandler.tsx
│   │   │   ├── StoreCheck.css
│   │   │   ├── StoreCheck.tsx
│   │   ├── providers
│   │   │   ├── CountryProvider.tsx
│   │   │   ├── Router.tsx
│   │   ├── App.css
│   │   ├── App.tsx
│   │   ├── main.tsx
│   │   ├── vite-env.d.ts
│   ├── .eslintrc.cjs
│   ├── .gitignore
│   ├── index.html
│   ├── package-lock.json
│   ├── package.json
│   ├── README.md
│   ├── tsconfig.json
│   ├── tsconfig.node.json
│   ├── vite.config.ts
├── venv
├── README.md
