import "./App.css";
import { useSelector, useDispatch } from "react-redux";
import ProductContainer from "./components/ProductContainer";
import Cart from "./components/Cart";

function App() {
  const dispatch = useDispatch();
  return (
    <div className="App">
      <h1>Kiwi's Handy Dandy Tools 🧰</h1>
      <div className="layoutContainer">
        <ProductContainer />
        <Cart />
      </div>
    </div>
  );
}

export default App;
