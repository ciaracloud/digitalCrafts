const express = require("express");
const app = express();
const PORT = 3000;
const friends = require("./app");

app.listen(PORT, console.log(`listening on http://localhost:${PORT}`));
