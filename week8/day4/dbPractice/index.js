const express = require("express");
const creds = require("./db");
const app = express();
const PORT = 3000;
app.use(express.json());

app.get("/", (req, res) => {
  res.send("hello");
});

app.post("/test", (req, res) => {
  console.log(req.body);
  creds.connect((err, client, release) => {
    client.query(
      `INSERT INTO veggies (name, color) VALUES ('${req.body.name}','${req.body.color}')`,
      (err, result) => {
        if (err) {
          console.log(err);
          res.status(400).send(err);
        }
        res.send(result);
      }
    );
  });
});

app.listen(PORT, console.log(`listening on http://localhost${PORT}`));
