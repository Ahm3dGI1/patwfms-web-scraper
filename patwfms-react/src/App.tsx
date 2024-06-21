import React, { useState } from 'react';
import { BrowserRouter as Router, useLocation } from 'react-router-dom';

import './App.css';

import SearchHandler from './components/SearchHandler';
import ProductsGrid from './components/ProductGrid';
import { fetchProducts } from './components/api';
import { ProductType } from './components/Product';
import StoreCheck from './components/StoreCheck';
import NavBar from './components/NavBar';
import RouterComponent from './providers/Router';


const App: React.FC = () => {
  const [searchQuery, setSearchQuery] = useState<string>('');
  const [products, setProducts] = useState<ProductType[]>([]);
  const [loading, setLoading] = useState<boolean>(false);
  const [checkedStores, setCheckedStores] = useState<string[]>([]);

  const location = useLocation();

  const getCountryFromPath = () => {
    const path = location.pathname;
    switch (path) {
      case '/taiwan':
        return 'Taiwan';
      case '/korea':
        return 'Korea';
      case '/argentina':
        return 'Argentina';
      case '/india':
        return 'India';
      case '/germany':
        return 'Germany';
      case '/japan':
        return 'Japan';
      default:
        return 'US';
    }
  };

  const country = getCountryFromPath();

  const handleSearch = async () => {
    setLoading(true);
    setProducts([]);

    try {
      const data = await fetchProducts(searchQuery, country);
      setProducts(data);
    } catch (error) {
      console.error('Error:', error);
    }

    setProducts([
      {
        image: 'https://m.media-amazon.com/images/I/71zny7BTRlL._AC_UL320_.jpg',
        name: 'Apple AirPods Pro',
        price: '$197.00',
        url: 'https://www.amazon.com/Apple-AirPods-Pro/dp/B07ZPC9QD4',
        site: 'Amazon',
      },
      {
        image: 'https://m.media-amazon.com/images/I/71zny7BTRlL._AC_UL320_.jpg',
        name: 'Apple AirPods with Charging Case',
        price: '$128.98',
        url: 'https://www.amazon.com/Apple-AirPods-Charging-Latest-Model/dp/B07PXGQC1Q',
        site: 'Amazon',
      },
      {
        image: 'https://m.media-amazon.com/images/I/71zny7BTRlL._AC_UL320_.jpg',
        name: 'Apple AirPods with Charging Case',
        price: '$128.98',
        url: 'https://www.amazon.com/Apple-AirPods-Charging-Latest-Model/dp/B07PXGQC1Q',
        site: 'Amazon',
      },
      {
        image: 'https://m.media-amazon.com/images/I/71zny7BTRlL._AC_UL320_.jpg',
        name: 'Apple AirPods with Charging Case',
        price: '$128.98',
        url: 'https://www.amazon.com/Apple-AirPods-Charging-Latest-Model/dp/B07PXGQC1Q',
        site: 'Other',
      },
      {
        image: 'https://m.media-amazon.com/images/I/71zny7BTRlL._AC_UL320_.jpg',
        name: 'Apple AirPods with Charging Case',
        price: '$128.98',
        url: 'https://www.amazon.com/Apple-AirPods-Charging-Latest-Model/dp/B07PXGQC1Q',
        site: 'Other',
      },
      {
        image: 'https://m.media-amazon.com/images/I/71zny7BTRlL._AC_UL320_.jpg',
        name: 'Apple AirPods with Charging Case',
        price: '$128.98',
        url: 'https://www.amazon.com/Apple-AirPods-Charging-Latest-Model/dp/B07PXGQC1Q',
        site: 'Other',
      },
      {
        image: 'https://m.media-amazon.com/images/I/71zny7BTRlL._AC_UL320_.jpg',
        name: 'Apple AirPods with Charging Case',
        price: '$128.98',
        url: 'https://www.amazon.com/Apple-AirPods-Charging-Latest-Model/dp/B07PXGQC1Q',
        site: 'Amazon',
      },
      {
        image: 'https://m.media-amazon.com/images/I/71zny7BTRlL._AC_UL320_.jpg',
        name: 'Apple AirPods with Charging Case',
        price: '$128.98',
        url: 'https://www.amazon.com/Apple-AirPods-Charging-Latest-Model/dp/B07PXGQC1Q',
        site: 'Walmart',
      },
      {
        image: 'https://m.media-amazon.com/images/I/71zny7BTRlL._AC_UL320_.jpg',
        name: 'Apple AirPods with Charging Case',
        price: '$128.98',
        url: 'https://www.amazon.com/Apple-AirPods-Charging-Latest-Model/dp/B07PXGQC1Q',
        site: 'Walmart',
      },
      {
        image: 'https://m.media-amazon.com/images/I/71zny7BTRlL._AC_UL320_.jpg',
        name: 'Apple AirPods with Charging Case',
        price: '$128.98',
        url: 'https://www.amazon.com/Apple-AirPods-Charging-Latest-Model/dp/B07PXGQC1Q',
        site: 'Walmart',
      },
      {
        image: 'https://m.media-amazon.com/images/I/71zny7BTRlL._AC_UL320_.jpg',
        name: 'Apple AirPods with Charging Case',
        price: '$128.98',
        url: 'https://www.amazon.com/Apple-AirPods-Charging-Latest-Model/dp/B07PXGQC1Q',
        site: 'Walmart',
      }
    ]);

    setLoading(false);

  };
  return (
    <Router>
      <div className="App">
        <header className="header-container">
          <NavBar />
          <RouterComponent />
          <SearchHandler
            searchQuery={searchQuery}
            setSearchQuery={setSearchQuery}
            handleSearch={handleSearch}
            loading={loading}
          />
          <div className="web-title">
            <span>P</span>rices <span>A</span>cross <span>T</span>he <span>W</span>orld <span>F</span>or <span>M</span>inerva <span>S</span>tudents
          </div>
          <div className="hum">cuz we are traveling like crazy</div>
        </header>
        <div className='main-container'>
          <StoreCheck checkedStores={checkedStores} setCheckedStores={setCheckedStores} country={country} />
          <ProductsGrid products={products} checkedStores={checkedStores} />
        </div>
      </div>
    </Router>
  );
};

export default App;
