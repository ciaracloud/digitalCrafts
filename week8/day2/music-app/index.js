const express = require("express");
const app = express();
const PORT = 3000;
const songs = require("./musicDB");

app.get("/", (req, res) => {
  let homePage = `<h1>Lil' Wayne</h1>
     <img src="https://64.media.tumblr.com/9fe4b9e96744c31675807d7ac84ac852/tumblr_pfrbz6kcd61r6ccbh_640.jpg"></img>';
     <p>Dwayne Michael Carter Jr., known professionally as Lil Wayne, is an American rapper. He is regarded by many contemporaries as one of the most influential hip hop artists of his generation, and often cited as one of the greatest rappers of all time.</p>`;
  res.send(homePage);
});

app.get("/cds", (req, res) => {
  let albums = `<h1>Albums:</h1>
  <ul>
  <li><a href="http://localhost:3000/0">${songs[0].name}</a></li>
  <li><a href="http://localhost:3000/1">${songs[1].name}</a></li>
  </ul>
  `;
  res.send(albums);
});

app.get("/:paramaters", (req, res) => {
  const number = req.params.paramaters;
  let page = `<img src=${songs[number].imgURL} width=200px>
  <h1>${songs[number].name}</h1>
  <ul>`;
  for (songTitle of songs[number].songTitles) {
    page += `<li>${songTitle}</li>`;
  }
  page += `</ul>`;
  res.send(page);
});

// app.get("/1", (req, res) => {
//   let page1 = `<img src=${songs[1].imgURL} width=200px>
//   <h1>${songs[1].name}</h1>
//   <ul>`;
//   for (songTitle of songs[1].songTitles) {
//     page1 += `<li>${songTitle}</li>`;
//   }
//   page1 += `</ul>`;
//   res.send(page1);
// });

app.listen(PORT, console.log(`listening to http://localhost:${PORT}`));
