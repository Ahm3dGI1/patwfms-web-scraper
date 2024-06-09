import './NavBar.css';

function NavBar() {
    return (
        <nav className="nav-bar">
            <div className='logo'>PATWFMS</div>
            <ul className='nav-list'>
                <li className='nav-item'><a href="/">US</a></li>
                <li className='nav-item'><a href="/taiwan">Taiwan</a></li>
                <li className='nav-item'><a href="/korea">Korea</a></li>
                <li className='nav-item'><a href="/argentina">Argentina</a></li>
                <li className='nav-item'><a href="/india">India</a></li>
                <li className='nav-item'><a href="/germany">Germany</a></li>
                <li className='nav-item'><a href="/japan">Japan</a></li>
            </ul>
        </nav>
    );
}

export default NavBar;