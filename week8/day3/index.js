const express = require("express");
const ejs = require("ejs");
const path = require("path");
const app = express();
const PORT = 3000;

//middleware
// template engine
app.set("views", path.join(__dirname, "views"));
app.set("view engine", "ejs");

//setup public folder
app.use(express.static("./public"));

//minimum required to show ejs rendering on a page
let students = ["Santos", "Jason", "Rayleigh", "Ciara"];

let html = ejs.render('<h2><%= students.join(","); %></h2>', {
  students: students,
});

app.get("/students", (req, res) => {
  res.send(html);
});

app.get("/", (req, res) => {
  res.render("pages/home");
});

app.listen(PORT, console.log(`Listening on port ${PORT}`));
