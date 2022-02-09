// array (list) []

let studentNames = ["Ciara", "Kiwi"];
studentNames[0];

// objects (dictionary) {}

let student = {
    name: "ciara"
}
console.log(student["name"])
console.log(student.name)
// while loop

while (condition is true) {

}

// for loop (original syntax for arrays)

for (let index = 0; index < array.length; index++) {
    const element = array[index];
    
}

// for...in loop (for objects)

for (const key in object) {
    if (Object.hasOwnProperty.call(object, key)) {
        const element = object[key];
        
    }
}

let accountDetails = {
    name: "Ciara",
    city: "Tampa"
}

for(const key in accountDetails) {
    console.log(accountDetails[key]);
}

// for...of loop (for arrays)

for (const iterator of object) {
    
}

const houses = ["123 Main St", "1224 Town Square"]

for (const house of houses) {
    console.log(house)
}

// .map (for loop used for arrays, loops over array, creates it's own empty array)

const dcInstructors = ["Ciara", "Kiwi", "Taylor"];
console.log(dcInstructors);
const dcInstructorsUpper = dcInstructors.map((instructor) => instructor.toUpperCase());

const complicatedExample = dcInstructors.map(function (element, index) {
  const newElement = element + index;
  return newElement.toUpperCase();
});
console.log(complicatedExample);