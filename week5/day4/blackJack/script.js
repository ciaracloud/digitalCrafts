// Select player and dealer
const deal = document.querySelector(".dealbutton");
const player = document.querySelector(".player");
const dealer = document.querySelector(".dealer");

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

let startingPlayerHand = [];
let startingDealerHand = [];

function startGame() {
  const dealerHandElement = document.createElement("img");
  const playerHandElement = document.createElement("img");
  const dealerHand = dealCards();
  const playerHand = dealCards();
  dealerHandElement.className = "dealerCards";
  dealerHandElement.src = `./images/${
    dealerHand.value
  }_of_${dealerHand.suit.toLowerCase()}.png`;
  playerHandElement.className = "playerCards";
  playerHandElement.src = `./images/${
    playerHand.value
  }_of_${playerHand.suit.toLowerCase()}.png`;
  player.append(playerHandElement);
  dealer.append(dealerHandElement);
  if (
    dealerHand.value === "Jack" ||
    dealerHand.value === "Queen" ||
    dealerHand.value === "King"
  ) {
    dealerHand.value = 10;
  } else if (dealerHand.value === "Ace") {
    dealerHand.value = 1;
  } else {
    dealerHand.value = parseInt(dealerHand.value);
  }
  if (
    playerHand.value === "Jack" ||
    playerHand.value === "Queen" ||
    playerHand.value === "King"
  ) {
    playerHand.value = 10;
  } else if (playerHand.value === "Ace") {
    playerHand.value = 1;
  } else {
    playerHand.value = parseInt(playerHand.value);
  }
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
  console.log("current player hand: ", startingPlayerHand);
  console.log("starting player total: ", startingPlayerTotal);
  console.log("current dealer hand: ", startingDealerHand);
  console.log("starting dealer total: ", startingDealerTotal);
});
