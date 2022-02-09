console.log(document);

//getElementById
//gets an element by their id name
//create variable
let button = document.getElementById("buttonid");
console.log(button);
button.innerText = "New Button";

//getElementsByClass or getElementByClass
//gets elements by their class name
let p = document.getElementsByClassName("paragraph");
console.log(p);

//querySelector or querySelectorAll
//gets an elements by class name or id name
//give (.) for class name and (#) for id name
let img = document.querySelector(".image");
console.log(img);

// in order to change the DOM,
// follow these steps:
// 1. select the element you want to change (ex. if you want to change button, select button)
// 1. select the container
// 1a. if the element does not exist, you need to create it and then you can select it
// 2. add the info to the element that you want to change/update
// 3. append it to the container you selected
// [SELECT CONTAINER, SELECT ELEMENT(S), CREATE/MODIFY ELEMENT(S), APPEND TO CONTAINER]
