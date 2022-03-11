const express = require("express");
const app = express();

const user = require("./routes/user");
const photos = require("./routes/photos");
const PORT = 3000;

app.use(express.json());

app.use("/user", user);
app.use("/photos", photos);

app.listen(PORT, console.log(`listening on http://localhost${PORT}`));
