// src/api.ts

import { ProductType } from './Product';

export const fetchProducts = async (searchQuery: string, country: string): Promise<ProductType[]> => {
  const response = await fetch(`http://localhost:5000/scrape_amazon?query=${searchQuery}`);
  if (!response.ok) {
    throw new Error('Failed to fetch data from backend');
  }
  const data: ProductType[] = await response.json();
  return data;
};