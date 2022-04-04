import React from "react";

export default function CartItem({ product }) {
  return (
    <div className="singleProduct">
      <img className="productImage" src={product?.img} alt="" />
      <h4>{product?.name}</h4>
    </div>
  );
}
