import React from "react";

export default function UserData({ userData }) {
  return (
    <div>
      <h1>User Data Entered</h1>
      <form action="">
        <input type="text" value={userData.name} disabled />
        <input type="text" value={userData.email} disabled />
      </form>
    </div>
  );
}
