const input = document.querySelector("input");
const searchButton = document.querySelector(".searchButton");
const todayContainer = document.querySelector(".todayContainer");
const forecastContainer = document.querySelector(".forecastContainer");
const weatherContainer = document.querySelector(".weatherContainer");

// functions

const searchWeatherAndForecast = async () => {
  todayContainer.innerHTML = "";
  const weatherUrl = `http://api.openweathermap.org/data/2.5/weather?appid=bef0a4f4c45aebade1866b368f3734f3&zip=${input.value}&units=imperial`;
  const weather = await fetch(weatherUrl);
  const weatherJson = await weather.json();
  const tempElement = document.createElement("p");
  tempElement.innerText = `${Math.floor(weatherJson.main.temp)}° F`;
  tempElement.className = "temp";
  const cityElement = document.createElement("p");
  cityElement.className = "cityElement";
  cityElement.innerText = `${weatherJson.name}`;
  const feelsLikeElement = document.createElement("p");
  feelsLikeElement.innerText = `Feels like: ${Math.floor(
    weatherJson.main.feels_like
  )}° F`;
  const descriptionElement = document.createElement("p");
  descriptionElement.className = "descriptionElement";
  if ((weatherJson.weather[0].main = "Clouds")) {
    descriptionElement.innerText = `Cloudy`;
  } else if ((weatherJson.weather[0].main = "Rain")) {
    descriptionElement.innerText = `Rainy`;
  } else if ((weatherJson.weather[0].main = "Clear")) {
    descriptionElement.innerText = `Sunny`;
  } else if ((weatherJson.weather[0].main = "Drizzle")) {
    descriptionElement.innerText = `Light Rain`;
  } else if ((weatherJson.weather[0].main = "Thunderstorm")) {
    descriptionElement.innerText = `Thunderstorms`;
  } else if ((weatherJson.weather[0].main = "Snow")) {
    descriptionElement.innerText = `Snowy`;
  } else {
    descriptionElement.innerText = `${weatherJson.weather[0].main}`;
  }
  const windElement = document.createElement("p");
  windElement.innerText = `Wind: ${Math.floor(weatherJson.wind.speed)} mi/h`;
  const imgElement = document.createElement("img");
  imgElement.className = "imgElement";
  if (weatherJson.weather[0].main == "Clear") {
    imgElement.src = "images/clear.jpg";
  } else if (weatherJson.weather[0].main == "Clouds") {
    imgElement.src = "images/cloudy.jpg";
  } else if (weatherJson.weather[0].main == "Rain") {
    imgElement.src = "images/rainy.jpg";
  } else if (weatherJson.weather[0].main == "Drizzle") {
    imgElement.src = "images/drizzle.jpg";
  } else if (weatherJson.weather[0].main == "Thunderstorm") {
    imgElement.src = "images/thunderstorm.jpg";
  } else if (weatherJson.weather[0].main == "Snow") {
    imgElement.src = "images/snow.jpg";
  } else {
    imgElement.src = "images/other.jpg";
  }
  const forecastUrl = `https://api.openweathermap.org/data/2.5/onecall?lat=${weatherJson.coord.lat}&lon=${weatherJson.coord.lon}&appid=bef0a4f4c45aebade1866b368f3734f3&units=imperial`;
  const forecast = await fetch(forecastUrl);
  const forecastJson = await forecast.json();
  counter = 0;
  for (day of forecastJson.daily) {
    const dayElement = document.createElement("div");
    dayElement.className = `day${counter + 1} forecastElement`;
    const dayHeaderElement = document.createElement("h3");
    dayHeaderElement.innerText = `-- Day ${counter + 1} --`;
    const dayDescriptionElement = document.createElement("p");
    dayDescriptionElement.innerText = `Description: ${forecastJson.daily[counter].weather[0].main}`;
    const highLowElement = document.createElement("p");
    highLowElement.innerText = `${Math.floor(
      forecastJson.daily[counter].temp.max
    )}°/${Math.floor(forecastJson.daily[counter].temp.min)}°`;
    dayElement.append(dayHeaderElement, dayDescriptionElement, highLowElement);
    forecastContainer.append(dayElement);
    counter++;
  }
  console.log("forecast object: ", forecastJson);
  todayContainer.append(
    tempElement,
    descriptionElement,
    feelsLikeElement,
    windElement,
    imgElement
  );
  weatherContainer.append(cityElement, todayContainer, forecastContainer);
  console.log("weather object: ", weatherJson);
};

const searchForecast = async () => {};

searchButton.addEventListener("click", () => {
  searchWeatherAndForecast();
  weatherContainer.innerHTML = "";
  input.value = "";
  forecastContainer.innerHTML = "";
});
