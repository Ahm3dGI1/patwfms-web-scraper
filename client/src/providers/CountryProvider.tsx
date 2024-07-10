import React from 'react';
import { useLocation } from 'react-router-dom';

interface CountryProviderProps {
    setCountry: (country: string) => void;
}

const CountryProvider: React.FC<CountryProviderProps> = ({ setCountry }) => {
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

    React.useEffect(() => {
        const country = getCountryFromPath();
        setCountry(country);
    }, [location]);

    return null;
};

export default CountryProvider;