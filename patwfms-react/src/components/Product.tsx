import React from 'react';
import './Product.css'

export interface ProductType {
    image: string;
    name: string;
    price: string;
    url: string;
    site: string;
}

interface ProductProps {
    product: ProductType;
}

const Product: React.FC<ProductProps> = ({ product }) => {
    return (
        <div className="product">
            <img src={product.image} alt={product.name} />
            <h2>{product.name}</h2>
            <p>{product.price}</p>
            <a href={product.url} target="_blank" rel="noopener noreferrer">
                View on Amazon
            </a>
        </div>
    );
};

export default Product;
