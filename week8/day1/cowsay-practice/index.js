const express = require("express");
const app = express();
const PORT = 3003;
app.listen(PORT, console.log(`listening on port http://localhost:${PORT}`));
const cowsay = require("cowsay");

// console.log(cowsay.say({ text: " " }));

app.post("/sendCowUserName", (req, res) => {
  const cowsayText1 = cowsay.say({ text: "Adding cow user" });
  res.send(cowsayText1);
});

app.post("/sendCowAppointment", (req, res) => {
  const cowsayText2 = cowsay.say({ text: "Setting up cow appointment" });
  res.send(cowsayText2);
});

app.get("/getCowUserName", (req, res) => {
  const cowsayText3 = cowsay.say({ text: "Adding cow user" });
  res.send(cowsayText3);
});

app.get("/getCowAppointment", (req, res) => {
  const cowsayText2 = cowsay.say({ text: "Setting up cow appointment" });
  res.send(cowsayText2);
});

app.delete("/deleteCowUser", (req, res) => {
  res.send(console.log("deleted user"));
});
