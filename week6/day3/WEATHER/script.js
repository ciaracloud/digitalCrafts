const input = document.querySelector("input");
const button = document.querySelector(".button");
const todayContainer = document.querySelector(".todayContainer");
const forecastContainer = document.querySelector(".forecastContainer");
const weatherContainer = document.querySelector(".weatherContainer");

const searchWeather = async () => {
  todayContainer.innerHTML = "";
  const weatherUrl = `http://api.openweathermap.org/data/2.5/weather?appid=bef0a4f4c45aebade1866b368f3734f3&zip=${input.value}&units=imperial`;
  const weather = await fetch(weatherUrl);
  const weatherJson = await weather.json();
  const headerElement = document.createElement("h3");
  headerElement.innerText = "-- Today --";
  const tempElement = document.createElement("p");
  tempElement.innerText = `Current tempurature: ${Math.floor(
    weatherJson.main.temp
  )}° F`;
  tempElement.className = "temp";
  const cityElement = document.createElement("p");
  cityElement.innerText = `City: ${weatherJson.name}`;
  const feelsLikeElement = document.createElement("p");
  feelsLikeElement.innerText = `Feels like: ${Math.floor(
    weatherJson.main.feels_like
  )}° F`;
  const descriptionElement = document.createElement("p");
  descriptionElement.innerText = `Sky: ${weatherJson.weather[0].main}`;
  const windElement = document.createElement("p");
  windElement.innerText = `Wind: ${Math.floor(weatherJson.wind.speed)} mi/h`;
  todayContainer.append(
    headerElement,
    cityElement,
    tempElement,
    feelsLikeElement,
    descriptionElement,
    windElement
  );
  weatherContainer.append(todayContainer);
  input.value = "";
  console.log("weather object: ", weatherJson);
};

const searchForecast = async () => {
  forecastContainer.innerHtml = "";
  const weatherUrl = `http://api.openweathermap.org/data/2.5/weather?appid=bef0a4f4c45aebade1866b368f3734f3&zip=${input.value}&units=imperial`;
  const weather = await fetch(weatherUrl);
  const weatherJson = await weather.json();
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
    highLowElement.innerText = `High: ${Math.floor(
      forecastJson.daily[counter].temp.max
    )}° F, Low: ${Math.floor(forecastJson.daily[counter].temp.min)}° F`;
    dayElement.append(dayHeaderElement, dayDescriptionElement, highLowElement);
    forecastContainer.append(dayElement);
    counter++;
  }
  weatherContainer.append(forecastContainer);
  console.log("forecast object: ", forecastJson);
  input.value = "";
};

button.addEventListener("click", () => {
  searchWeather();
  searchForecast();
});
