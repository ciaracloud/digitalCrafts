const express = require("express");
const app = express();
const PORT = 3001;

//routes
app.get("/", (req, res) => {
  console.log(req);
  res.send("this is my response");
});

app.post("/user_data", (req, res) => {
  res.send("posting user data");
});

app.listen(PORT, console.log(`listening on port http://localhost:${PORT}`));

console.log("hello");
