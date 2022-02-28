console.log("hello, i am in node");

const express = require("express");
const app = express();
const PORT = 3002;
app.listen(PORT, console.log(`listening on port http://localhost:${PORT}`));
