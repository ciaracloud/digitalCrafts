import "./App.css";
import ContactForm from "./components/ContactForm";
import { useState } from "react";

function App() {
  const defaultState = {
    firstName: "",
    lastName: "",
    phone: "",
    email: "",
    message: "",
    contact: "",
  };
  const validateAndReset = (e) => {
    e.preventDefault();
    if (
      input.firstName === "" ||
      input.lastName === "" ||
      input.phone === "" ||
      input.email === "" ||
      input.message === "" ||
      input.contact === ""
    ) {
      alert("Please check that none of the fields are blank! :)");
    }
    setInput(defaultState);
  };
  const [input, setInput] = useState(defaultState);
  return (
    <div className="App">
      <ContactForm
        input={input}
        setInput={setInput}
        validateAndReset={validateAndReset}
      />
    </div>
  );
}

export default App;
