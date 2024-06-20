import React, { ChangeEvent } from 'react'
import './StoreCheck.css'



interface StoreCheckProps {
    checkedStores: string[];
    setCheckedStores: React.Dispatch<React.SetStateAction<string[]>>;
}


const StoreCheck: React.FC<StoreCheckProps> = ({ checkedStores, setCheckedStores }) => {

    let stores = ['Amazon', 'Walmart', 'Best Buy', 'Target', 'Other']

    const handleCheck = (store: string) => {
        if (checkedStores.includes(store)) {
            setCheckedStores(checkedStores.filter(product => product !== store));
        } else {
            setCheckedStores([...checkedStores, store]);
        }
    };

    return (
        <div className="sidebar">
            <div>
                <h2>Stores</h2>
                {stores.map((store, index) => (
                    <div className="store-check">
                        <input
                            onClick={() => handleCheck(store)}
                            type="checkbox"
                            id={store}
                        />
                        <span>
                            {store}
                        </span>
                    </div>
                ))}
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

export default StoreCheck