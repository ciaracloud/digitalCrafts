console.log("hi");
function printMessage() {
  console.log("I printed a button");
}

// select the element you want to update/change
let button = document.querySelector(".printButton");
console.log(button);

// add event listener (listens for an event to happen and uses anonymous function)
// first element in anonymous function parentheses (e) stands for event and gives information about the element
button.addEventListener("click", (e) => {
  console.log(e);
  printMessage();
});

// make change to element
