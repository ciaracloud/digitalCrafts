const initialState = {
  temp: "",
  name: "",
};

function weather(state = initialState, action) {
  switch (action.type) {
    case "CHANGE_TEMP":
      return { ...state, temp: action.payload };
    case "CHANGE_NAME":
      return { ...state, name: action.payload };
    default:
      return state;
  }
}

export default weather;
