import { ProductType } from './Product';

export const fetchProducts = async (searchQuery: string, country: string): Promise<ProductType[]> => {
  const response = await fetch(`http://localhost:5000/scrape?query=${searchQuery}$country=${country}`);
  if (!response.ok) {
    throw new Error('Failed to fetch data from backend');
  }
  const data: ProductType[] = await response.json();
  return data;
};