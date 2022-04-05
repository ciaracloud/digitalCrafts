import "./Weather.css";
import { useDispatch, useSelector } from "react-redux";

import React from "react";

export default function Weather() {
  const dispatch = useDispatch();
  const name = useSelector((state) => state.weather.name);
  const temp = useSelector((state) => state.weather.temp);

  const updateName = (e) => {
    dispatch({ type: "CHANGE_NAME", payload: e.target.value });
  };

  const updateTemp = (e) => {
    dispatch({ type: "CHANGE_TEMP", payload: e.target.value });
  };

  const getWeather = async (city) => {
    const url = `https://api.openweathermap.org/data/2.5/weather?units=imperial&q=${city}&appid=bef0a4f4c45aebade1866b368f3734f3`;
    const weather = await fetch(url);
    const weatherJson = await weather.json();
    const weatherTemp = weatherJson.main.temp;
    console.log(weatherJson);
    console.log(weatherTemp);
    dispatch({ type: "CHANGE_TEMP", payload: weatherTemp });
  };
  return (
    <div>
      <h1>Weather App</h1>
      <p name="temp">{name}</p>
      <p name="name">{temp}</p>
      <input type="text" value={name} onChange={updateName} />
      <button onClick={() => getWeather(name)}>Search</button>
    </div>
  );
}
