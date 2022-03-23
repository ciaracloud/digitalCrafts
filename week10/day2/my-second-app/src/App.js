import logo from "./logo.svg";
import "./App.css";
import Plot from "react-plotly.js";

function App() {
  var data = [
    {
      values: [19, 26, 55],
      labels: ["Residential", "Non-Residential", "Utility"],
      type: "pie",
    },
  ];
  const layout = {
    height: 600,
    width: 700,
  };
  return (
    <div className="App">
      <h1>Hello</h1>
      <Plot data={data} layout={layout} />
    </div>
  );
}

export default App;
