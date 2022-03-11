const express = require("express");
const router = express.Router();
const db = require("../models");

// CRUD for photo (create, read, update, delete)

router.post("/create", async (req, res) => {
  const { title, url, userId } = req.body;
  const createPhoto = await db.Photo.create({
    title: title,
    url: url,
    userId: userId,
  });
  res.send(`added the photo!`);
});

router.get("/get_all", async (req, res) => {
  const getPhotos = await db.Photo.findAll();
  res.send(getPhotos);
});

router.post("/update/:id", async (req, res) => {
  let { id } = req.params;
  id = parseInt(id);
  const { title, url } = req.body;
  const updatePhoto = await db.Photo.update(
    { title: title, url: url },
    { where: { id: id } }
  );
  res.send("updated photo!");
});

router.delete("/delete/:id", async (req, res) => {
  let { id } = req.params;
  id = parseInt(id);
  const deletePhoto = await db.Photo.destroy({ where: { id: id } });
  res.send(`deleted photo!`);
});

module.exports = router;
