const express = require("express");
const app = express();
PORT = 3000;

app.get("/", (req, res) => {
  res.send("Hello World!");
});

app.get("/cats", (req, res) => {
  res.send("Meow!");
});

app.get("/dogs", (req, res) => {
  res.send("Woof!");
});

app.get("/cats_and_dogs", (req, res) => {
  res.send("Dogs and cats living together...mass hysteria!!");
});

app.get("/greet/Luke", (req, res) => {
  res.send("Hello, Luke!");
});

app.get("/greet/Ahsoka", (req, res) => {
  res.send("Hello, Ahsoka!");
});

app.get("/greet/Han", (req, res) => {
  res.send("Hello, Han!");
});

app.listen(PORT, console.log(`listening on http://localhost:${PORT}`));
