let input = document.querySelector(".input");
let remove = document.querySelector(".remove");
let add = document.querySelector(".addButton");
let pendingTaskContainer = document.querySelector(".pendingTaskContainer");
console.log(pendingTaskContainer);
let checkbox = document.querySelectorAll(".checkbox");
console.log(checkbox);
let cb1 = document.querySelector(".cb1");
let cb2 = document.querySelector(".cb2");
let cb3 = document.querySelector(".cb3");
let cb4 = document.querySelector(".cb4");
let cb5 = document.querySelector(".cb5");

input.addEventListener("click", (e) => {
  input.value = "";
});

taskList = [];

// add.addEventListener("click", (e) => {
//   taskList.push(input.value);
//   console.log("this is the task array:", taskList);
// });

add.addEventListener("click", (e) => {
  pendingTaskContainer.append(input.value);
  console.log(pendingTaskContainer);
});

for (i = 0; i < checkbox.length; i++) {
  checkbox[i].addEventListener("click", (e) => {
    for (j = 0; j < checkbox.length; j++)
      if (cb1.checked) {
        console.log("box1 is checked");
      } else {
        console.log("box1 is not checked");
      }
  });
}
