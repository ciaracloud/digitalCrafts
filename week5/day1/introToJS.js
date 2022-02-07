function printAUser(user) {
  console.log(user);
}

// Exercise 1:
// create a function that prints out the product of 2 numbers
// return the product of those two numbers
// store the function return value in a variable
// print that variable

function productOfNumbers() {
  return 1 * 2;
}

let printProduct = productOfNumbers();
console.log(printProduct);

// Exercise 2:
// define a function that takes in two arguments
// those arguments will be numbers or have a type of integer
// divide the first number by the second number
// print the result

function quotientOfNumbers(number1, number2) {
  return number1 / number2;
}

let printQuotient = quotientOfNumbers();
console.log(printQuotient);

// OR

function quotientOfNumbers(number1, number2) {
  console.log(number1 / number2);
}

// Exercise 3:
// create a function that takes your first name and last name as arguments
// find out how to make your first name and last name
// uppercased
// return to me the values of your first and last name in this format
// "I AM {firstName} {lastName}, I am from Tomball"

function fullName1(firstName, lastName) {
  let upperFirstName = firstName.charAt(0).toUpperCase() + firstName.slice(1);
  let upperLastName = lastName.charAt(0).toUpperCase() + lastName.slice(1);
  console.log(`I AM ${upperFirstName} ${upperLastName}, I am from Tampa`);
}
