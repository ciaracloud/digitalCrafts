// -----------------------------{DEFAULT VALUES}-----------------------------

const printArray = (array) => {
  console.log(array[0]);
};

// give default value of empty array
const printArray = (array = []) => {
  console.log(array[0]);
};

// give deafult value of array with something in it
const printArray = (array = ["Kiwi"]) => {
  console.log(array[0]);
};
printArray(["Ciara"]);
