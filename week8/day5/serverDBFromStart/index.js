const express = require("express");
const creds = require("./db");
const app = express();
app.use(express.json());
const PORT = 3000;

app.get("/get_fruit", (req, res) => {
  creds.connect((err, client, release) => {
    if (err) {
      console.log("error with your connection, read this error:", err);
    }
    console.log("connection successfl with client");
    client.query(`SELECT * FROM fruits`, (err, result) => {
      if (err) {
        res.status(400).send(err);
      }
      res.send(result.rows);
    });
  });
});

app.post("/create_fruit", (req, res) => {
  console.log("create fruit");
});

app.listen(PORT, console.log(`listening on http://localhost${PORT}`));
