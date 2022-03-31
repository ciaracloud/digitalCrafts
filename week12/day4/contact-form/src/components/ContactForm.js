import React from "react";
import "./ContactForm.css";

export default function ContactForm({ input, setInput, validateAndReset }) {
  return (
    <div className="contactForm">
      <h1>ContactForm</h1>
      <div className="firstNameContainer elementContainer">
        <p>Your first name</p>
        <input
          type="text"
          name="firstName"
          onChange={(e) =>
            setInput({ ...input, [e.target.name]: e.target.value })
          }
          placeholder="First name"
          value={input.firstName}
        />
      </div>
      <div className="lastNameContainer elementContainer">
        <p>Your last name</p>
        <input
          type="text"
          name="lastName"
          onChange={(e) =>
            setInput({ ...input, [e.target.name]: e.target.value })
          }
          placeholder="Last name"
          value={input.lastName}
        />
      </div>
      <div className="phoneContainer elementContainer">
        <p>Phone</p>
        <input
          type="text"
          name="phone"
          onChange={(e) =>
            setInput({ ...input, [e.target.name]: e.target.value })
          }
          placeholder="Phone"
          value={input.phone}
        />
      </div>
      <div className="mailContainer elementContainer">
        <p>Mail</p>
        <input
          type="text"
          name="email"
          onChange={(e) =>
            setInput({ ...input, [e.target.name]: e.target.value })
          }
          placeholder="Email"
          value={input.email}
        />
      </div>
      <div className="mailContainer elementContainer">
        <p>Message</p>
        <input
          type="text"
          name="message"
          onChange={(e) =>
            setInput({ ...input, [e.target.name]: e.target.value })
          }
          placeholder="Message"
          value={input.message}
        />
      </div>
      <div className="contactContainer elementContainer">
        <p>Best way to contact you</p>
        <select
          name="contact"
          id="contact"
          value={input.contact}
          onChange={(e) =>
            setInput({ ...input, [e.target.name]: e.target.value })
          }
        >
          <option name="contact" value="Phone call">
            Phone call
          </option>
          <option name="contact" value="Text message">
            Text message
          </option>
          <option name="contact" value="Email">
            Email
          </option>
        </select>
      </div>
      <button
        onClick={(e) => {
          validateAndReset(e);
        }}
      >
        Submit
      </button>
    </div>
  );
}
