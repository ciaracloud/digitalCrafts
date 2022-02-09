//SPREAD OPERATOR
//combines arrays/objects, but allows values/key:value pairs to remain separate

let array1 = ["hi"];
let array2 = ["howdy"];
let array3 = [...array1, ...array2];
let object1 = { name: "Joe" };
let object2 = { height: "6.1" };
let object3 = { ...object1, ...object2 };

console.log(array3);
console.log(object3);

//can't spread objects into array
//can spread objects into objects
//if you do not declare a key for object, the value becomes the key
