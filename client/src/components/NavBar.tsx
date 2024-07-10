import { NavLink } from 'react-router-dom';
import './NavBar.css';

function NavBar() {

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
