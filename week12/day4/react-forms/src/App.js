import "./App.css";
import { useState } from "react";
import UserData from "./UserData";

//controlled forms - tracked in state and value is set as the state
//add value and on change to input

function App() {
  const defaultState = {
    name: "",
    email: "",
  };

  const [inputField, setInputField] = useState(defaultState);

  const [userData, setUserData] = useState(defaultState);

  const changeStuff = (e) => {
    setInputField({
      ...inputField,
      [e.target.name]: e.target.value,
    });
  };

  const validateForm = (e) => {
    e.preventDefault();
    if (inputField.name === "") {
      alert("please type your name");
    }
    setUserData(inputField);
    setInputField(defaultState);
  };
  return (
    <div className="App">
      <h1>Forms</h1>
      <form action="" onSubmit={(e) => validateForm(e)}>
        <input
          name="name"
          onChange={(e) => changeStuff(e)}
          type="text"
          placeholder="name"
          value={inputField?.name}
        />
        <input
          name="email"
          onChange={(e) =>
            setInputField({ ...inputField, [e.target.name]: e.target.value })
          }
          type="email"
          placeholder="email"
          value={inputField?.email}
        />
        <input type="submit" value="submit" />
      </form>
      <UserData userData={userData} />
    </div>
  );
}

export default App;
