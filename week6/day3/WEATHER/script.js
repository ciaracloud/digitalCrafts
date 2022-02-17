const input = document.querySelector("input");
const button = document.querySelector(".btn.btn-info");
const weatherContainer = document.querySelector(".weatherContainer");

button.addEventListener("click", () => {
  searchWeather();
});

const searchWeather = async () => {
  console.log(input.value);
  const url = `http://api.openweathermap.org/data/2.5/weather?appid=05407dc4254bea406be637af43796a6a&zip=${input.value}`;
  const weather = await fetch(url);
  const weatherJson = await weather.json();
  console.log(weatherJson);
};
