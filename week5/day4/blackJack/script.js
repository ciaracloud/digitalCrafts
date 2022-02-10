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
}

deal.addEventListener("click", () => {
  startGame();
});
