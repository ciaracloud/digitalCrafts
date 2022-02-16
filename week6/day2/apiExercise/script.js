const form = document.querySelector("form");
const inputMovie = document.querySelector(".inputMovie");
const movieContainer = document.querySelector(".movieContainer");

form.addEventListener("submit", (e) => {
  e.preventDefault();
  movieContainer.innerHTML = "";
  console.log(inputMovie.value);
  const getMovie = async () => {
    const movie = await fetch(
      `http://www.omdbapi.com/?apikey=c2b8d3c5&t=${inputMovie.value}&`
    );
    const movieJson = await movie.json();
    console.log(movieJson);
    const movieName = document.createElement("h3");
    movieName.innerText = movieJson.Title;
    console.log(movieName);
    movieContainer.append(movieName);
    const movieImg = document.createElement("img");
    movieImg.src = movieJson.Poster;
    movieContainer.append(movieImg);
    inputMovie.value = "";
  };
  getMovie();
});

// const testFunction = async () => {
//   const test = await fetch(`http://www.omdbapi.com/?apikey=c2b8d3c5&s=Home&`);
//   const testJson = await test.json();
//   console.log(testJson);
// };
// testFunction();
