import "./App.css";
import House from "./components/House.js";

function App() {
  const rooms = [
    { name: "Bedroom" },
    { name: "Cat Room" },
    { name: "Guest Room" },
  ];
  return (
    <div className="App">
      <h1>Passing Props</h1>
      <House rooms={rooms} />
    </div>
  );
}

export default App;
