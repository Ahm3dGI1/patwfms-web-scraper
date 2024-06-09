import { FaSearch } from "react-icons/fa";
import React, { useState } from 'react';

import './SearchHandler.css';


interface SearchHandlerProps {
    searchQuery: string;
    setSearchQuery: (query: string) => void;
    handleSearch: () => void;
    loading: boolean;
}

const SearchHandler: React.FC<SearchHandlerProps> = ({ searchQuery, setSearchQuery, handleSearch, loading }) => {

    return (
        <>
            <div className="search-handler">
                <button onClick={handleSearch} disabled={loading}>
                    <FaSearch color="black" size="20px" />
                </button>
                <input type="text" placeholder="Search for products..." value={searchQuery} onChange={(e) => setSearchQuery(e.target.value)} />
            </div>
            {loading && <p className='loading-screen'>Loading...</p>}
        </>
    );
};

export default SearchHandler;
