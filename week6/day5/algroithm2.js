// fizz buzz
// fizz
// buzz
// if a number is divisible by 2, print fizz, if by 5, print buzz, if by both print fizzbuzz

const number = 10;
const fizzBuzz = (number) => {
  if (number % 2 == 0 && number % 5 == 0) {
    console.log("fizz buzz");
  } else if (number % 5 == 0) {
    console.log("buzz");
  } else if (number % 2 == 0) {
    console.log("fizz");
  } else {
    console.log("not divisible by 2 or 5");
  }
};
