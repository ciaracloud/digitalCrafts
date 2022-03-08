require("dotenv").config();
const express = require("express");
const app = express();
const PORT = 3000;
const bcrypt = require("bcrypt");
const db = require("./models/");
const { append } = require("express/lib/response");
app.use(express.json());

app.get("/get_users", async (req, res) => {
  let test4 = await db.test4.findAll();
  res.send(test4);
});

// app.post("/make_bcrypt_user", (req, res) => {
//   const saltRounds = 2;
//   const name = req.body.name;
//   const password = req.body.password;
//   console.log("this is your original password", password);
//   bcrypt.genSalt(saltRounds, function (err, salt) {
//     bcrypt.hash(password, salt, function (err, hash) {
//       console.log("this is the hashed password", hash);
//     });
//   });
//   console.log(name, password);
// });

app.get("/get_pets", async (req, res) => {
  let pets = await db.pets.findAll();
  res.send(pets);
});

app.post("/create_pet", async (req, res) => {
  const type = req.body.type;
  const species = req.body.species;
  const name = req.body.name;
  const age = req.body.age;
  const ownerId = req.body.ownerId;
  const addPet = await db.pets.create({
    type: type,
    species: species,
    name: name,
    age: age,
    ownerId: ownerId,
  });
  res.send(addPet);
});

app.get("/get_owners", async (req, res) => {
  let owners = await db.owners.findAll();
  res.send(owners);
});

app.post("/create_owner", async (req, res) => {
  const saltRounds = 2;
  const name = req.body.name;
  const password = req.body.password;
  const location = req.body.location;
  const enviornment = req.body.enviornment;
  const salt = await bcrypt.genSalt(saltRounds);
  const hashedPw = await bcrypt.hash(password, salt);
  const addOwner = await db.owners.create({
    name: name,
    password: hashedPw,
    location: location,
    enviornment: enviornment,
  });
  res.send(addOwner);
});

app.listen(PORT, console.log(`listening on http://localhost${PORT}`));
