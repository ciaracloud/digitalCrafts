import "./App.css";
import { useState, useEffect } from "react";

function App() {
  const [username, setUsername] = useState("");
  const [phoneNumber, setPhoneNumber] = useState("");
  const [contacts, setContacts] = useState([]);
  useEffect(() => {
    setUsername("");
    setPhoneNumber("");
  }, [contacts]);
  return (
    <div className="App">
      <h1>Phone Book</h1>
      <h2>Name: {username}</h2>
      <h2>Phone Number: {phoneNumber}</h2>
      <input
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        type="text"
        placeholder="Name"
      />
      <input
        value={phoneNumber}
        onChange={(e) => setPhoneNumber(e.target.value)}
        type="text"
        placeholder="Phone number"
      />
      <button
        onClick={() => setContacts([...contacts, [username, phoneNumber]])}
      >
        Add contact
      </button>
      {contacts.map((contact) => {
        return (
          <div>
            <p>
              {contact[0]} {contact[1]}
            </p>
          </div>
        );
      })}
    </div>
  );
}

export default App;
