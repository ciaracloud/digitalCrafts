// reverse a string (using .reverse)

function dotreverse(word) {
  let splitWord = word.split("").reverse().join("");
  return console.log(splitWord);
}

// reverse a string using a for loop
function forReverseString(word) {
  let reversedWord = "";
  for (let i = word.length - 1; i >= 0; i--) {
    reversedWord += word[i];
  }
  return console.log(reversedWord);
}
