import React from 'react';
import './Product.css'

export interface ProductType {
    image: string;
    title: string;
    price: string;
    url: string;
    store: string;
}

interface ProductProps {
    product: ProductType;
}

const Product: React.FC<ProductProps> = ({ product }) => {
    return (
        <div className="product">
            <div className="img-wrapper">
                <img src={product.image} alt={product.title} />
            </div>
            <h2>{product.title}</h2>
            <p>{product.price}</p>
            <a href={product.url} target="_blank" rel="noopener noreferrer">
                View on {product.store}
            </a>
        </div>
    );
};

export default Product;
