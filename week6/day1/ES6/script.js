// ES6

// ---------------------- {DECLARING VARIABLES} ----------------------------
// block scope
// this variable is defined at a global level

// use const for global
const variableName = { name: "Ciara" };

// use let for local
function printHi() {
  let hi = "hi";
  console.log(hi);
}

//------------------------- {FUNCTIONS IN ES6} -----------------------------

// first way to write a function (function can be redefined)
// GETS ACCESS TO 'this'
function printHi() {
  let hi = "hi";
  console.log(hi);
}

printHi = 0;

// second way to write a function (called arrow function)
// adds const (function can't be redefined)
// DOESN'T GET ACCES TO 'this'
const printHi = () => {
  let hi = "hi";
  console.log(hi);
};

//-----------------------------{SETS & MAPS}--------------------------------------

// declare a set - can't have duplicates in a set
// set can't have duplicate keys or values
const names = new Set();
console.log(names);

// declare a map
const mapName = new Map();
console.log(mapName);

//----------------------------{DESTRUCTURING}-------------------------------------

const Kiwi = {
  name: "kiwi",
  age: "2",
  height: "1",
};

let name = Kiwi.name;
let age = Kiwi.age;
let height = Kiwi.height;

// syntactic sugar - ways to define, must use the name of the keys
// use a for loop to get access to multiple names, ages, heights
const { name, age, height } = Kiwi;

//----------------------------{LOOPS}---------------------------------------------

// for - used for arrays
for (let index = 0; index < li; index++) {}

// for of - used for arrays
for (let student of array) {
}

// for each - used for arrays
listName.forEach((element) => console.log(element));

// for in - used for objects
for (let student in object) {
}
