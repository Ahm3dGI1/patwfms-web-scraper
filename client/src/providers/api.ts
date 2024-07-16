import { ProductType } from '../components/Product';

export const fetchProducts = async (searchQuery: string, country: string, limitValue: string): Promise<ProductType[]> => {
  const response = await fetch(`https://patwfms-web-scraper-server.vercel.app/scrape?query=${searchQuery}&country=${country}&limit=${limitValue}`);
  if (!response.ok) {
    throw new Error('Failed to fetch data from backend');
  }
  const data: ProductType[] = await response.json();
  return data;
};