import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";

export default function Form() {
  const dispatch = useDispatch();
  const name = useSelector((state) => state.name);
  const email = useSelector((state) => state.email);
  const password = useSelector((state) => state.password);
  const user = useSelector((state) => state.user);

  const changeInputField = (e) => {
    dispatch({
      type: `CHANGE_${e.target.name.toUpperCase()}`,
      payload: e.target.value,
    });
  };

  return (
    <div className="form">
      <h1>Form</h1>
      <input
        name="name"
        type="text"
        onChange={changeInputField}
        value={name}
        placeholder="name"
      />
      <input
        name="email"
        type="text"
        onChange={changeInputField}
        placeholder="email"
        value={email}
      />
      <input
        name="password"
        type="text"
        onChange={changeInputField}
        placeholder="password"
        value={password}
      />
      <input
        name="userList"
        type="text"
        onChange={changeInputField}
        placeholder="Add a user to a list"
        // value={user.username}
      />
      <button>Submit</button>
      {/* // print user here */}
    </div>
  );
}
