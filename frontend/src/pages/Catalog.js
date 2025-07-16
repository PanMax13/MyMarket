import React from 'react';
import './Catalog.css';

const Catalog = () => {
  // TODO: получить список товаров с backend
  const products = [
    { id: 1, name: 'Товар 1', price: 100 },
    { id: 2, name: 'Товар 2', price: 200 },
    { id: 3, name: 'Товар 3', price: 300 },
  ];

  return (
    <div className="catalog-container">
      <h2>Каталог товаров</h2>
      <ul className="product-list">
        {products.map(product => (
          <li key={product.id} className="product-item">
            <span>{product.name}</span>
            <span>{product.price} ₽</span>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Catalog; 