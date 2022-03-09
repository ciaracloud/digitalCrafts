const express = require("express");
const app = express();
const PORT = 3000;
app.use(express.json());
const db = require("./models");

// CRUD for user (create, read, update, delete)

app.post("/create_user", async (req, res) => {
  const { firstName, lastName, email } = req.body;
  const createUser = await db.User.create({
    firstName: firstName,
    lastName: lastName,
    email: email,
  });
  res.send(`Made the user ${firstName} ${lastName}`);
});

app.get("/get_users", async (req, res) => {
  const getUsers = await db.User.findAll();
  res.send(getUsers);
});

app.post("/update_user/:id", async (req, res) => {
  let { id } = req.params;
  id = parseInt(id);
  const { email } = req.body;
  const updateUser = await db.User.update(
    { email: email },
    { where: { id: id } }
  );
  res.send("updated user email");
});

app.delete("/delete_user/:id", async (req, res) => {
  let { id } = req.params;
  id = parseInt(id);
  const deleteUser = await db.User.destroy({ where: { id: id } });
  res.send(`deleted user with id: ${id}`);
});

// CRUD for photo (create, read, update, delete)

app.post("/create_photo", async (req, res) => {
  const { title, url, userId } = req.body;
  const createPhoto = await db.Photo.create({
    title: title,
    url: url,
    userId: userId,
  });
  res.send(`added the photo!`);
});

app.get("/get_photos", async (req, res) => {
  const getPhotos = await db.Photo.findAll();
  res.send(getPhotos);
});

app.post("/update_photo/:id", async (req, res) => {
  let { id } = req.params;
  id = parseInt(id);
  const { title, url } = req.body;
  const updatePhoto = await db.Photo.update(
    { title: title, url: url },
    { where: { id: id } }
  );
  res.send("updated photo!");
});

app.delete("/delete_photo/:id", async (req, res) => {
  let { id } = req.params;
  id = parseInt(id);
  const deletePhoto = await db.Photo.destroy({ where: { id: id } });
  res.send(`deleted photo!`);
});

app.listen(PORT, console.log(`listening on http://localhost${PORT}`));
