import { combineReducers } from "redux";
import name from "./nameReducer";
import email from "./emailReducer";
import password from "./passwordReducer";
import cat from "./catReducer";
import weather from "./weatherReducer";

export default combineReducers({
  name,
  email,
  password,
  cat,
  weather,
});
