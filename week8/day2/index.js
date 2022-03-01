const express = require("express");
const app = express();
// middleware (jumps in between the request and the response and does something for you)
app.use(express.json()); //converts requests to JSON
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
  // formatting the data to always match how have the db set up as
  const values = Object.values(req.body);
  const theRightWayToSendData = {
    name: values[0],
  };
  studentDB.push(theRightWayToSendData);
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
app.post("/update_users", (req, res) => {
  const studentFound = studentDB.find((student) => student.name === "Santos");
  console.log(studentFound);
  studentFound.name = "SanToast";
  studentDB[0] = studentFound;
  res.send(studentDB);
});

// delete
app.get("/delete_users", (req, res) => {
  res.send("/delete_users");
});

app.listen(PORT, console.log(`listening on http://localhost:${PORT}`));
