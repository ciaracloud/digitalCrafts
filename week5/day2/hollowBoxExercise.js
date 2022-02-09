//make a function that prints a hollow box with the width and height that it is given

function printBox(width, height) {
  let str = "";
  for (i = 0; i < width; i++) {
    str += "-";
  }
  console.log(str);
  let str2 = "";
  for (j = 0; j < width; j++) {
    if (j === 0 || j === width - 1) {
      str2 += "|";
    } else {
      str2 += " ";
    }
  }
  for (k = 0; k < height; k++) {
    console.log(str2);
  }
  console.log(str);
}

printBox(5, 6);
