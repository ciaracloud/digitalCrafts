require("dotenv").config();
const express = require("express");
const app = express();
const PORT = 3000;
const db = require("./models/");
const { append } = require("express/lib/response");

app.get("/get_users", async (req, res) => {
  let test4 = await db.test4.findAll();
  res.send(test4);
});

app.listen(PORT, console.log(`listening on http://localhost${PORT}`));
