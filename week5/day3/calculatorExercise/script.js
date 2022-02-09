let buttons = document.querySelectorAll(".buttons");
console.log(buttons);
let numbers = document.querySelectorAll(".numbers");
console.log(numbers);
let operands = document.querySelectorAll(".operands");
console.log(operands);
let clear = document.querySelector(".clear");
console.log(clear);

let equation = [];

function doTheMath() {
  operation = equation[1];
  if (equation.length === 4) {
    if (operation === "+" && equation[3] === "=") {
      console.log(equation[0] + equation[2]);
    } else if (operation === "-" && equation[3] === "=") {
      console.log(equation[0] - equation[2]);
    } else if (operation === "/" && equation[3] === "=") {
      console.log(equation[0] / equation[2]);
    } else if (operation === "*" && equation[3] === "=") {
      console.log(equation[0] * equation[2]);
    }
    equation = [];
    console.log("this is the list now:", equation);
  }
}

for (i = 0; i < numbers.length; i++) {
  numbers[i].addEventListener("click", (e) => {
    let numberInnerText = parseInt(e.target.innerText);
    equation.push(numberInnerText);
    console.log("this is the current list:", equation);
    doTheMath();
  });
}

for (i = 0; i < operands.length; i++) {
  operands[i].addEventListener("click", (e) => {
    let operandInnerText = e.target.innerText;
    equation.push(operandInnerText);
    console.log("this is the current list:", equation);
    doTheMath();
  });
}

clear.addEventListener("click", (e) => {
  equation = [];
  console.log("this is the current list", equation);
});
