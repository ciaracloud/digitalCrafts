let buttons = document.querySelectorAll(".buttons");

function getNumber(e) {
  num = e.target.innerText;
  console.log(num);
}

for (let i = 0; i < buttons.length; i++) {
  buttons[i].addEventListener("click", (e) => {
    getNumber(e);
  });
}
