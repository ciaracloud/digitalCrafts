require("dotenv").config();
const express = require("express");
const app = express();
const db = require("./models/");
const PORT = 3000;

app.listen(PORT, console.log(`listening on http://localhost${PORT}`));
