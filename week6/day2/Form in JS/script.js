// TO CHECK FORM:

//select form
const form = document.querySelector("form");

const checkNames = (firstName, lastName) => {
  if (firstName.value.length < 2) {
    window.alert("Your first name needs to be greate than 1 character.");
    return false;
  }
  if (lastName.value.length < 2) {
    window.alert("Your first name needs to be greate than 1 character.");
    return false;
  }
  return true;
};

form.addEventListener("submit", (e) => {
  e.preventDefault();
  const firstName = document.querySelector(".firstName");
  const lastName = document.querySelector(".lastName");
  if (checkNames(firstName, lastName)) {
    //send stuff to database
    const userData = {
      firstName: firstName.value,
      lastName: lastName.value,
    };
  }
  window.alert("Your form needs to be fixed");
});
