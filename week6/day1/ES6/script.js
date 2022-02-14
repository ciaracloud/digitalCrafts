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

// old way to write a function (function can be redifined)
function printHi() {
  let hi = "hi";
  console.log(hi);
}

printHi = 0;

// new way adds const (so function can't be redefined)
const printHi = () => {
  let hi = "hi";
  console.log(hi);
};
