let input = document.querySelector(".input");
let remove = document.querySelector(".remove");
let add = document.querySelector(".addButton");
let pendingTaskContainer = document.querySelector(".pendingTaskContainer");
let checkbox = document.querySelectorAll(".checkbox");
let completedTaskContainer = document.querySelector(".completedTaskContainer");
let tasks = document.querySelectorAll(".tasks");

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

for (i = 0; i < tasks.length; i++) {
  tasks[i].addEventListener("click", (e) => {
    if (e.target.checked) {
      console.log("box is checked");
      let newDiv = document.createElement("div");

      newDiv.innerText = e.target.innerText;
      completedTaskContainer.append(newDiv);
    } else {
      console.log("box is not checked");
      pendingTaskContainer.append(e);
    }
  });
}
