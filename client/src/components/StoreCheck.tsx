import './StoreCheck.css'



interface StoreCheckProps {
    checkedStores: string[];
    setCheckedStores: React.Dispatch<React.SetStateAction<string[]>>;
    country: string;
}

const storeLists: { [key: string]: string[] } = {
    US: ['Amazon', 'Ebay', 'Target', 'Walmart'],
    Taiwan: ['Yahoo'],
    Korea: ['Coupang', 'Naver', 'SSG'],
    Japan: ['Amazon', 'Rakuten'],
    India: ['Amazon'],
    Germany: ['Amazon', 'Otto'],
    Argentina: ['MercadoLibre', 'Fravega'],
};

const StoreCheck: React.FC<StoreCheckProps> = ({ checkedStores, setCheckedStores, country }) => {

    const stores = storeLists[country];

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
                {stores.map((store, _) => (
                    <div className="store-check">
                        <input
                            onClick={() => handleCheck(store)}
                            type="checkbox"
                            id={store}
                            key={store}
                        />
                        <span>
                            {store}
                        </span>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default StoreCheck