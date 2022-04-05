import { categories } from "plotly.js/lib/box";

const initialState = "Kiwi";

function cat(state = initialState, action) {
  switch (action.type) {
    case "CHANGE_CAT":
      return (state = action.payload);
    default:
      return state;
  }
}

export default cat;
