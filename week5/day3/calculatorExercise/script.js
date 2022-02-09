let buttons = document.querySelectorAll(".buttons");
console.log(buttons);
let numbers = document.querySelectorAll(".numbers");
console.log(numbers);
let operands = document.querySelectorAll(".operands");
console.log(operands);

let equation = [];

for (i = 0; i < numbers.length; i++) {
  numbers[i].addEventListener("click", (e) => {
    let numberInnerText = parseInt(e.target.innerText);
    equation.push(numberInnerText);
    console.log("this is the current list:", equation);
  });
}

for (i = 0; i < operands.length; i++) {
  operands[i].addEventListener("click", (e) => {
    let operandInnerText = e.target.innerText;
    equation.push(operandInnerText);
    console.log("this is the current list:", equation);
  });
}
