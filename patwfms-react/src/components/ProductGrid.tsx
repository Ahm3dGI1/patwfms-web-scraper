import React from 'react';
import Product from './Product';
import { ProductType } from './Product';

interface ProductsGridProps {
    products: ProductType[];
    checkedStores: string[];
}

const ProductsGrid: React.FC<ProductsGridProps> = ({ products, checkedStores }) => {

    // Filter products based on checked stores
    const filteredProducts = checkedStores.length > 0
        ? products.filter(product => checkedStores.includes(product.site))
        : products;

    return (
        <div className="products">
            {filteredProducts.map((product, index) => (
                <Product key={index} product={product} />
            ))}
        </div>
    );
};

export default ProductsGrid;
