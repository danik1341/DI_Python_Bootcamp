// EX XP

// 1)

const person = {
  name: "John Doe",
  age: 25,
  location: {
    country: "Canada",
    city: "Vancouver",
    coordinates: [49.2827, -123.1207],
  },
};

const {
  name,
  location: {
    country,
    city,
    coordinates: [lat, lng],
  },
} = person;

console.log(
  `I am ${name} from ${city}, ${country}. Latitude(${lat}), Longitude(${lng})` // Output: I am John Doe from Vancouver, Canada. Latitude(49.2827), Longitude(-123.1207)
);

// The destructuring assignment extracts values from the person object and assigns them to variables.

// 2)

function displayStudentInfo(objUser) {
  const { first, last } = objUser;
  console.log(`Your full name is ${first} ${last}`);
}

displayStudentInfo({ first: "Elie", last: "Schoppik" });

// 3)

const users = { user1: 18273, user2: 92833, user3: 90315 };

const usersArray = Object.entries(users);
console.log(usersArray);

const modifiedUsersArray = usersArray.map(([user, id]) => [user, id * 2]);
console.log(modifiedUsersArray);

// 4)

class Person {
  constructor(name) {
    this.name = name;
  }
}

const member = new Person("John");
console.log(typeof member); // Output: object

// 5)

class Dog {
  constructor(name) {
    this.name = name;
  }
}

// 2
class Labrador extends Dog {
  constructor(name, size) {
    super(name);
    this.size = size;
  }
}

// 6)

// [2] === [2]: False
// Arrays are objects in JavaScript, when comparing objects you're comparing their references in memory, not their values.

// {} === {}: False
// Objects are compared by reference in JavaScript. In this case, you're comparing two separate empty object instances, and they have different memory references.

const object1 = { number: 5 };
const object2 = object1;
const object3 = object2;
const object4 = { number: 5 };

object1.number = 4;
console.log(object2.number); // Output: 4
// object1 is assigned { number: 5 }, and then its number property is changed to 4. So, object1.number is 4.
// object2 is assigned the reference to object1. Since they reference the same object in memory, any changes made to the object will reflect in both variables. Therefore, object2.number is also 4.

console.log(object3.number); // Output: 4
// Similarly, object3 is assigned the reference to object2, which in turn references the same object as object1. So, object3.number is also 4.

console.log(object4.number); // Output: 5
// object4 is assigned a new object { number: 5 }. This is a separate object from the others. Its number property remains 5.

// 7)

class Animal {
  constructor(name, type, color) {
    this.name = name;
    this.type = type;
    this.color = color;
  }
}

class Mamal extends Animal {
  constructor(name, type, color) {
    super(name, type, color);
  }

  sound(animalSound) {
    return `Moooo I'm a ${this.type}, named ${this.name} and I'm ${this.color}`;
  }
}

const farmerCow = new Mamal("Lily", "cow", "brown and white");
const cowSound = farmerCow.sound();
console.log(cowSound);
