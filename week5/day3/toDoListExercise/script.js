let input = document.querySelector(".input");
let remove = document.querySelector(".remove");
let add = document.querySelector(".addButton");
let pendingTaskContainer = document.querySelector(".pendingTaskContainer");
let checkbox = document.querySelectorAll(".checkbox");
let completedTaskContainer = document.querySelector(".completedTaskContainer");
let tasks = document.querySelectorAll(".tasks");
let taskTitles = document.querySelectorAll(".taskTitles");
let taskContents = document.querySelectorAll(".tasks").childNodes;

taskList = [];

add.addEventListener("click", (e) => {
  let newDiv = document.createElement("div");
  newDiv.className = "tasks";
  let inputTag = document.createElement("input");
  inputTag.type = "checkbox";
  inputTag.className = "checkbox";
  let paragraphTag = document.createElement("p");
  paragraphTag.innerText = input.value;
  let buttonTag = document.createElement("button");
  buttonTag.className = "remove";
  buttonTag.innerText = "Remove";
  newDiv.append(inputTag);
  newDiv.append(paragraphTag);
  newDiv.append(buttonTag);
  console.log(newDiv);
  pendingTaskContainer.append(newDiv);
  input.value = "";
});

for (i = 0; i < tasks.length; i++) {
  tasks[i].addEventListener("click", (e) => {
    if (e.target.checked) {
      console.log("box is checked");
      let newDiv = document.createElement("div");
      newDiv.className = "tasks";
      let inputTag = document.createElement("input");
      inputTag.type = "checkbox";
      inputTag.className = "checkbox";
      let paragraphTag = document.createElement("p");
      paragraphTag.innerText = "this is a completed task";
      let buttonTag = document.createElement("button");
      buttonTag.className = "remove";
      buttonTag.innerText = "Remove";
      newDiv.append(inputTag);
      newDiv.append(paragraphTag);
      newDiv.append(buttonTag);
      completedTaskContainer.append(newDiv);
    } else {
      console.log("box is checked");
      let newDiv = document.createElement("div");
      newDiv.className = "tasks";
      let inputTag = document.createElement("input");
      inputTag.type = "checkbox";
      inputTag.className = "checkbox";
      let paragraphTag = document.createElement("p");
      paragraphTag.innerText = "this is a pending task";
      let buttonTag = document.createElement("button");
      buttonTag.className = "remove";
      buttonTag.innerText = "Remove";
      newDiv.append(inputTag);
      newDiv.append(paragraphTag);
      newDiv.append(buttonTag);
      pendingTaskContainer.append(newDiv);
    }
  });
}
