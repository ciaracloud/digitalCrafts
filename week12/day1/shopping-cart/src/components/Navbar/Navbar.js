import "./Navbar.css";

import React from "react";

export default function Navbar() {
  return (
    <div className="navbar">
      <a href="http://localhost:3000/items">Items</a>
      <a href="http://localhost:3000/cart">Cart</a>
    </div>
  );
}
