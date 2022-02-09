//write a function that prints a border around given text with "-"

function printBanner(string) {
  let str = "";
  for (i = 0; i < string.length; i++) {
    str += "-";
  }
  console.log(str + "-" + "-");
  console.log(`-${string}-`);
  console.log(str + "-" + "-");
}

printBanner("Welcome to Digital Crafts");
