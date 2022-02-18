const input = document.querySelector("input");
const searchButton = document.querySelector(".searchButton");
const todayContainer = document.querySelector(".todayContainer");
const forecastContainer = document.querySelector(".forecastContainer");
const weatherContainer = document.querySelector(".weatherContainer");

// functions
const daysOfWeek = [
  "Sunday",
  "Monday",
  "Tuesday",
  "Wednesday",
  "Thursday",
  "Friday",
  "Saturday",
];

const printToday = () => {
  const d = new Date();
  let day = d.getDay();
  console.log("today is: ", daysOfWeek[day]);
};

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
  const feelsLikeElement = document.createElement("p");
  feelsLikeElement.innerText = `Feels like:\n${Math.floor(
    weatherJson.main.feels_like
  )}° F`;
  feelsLikeElement.className = "infoElement";
  const windElement = document.createElement("p");
  windElement.innerText = `Wind:\n${Math.floor(weatherJson.wind.speed)} mi/h`;
  windElement.className = "infoElement";
  const humidityElement = document.createElement("p");
  humidityElement.innerText = `Humidity:\n${Math.floor(
    weatherJson.main.humidity
  )}`;
  humidityElement.className = "infoElement";
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
    dayHeaderElement.innerText = `${counter + 1}`;
    const dayDescriptionElement = document.createElement("p");
    if (forecastJson.daily[counter].weather[0].main == "Clouds") {
      dayDescriptionElement.innerText = `Cloudy`;
    } else if (forecastJson.daily[counter].weather[0].main == "Rain") {
      dayDescriptionElement.innerText = `Rainy`;
    } else if (forecastJson.daily[counter].weather[0].main == "Clear") {
      dayDescriptionElement.innerText = `Sunny`;
    } else if (forecastJson.daily[counter].weather[0].main == "Drizzle") {
      dayDescriptionElement.innerText = `Light Rain`;
    } else if (forecastJson.daily[counter].weather[0].main == "Thunderstorm") {
      dayDescriptionElement.innerText = `Thunderstorms`;
    } else if (forecastJson.daily[counter].weather[0].main == "Snow") {
      dayDescriptionElement.innerText = `Snowy`;
    } else {
      dayDescriptionElement.innerText = `${forecastJson.daily[counter].weather[0].main}`;
    }
    const dayHighLowElement = document.createElement("p");
    dayHighLowElement.innerText = `${Math.floor(
      forecastJson.daily[counter].temp.max
    )}°/${Math.floor(forecastJson.daily[counter].temp.min)}°`;
    dayElement.append(
      dayHeaderElement,
      dayDescriptionElement,
      dayHighLowElement
    );
    forecastContainer.append(dayElement);
    counter++;
  }

  const infoContainer = document.createElement("div");
  infoContainer.append(feelsLikeElement, windElement, humidityElement);
  infoContainer.className = "infoContainer";
  const tempAndDescriptionContainer = document.createElement("div");
  tempAndDescriptionContainer.className = "tempAndDescriptionContainer";
  tempAndDescriptionContainer.append(
    tempElement,
    descriptionElement,
    infoContainer
  );
  console.log("forecast object: ", forecastJson);
  todayContainer.append(tempAndDescriptionContainer, imgElement);
  weatherContainer.append(cityElement, todayContainer, forecastContainer);
  console.log("weather object: ", weatherJson);
};

searchButton.addEventListener("click", () => {
  printToday();
  searchWeatherAndForecast();
  weatherContainer.innerHTML = "";
  input.value = "";
  forecastContainer.innerHTML = "";
});

// ------------ PRINT DAYS OF WEEK (PUT IN LOOP) ------------
// const d = new Date();
// let day = d.getDay();
// let dayIndex = day + counter1;
// if (dayIndex == 7) {
//   counter1 = day - 2;
// }
// console.log(
//   "day: ",
//   day,
//   "counter1: ",
//   counter1,
//   "dayIndex: ",
//   dayIndex,
//   "this is day 1:",
//   daysOfWeek[dayIndex]
// );
