import React from "react";
import { useDispatch } from "react-redux";

export default function Products({ product }) {
  console.log("this is product", product);
  const dispatch = useDispatch();
  return (
    <div className="singleProduct">
      <img className="productImage" src={product?.img} alt="" />
      <h4>{product?.name}</h4>
      <button
        onClick={() => dispatch({ type: "ADD_TO_CART", payload: product })}
      >
        Add to cart
      </button>
    </div>
  );
}
