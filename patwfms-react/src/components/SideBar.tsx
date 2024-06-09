import React from 'react'
import './SideBar.css'

function SideBar() {
    return (
        <div className="sidebar">
            <div>
                <h2>Stores</h2>
                <div className="store-check">
                    <input type="checkbox" id="amazon" name="amazon" value="amazon" />
                    <span>
                        Amazon
                    </span>
                </div>
                <div className="store-check">
                    <input type="checkbox" id="wallmart" name="wallmart" value="wallmart" />
                    <span>
                        wallmart
                    </span>
                </div><div className="store-check">
                    <input type="checkbox" id="other" name="other" value="other" />
                    <span>
                        other
                    </span>
                </div>
            </div>

            <div className="sort-order">
                <h2>Sort By</h2>
                <select name="sort" id="sort">
                    <option value="price">Price</option>
                    <option value="rating">Rating</option>
                    <option value="popularity">Popularity</option>
                </select>
            </div>
        </div>
    )
}

export default SideBar
