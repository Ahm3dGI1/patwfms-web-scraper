import { FaSearch } from "react-icons/fa";
import React from 'react';

import './SearchHandler.css';


interface SearchHandlerProps {
    searchQuery: string;
    setSearchQuery: (query: string) => void;
    limitValue: string;
    setLimit: (limit: string) => void;
    handleSearch: () => void;
    loading: boolean;
}

const SearchHandler: React.FC<SearchHandlerProps> = ({ searchQuery, setSearchQuery, limitValue, setLimit, handleSearch, loading }) => {

    limitValue = "10";

    return (
        <>
            <div className="search-handler">
                <button onClick={handleSearch} disabled={loading}>
                    <FaSearch color="black" size="20px" />
                </button>
                <input className="search-input" type="text" placeholder="Search for products..." value={searchQuery} onChange={(e) => setSearchQuery(e.target.value)} />
            </div>
            <div className="limit-handler">
                <span>No. of items per store</span>
                <input className="limit-input" type="number" placeholder="10" value={limitValue} onChange={(e) => setLimit(e.target.value)} />
            </div>
            {loading && <p className='loading-screen'>Loading...</p>}
        </>
    );
};

export default SearchHandler;
