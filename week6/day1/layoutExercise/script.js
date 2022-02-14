const movie = {
  Title: "Mean Girls",
  Year: "2004",
  Rated: "PG-13",
  Released: "30 Apr 2004",
  Runtime: "97 min",
  Genre: "Comedy",
  Director: "Mark Waters",
  Writer: "Rosalind Wiseman, Tina Fey",
  Actors: ["Lindsay Lohan", "Jonathan Bennett", "Rachel McAdams"],
  Plot: `Cady Heron is a hit with The Plastics, the A-list girl clique at her new school, until she makes the mistake of falling for Aaron Samuels, the ex-boyfriend of alpha Plastic Regina George.`,
  Language: "English, German, Vietnamese, Swahili",
  Country: "United States, Canada",
  Awards: "7 wins & 25 nominations",
  Poster1:
    "https://play-lh.googleusercontent.com/FaBWrOOZBR3NcTCNKsUnKG3zzIIIYech-dwsCgw0XdLsN4WIM68k9pnh6YhTaVLsV9UL=w400-h600-rw",
  Image1:
    "https://imgix.bustle.com/nylon/18542152/origin.jpg?w=1200&h=1000&fit=crop&crop=faces&auto=format%2Ccompress",
  Ratings: [
    {
      Source: "Internet Movie Database",
      Value: "7.0/10",
    },
    {
      Source: "Rotten Tomatoes",
      Value: "84%",
    },
    {
      Source: "Metacritic",
      Value: "66/100",
    },
  ],
  Metascore: "66",
  imdbRating: "7.0",
  imdbVotes: "365,428",
  imdbID: "tt0377092",
  Type: "movie",
  DVD: "21 Sep 2004",
  BoxOffice: "$86,058,055",
  Production: "N/A",
  Website: "N/A",
  Response: "True",
};

const container = document.querySelector(".container");

const { Title, Year, Genre, Rated, Actors, Plot, Poster1, Image1 } = movie;
const titleElement = document.createElement("h1");
titleElement.innerText = Title;
const posterElement = document.createElement("img");
posterElement.src = Poster1;
posterElement.className = "poster";
const imageElement = document.createElement("img");
imageElement.src = Image1;
imageElement.className = "image";
const plotElement = document.createElement("p");
plotElement.innerText = Plot;
plotElement.className = "plot";
const castContainer = document.createElement("div");
castContainer.className = "castContainer";
const castElement = document.createElement("p");
castElement.innerText = `Starring ${Actors[0]}, ${Actors[1]}, ${Actors[2]}`;
const genreElement = document.createElement("p");
genreElement.innerText = Genre;
genreElement.className = "genre";
const ratedElement = document.createElement("p");
ratedElement.innerText = Rated;
const yearElement = document.createElement("p");
yearElement.innerText = Year;
const contentContainer = document.createElement("div");
const yearRatedContainer = document.createElement("div");
yearRatedContainer.className = "yearRated";
const posterContentContainer = document.createElement("div");
posterContentContainer.className = "posterContent";
posterContentContainer.append(posterElement, contentContainer);
yearRatedContainer.append(yearElement, ratedElement);
castContainer.append(castElement);
container.append(imageElement, titleElement, posterContentContainer);
contentContainer.append(
  yearRatedContainer,
  genreElement,
  plotElement,
  castContainer
);
