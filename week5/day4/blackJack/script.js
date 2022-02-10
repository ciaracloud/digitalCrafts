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
  const hand = {
    suit: "",
    value: "",
  };
  const randomSuit = Math.floor(Math.random() * cardSuits.length);
  const randomCardList = Math.floor(Math.random() * cardList.length);
  hand.suit = cardSuits[randomSuit];
  //   add your conditional
  hand.value = cardList[randomCardList];
  // if (hand.value === "Jack") {
  //   hand.value = 10;
  // } else if (hand.value === "Queen") {
  //   hand.value = 10;
  // } else if (hand.value === "King") {
  //   hand.value = 10;
  // }
  // console.log("this is the value of the card", hand.value);
  // return hand;
}

function startGame() {
  const dealerHandImage = document.createElement("img");
  const playerHandImage = document.createElement("img");
  const dealerHand = dealCards();
  const playerHand = dealCards();
  dealerHandImage.className = "dealerCards";
  dealerHandImage.src = `./images/${
    dealerHand.value
  }_of_${dealerHand.suit.toLowerCase()}.png`;
  playerHandImage.className = "playerCards";
  playerHandImage.src = `./images/${
    playerHand.value
  }_of_${playerHand.suit.toLowerCase()}.png`;
  player.append(playerHandImage);
  dealer.append(dealerHandImage);
  console.log("this is the dealer hand:", dealerHand);
  console.log("this is the player hand:", playerHand);
}

// counter = 0;
deal.addEventListener("click", () => {
  // // counter += 1;
  // if (counter === 1) {
  startGame();
  // } else {
  //   console.log("player's turn");
  // }
});
