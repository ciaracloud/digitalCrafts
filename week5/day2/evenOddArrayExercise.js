//given an array, print only even numbers
//given an array, print only odd numbers
//given an array, print double of the numbers
//create a separate function for each

testArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

//even function
function printEven(array) {
  for (i = 0; i < array.length; i++) {
    if (i % 2 === 0) {
      console.log(i + 2);
    }
  }
}

printEven(testArray);

//odd function
function printOdd(array) {
  for (i = 0; i < array.length; i++) {
    if (i % 2 != 0) {
      console.log(i);
    }
  }
}

printOdd(testArray);

//double numbers
function printDouble(array) {
  for (i = 0; i < array.length; i++) {
    console.log(i + 1, i + 1);
  }
}

printDouble(testArray);
