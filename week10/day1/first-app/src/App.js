import "./App.css";
import Location from "./Location";

function App() {
  const name = "Ciara";
  const favFood = "Sushi";
  const city = "Tampa";
  return (
    <div className="App">
      <h1>Ciara</h1>
      <Location city={city} />
      <p>{favFood}</p>
      <p>{name}</p>
    </div>
  );
}

export default App;
