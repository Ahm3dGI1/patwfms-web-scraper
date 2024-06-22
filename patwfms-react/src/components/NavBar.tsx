import React from 'react';
import { NavLink, useLocation } from 'react-router-dom';
import './NavBar.css';

function NavBar() {
    const location = useLocation();

    const getActiveCountry = () => {
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

    return (
        <nav className="nav-bar">
            <div className='logo'>PATWFMS</div>
            <ul className='nav-list'>
                <li className='nav-item'>
                    <NavLink to="/" className={({ isActive }) => isActive ? 'active' : undefined}>US</NavLink>
                </li>
                <li className='nav-item'>
                    <NavLink to="/taiwan" className={({ isActive }) => isActive ? 'active' : undefined}>Taiwan</NavLink>
                </li>
                <li className='nav-item'>
                    <NavLink to="/korea" className={({ isActive }) => isActive ? 'active' : undefined}>Korea</NavLink>
                </li>
                <li className='nav-item'>
                    <NavLink to="/argentina" className={({ isActive }) => isActive ? 'active' : undefined}>Argentina</NavLink>
                </li>
                <li className='nav-item'>
                    <NavLink to="/india" className={({ isActive }) => isActive ? 'active' : undefined}>India</NavLink>
                </li>
                <li className='nav-item'>
                    <NavLink to="/germany" className={({ isActive }) => isActive ? 'active' : undefined}>Germany</NavLink>
                </li>
                <li className='nav-item'>
                    <NavLink to="/japan" className={({ isActive }) => isActive ? 'active' : undefined}>Japan</NavLink>
                </li>
            </ul>
        </nav>
    );
}

export default NavBar;
