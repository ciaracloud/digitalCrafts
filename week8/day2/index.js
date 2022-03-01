const express = require("express");
const app = express();
// middleware
app.use(express.json());
PORT = 3000;
const studentDB = [
  { name: "Santos" },
  { name: "Ciara" },
  { name: "Rayleigh" },
  { name: "Jason" },
];

// routes for CRUD (create, read, update, delete)
// create
app.post("/create_user", (req, res) => {
  console.log(req.body);
  //   const studentToAdd = {
  //     name: "Jarrod",
  //   };
  //   studentDB.push(studentToAdd);
  res.send(studentDB);
});

// read
app.get("/", (req, res) => {
  const students = [
    { name: "Santos" },
    { name: "Ciara" },
    { name: "Rayleigh" },
    { name: "Jason" },
  ];
  let greeting = `<div>`;
  for (const student of students) {
    greeting += `<h1>Howdy ${student.name}</h1>`;
  }
  greeting += `</div>`;
  res.send(greeting);
});

// update
app.get("/update_users", (req, res) => {
  res.send("/update_users");
});

// delete
app.get("/delete_users", (req, res) => {
  res.send("/delete_users");
});

app.listen(PORT, console.log(`listening on http://localhost:${PORT}`));
