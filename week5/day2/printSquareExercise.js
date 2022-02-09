//write a function that is given a size and prints a square in that size with "-"

function printSquare(number) {
  for (i = 0; i < number; i++) {
    let str = "";
    for (j = 0; j < number; j++) {
      str += "-";
    }
    console.log(str);
  }
}

printSquare(5);
