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
import CountryProvider from './providers/CountryProvider';



const App: React.FC = () => {
  const [searchQuery, setSearchQuery] = useState<string>('');
  const [products, setProducts] = useState<ProductType[]>([]);
  const [loading, setLoading] = useState<boolean>(false);
  const [checkedStores, setCheckedStores] = useState<string[]>([]);
  const [country, setCountry] = useState<string>('US');

  const handleSearch = async () => {
    setLoading(true);
    setProducts([]);

    try {
      const data = await fetchProducts(searchQuery, country);
      setProducts(data);
    } catch (error) {
      console.error('Error:', error);
    }

    setLoading(false);

  };
  return (
    <Router>
      <CountryProvider setCountry={setCountry} />
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
