// Select player and dealer
const deal = document.querySelector(".dealButton");
const player = document.querySelector(".player");
const dealer = document.querySelector(".dealer");
const otherButtonsContainer = document.querySelector(".otherButtons");

const cardList = [
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
const cardSuits = ["Spades", "Diamonds", "Clubs", "Hearts"];

function dealCards() {
  const hand2 = {
    suit: "",
    value: "",
  };
  const randomSuit = Math.floor(Math.random() * cardSuits.length);
  const randomCardList = Math.floor(Math.random() * cardList.length);
  hand2.suit = cardSuits[randomSuit];
  //   add your conditional
  hand2.value = cardList[randomCardList];
  return hand2;
}

function convertStrings(playerObject, dealerObject) {
  if (
    dealerObject.value === "Jack" ||
    dealerObject.value === "Queen" ||
    dealerObject.value === "King"
  ) {
    dealerObject.value = 10;
  } else if (dealerObject.value === "Ace") {
    dealerObject.value = 1;
  } else {
    dealerObject.value = parseInt(dealerObject.value);
  }
  if (
    playerObject.value === "Jack" ||
    playerObject.value === "Queen" ||
    playerObject.value === "King"
  ) {
    playerObject.value = 10;
  } else if (playerObject.value === "Ace") {
    playerObject.value = 1;
  } else {
    playerObject.value = parseInt(playerObject.value);
  }
}

let startingPlayerHand = [];
let startingDealerHand = [];

function addPlayerImages(playerObject) {
  const playerHandElement = document.createElement("img");
  playerHandElement.className = "playerCards";
  playerHandElement.src = `./images/${
    playerObject.value
  }_of_${playerObject.suit.toLowerCase()}.png`;
  player.append(playerHandElement);
}

function addDealerImages(dealerObject) {
  const dealerHandElement = document.createElement("img");
  dealerHandElement.className = "dealerCards";
  dealerHandElement.src = `./images/${
    dealerObject.value
  }_of_${dealerObject.suit.toLowerCase()}.png`;
  dealer.append(dealerHandElement);
}

// function addImagesToScreen(playerObject, dealerObject) {
//   const dealerHandElement = document.createElement("img");
//   const playerHandElement = document.createElement("img");
//   dealerHandElement.className = "dealerCards";
//   dealerHandElement.src = `./images/${
//     dealerObject.value
//   }_of_${dealerObject.suit.toLowerCase()}.png`;
//   playerHandElement.className = "playerCards";
//   playerHandElement.src = `./images/${
//     playerObject.value
//   }_of_${playerObject.suit.toLowerCase()}.png`;
//   player.append(playerHandElement);
//   dealer.append(dealerHandElement);
// }

function startGame() {
  const dealerHand = dealCards();
  const playerHand = dealCards();
  addPlayerImages(playerHand);
  addDealerImages(dealerHand);
  convertStrings(playerHand, dealerHand);
  startingDealerHand.push(dealerHand);
  startingPlayerHand.push(playerHand);
  console.log("dealer hand this round: ", dealerHand);
  console.log("player hand this round: ", playerHand);
}

deal.addEventListener("click", () => {
  startGame();
  startGame();
  let startingPlayerTotal =
    startingPlayerHand[0].value + startingPlayerHand[1].value;
  let startingDealerTotal =
    startingDealerHand[0].value + startingDealerHand[1].value;
  let playerTotalElement = document.createElement("p");
  let dealerTotalElement = document.createElement("p");
  playerTotalElement.innerText = `Player's starting total is: ${startingPlayerTotal}`;
  dealerTotalElement.innerText = `Dealer's starting total is: ${startingDealerTotal}`;
  player.append(playerTotalElement);
  dealer.append(dealerTotalElement);
  let hitButton = document.createElement("button");
  hitButton.innerText = "HIT";
  hitButton.className = "hitButton";
  let standButton = document.createElement("button");
  standButton.innerText = "STAND";
  standButton.className = "standButton";
  otherButtonsContainer.append(hitButton);
  otherButtonsContainer.append(standButton);
  deal.remove();
  console.log("current player hand: ", startingPlayerHand);
  console.log("starting player total: ", startingPlayerTotal);
  console.log("current dealer hand: ", startingDealerHand);
  console.log("starting dealer total: ", startingDealerTotal);
  hitButton.addEventListener("click", () => {
    const playerHand = dealCards();
    addPlayerImages(playerHand);
    convertStrings(playerHand, "");
    console.log("this is my hand this round: ", playerHand);
    startingPlayerHand.push(playerHand);
    console.log("this is my hand now: ", startingPlayerHand);
  });
});
