// ONE
//const functionName = (word) => `hello ${word}`;

// TWO
// functionMath(5)(6) => 30
const functionMath = (firstNumber) => {
  return function (second) {
    return second * firstNumber;
  };
  // return (second) => {
  //   return second * firstNumber;
  // };
};

// THREE
// const longWord = "yrhnyyn";
// const test = {
//   y: 3,
//   r: 1,
//   h: 1,
//   n: 2,
// };

function loopdeloop(longWord) {
  let newObj = {};
  for (const letter of longWord) {
    console.log(letter);
    if (letter in newObj) {
      newObj = { ...newObj, [letter]: newObj[letter] + 1 };
    } else {
      newObj = {
        ...newObj,
        [letter]: 1,
      };
    }
  }
  return newObj;
}
loopdeloop(longWord);

// FOUR
const Animal = {};

const chicken = {
  height: "123ft",
  species: "chicken",
};
const dog = {
  species: "dog",
  fur: 20,
  color: "red",
};
