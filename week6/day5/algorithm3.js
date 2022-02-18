myArray = [7, 1, 5, 3, 6, 4];

for (i = myArray.length - 1; i > -1; i--) {
  for (counter = 0; i < myArray.length; i++) {
    const result = myArray[i] - myArray[counter];
    console.log(result);
  }
}
