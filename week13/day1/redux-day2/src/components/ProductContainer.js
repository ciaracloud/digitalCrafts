import React from "react";
import Products from "./Products";
import { useSelector, useDispatch } from "react-redux";

export default function ProductContainer() {
  const products = useSelector((state) => state.products);
  console.table(products);
  return (
    <div className="productContainer">
      <h1>Product Container</h1>
      {products?.map((product) => (
        <Products product={product} />
      ))}
    </div>
  );
}
