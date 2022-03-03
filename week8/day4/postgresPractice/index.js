const express = require("express");
const app = express();
const creds = require("./db");
const PORT = 3000;
app.use(express.json());

app.get("/getCats", (req, res) => {
  creds.connect((err, client, release) => {
    client.query("SELECT * FROM cats", (err, result) => {
      res.send(result);
    });
  });
});

app.post("/makeCats", (req, res) => {
  console.log(req.body);
  creds.connect((err, client, release) => {
    client.query(
      `INSERT INTO cats (name, color) VALUES ('${req.body.name}','${req.body.color}')`,
      (err, result) => {
        if (err) {
          console.log(err);
          res.send(err);
        }
        res.send(result);
      }
    );
  });
});

app.listen(PORT, console.log(`listening on http://localhost:${PORT}`));
