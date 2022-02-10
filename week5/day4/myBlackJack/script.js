let dealButton = document.querySelector(".dealButton");

function dealCards() {
  let randomSuit = Math.floor(Math.random() * suitOptions.length);
  let randomCard = Math.floor(Math.random() * cardOptions.length);
  let randomFinalCard = suitOptions[randomSuit] + " " + cardOptions[randomCard];
  console.log(randomFinalCard);
}

suitOptions = ["Clubs", "Diamonds", "Hearts", "Spades"];
cardOptions = [
  "Ace",
  "2",
  "3",
  "4",
  "5",
  "6",
  "7",
  "8",
  "9",
  "10",
  "Jack",
  "Queen",
  "King",
];

function dealOnceForBoth() {
  let dealForPlayer = dealCards();
  let dealForDealer = dealCards();
}

counter = 0;
dealButton.addEventListener("click", () => {
  counter += 1;
  if (counter === 1) {
    dealOnceForBoth();
    dealOnceForBoth();
  } else {
    console.log("player's turn");
  }
});
