// Write a function that takes a number as an input.
// Have it create an empty array and then push a string into the array as many
// times as the input number. If the input is anything other than a positive
// integer return an empty array
//
// Name the function "finalFunction"

function finalFunction(number) {
  let arr = [];
  for (i = 0; i < number; i++) {
    arr.push("hi");
  }
  if (number >= 0) {
    return arr;
  } else {
    return (arr = []);
  }
}
