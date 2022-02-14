//---------------------------- {CLASSES IN JS} ---------------------------------

// class
class Student {
  constructor(name, height, age) {
    this.name = name;
    this.height = height;
    this.age = age;
  }
  greet() {
    return `${this.name} says hello!`;
  }
}

// inheriting from first class
class SuperStudent extends Student {
  constructor(title) {
    super(title); // needs super with the argument that is different
    this.title = title;
  }
  greet() {
    console.log(this.title);
  }
}

const Kiwi = new Student("Kiwi", "1", "2");
const Matt = new SuperStudent("TA");
console.log(Kiwi);
console.log(Kiwi.name);
console.log(Ciara.greet());
Matt.greet();
