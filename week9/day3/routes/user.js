const express = require("express");
const router = express.Router();
const db = require("../models");

// CRUD for user (create, read, update, delete)

router.post("/create", async (req, res) => {
  const { firstName, lastName, email } = req.body;
  const createUser = await db.User.create({
    firstName: firstName,
    lastName: lastName,
    email: email,
  });
  res.send(`Made the user ${firstName} ${lastName}`);
});

router.get("/get_all", async (req, res) => {
  const getUsers = await db.User.findAll();
  res.send(getUsers);
});

router.post("/update/:id", async (req, res) => {
  let { id } = req.params;
  id = parseInt(id);
  const { email } = req.body;
  const updateUser = await db.User.update(
    { email: email },
    { where: { id: id } }
  );
  res.send("updated user email");
});

router.delete("/delete/:id", async (req, res) => {
  let { id } = req.params;
  id = parseInt(id);
  const deleteUser = await db.User.destroy({ where: { id: id } });
  res.send(`deleted user with id: ${id}`);
});

module.exports = router;
