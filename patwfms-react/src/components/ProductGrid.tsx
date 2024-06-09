// src/ProductsGrid.tsx

import React from 'react';
import Product from './Product';
import { ProductType } from './Product';

interface ProductsGridProps {
    products: ProductType[];
}

const ProductsGrid: React.FC<ProductsGridProps> = ({ products }) => {
    return (
        <div className="products">
            {products.map((product, index) => (
                <Product key={index} product={product} />
            ))}
        </div>
    );
};

export default ProductsGrid;
