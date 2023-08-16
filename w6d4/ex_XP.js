// EX XP

// 1)

const people = ["Greg", "Mary", "Devon", "James"];

const personToRemove = 'Greg';
const index = people.indexOf(personToRemove);
people.splice(index, 1);
console.log(people); // Output:  ['Mary', 'Devon', 'James']

people[people.indexOf('James')] = 'Jason'
console.log(people); // Output:  ['Mary', 'Devon', 'Jason']

people.push('Daniel');
console.log(people); // Output:  ['Mary', 'Devon', 'Jason', 'Daniel']

console.log(`Marry is at index -> ${people.indexOf('Mary')}`); // Output:  Marry is at index -> 0

console.log(`Foo is at index -> ${people.indexOf('Foo')}`); // Output: Foo is at index -> -1
//It return -1 as "Foo" is not a value in our array so its index is out of bounds, or none existing

var last = people[people.length - 1];
console.log(`Last value in the array is -> ${last}`); // Output: Last value in the array is -> Daniel

people.forEach(person => {
    console.log(person)
})

for (let i = 0; i < people.length; i++) {
    if (people[i] === "Devon") {
      console.log(people[i]);
      break;
    }
    console.log(people[i]);
  }

// 2)

const colors = ['red', 'black', 'purple', 'dark blue', 'grey']

for (let i = 0; i < colors.length;  i++){
    console.log(`My #${i + 1} choice is ${colors[i]}`)
}

const suffixes = ['st', 'nd', 'rd', 'th', 'th'];
for (let i = 0; i < colors.length; i++) {
  const suffixIndex = i < 4 ? i : 4;
  console.log(`My ${i + 1}${suffixes[suffixIndex]} choice: ${colors[i]}`);
}

// 3)

const userInput = prompt("Please enter a number:");
console.log("User input:", userInput);
console.log("Data type:", typeof userInput);
const numericValue = parseFloat(userInput);
console.log("Parsed as a number:", numericValue);
console.log("Data type after parsing:", typeof numericValue);

while (true) {
    const userInput = prompt("Please enter a number:");

    const numericValue = parseFloat(userInput);

    if(!isNaN(numericValue)){
        if(numericValue < 10 ){
            console.log("Number is smaller than 10. Please enter a new number.");
        } else {
            console.log("Number is not smaller than 10. Exiting loop.");
            break;
        }
    } else {
        console.log("Invalid input. Please enter a valid number.");
    }
}

// 4)

const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}

console.log(`Number Of Floors: ${building.numberOfFloors}`)

console.log("Number of apartments on the first floor:", building.numberOfAptByFloor.firstFloor);
console.log("Number of apartments on the third floor:", building.numberOfAptByFloor.thirdFloor);

console.log("Name of the second tenant:", building.nameOfTenants[1]);
const secondTenant = building.nameOfTenants[1].toLowerCase();
console.log("Number of rooms for the second tenant:", building.numberOfRoomsAndRent[secondTenant][0]);

const sarahRent = building.numberOfRoomsAndRent.sarah[1];
const davidRent = building.numberOfRoomsAndRent.david[1];
const danRent = building.numberOfRoomsAndRent.dan[1];
const sumOfSarahAndDavidRent = sarahRent + davidRent;

if (sumOfSarahAndDavidRent > danRent) {
    building.numberOfRoomsAndRent.dan[1] = 1200;
    console.log("Dan's rent has been increased to 1200.");
  } else {
    console.log("No change to Dan's rent needed.");
  }

// 5)

const family = {
    father: "John",
    mother: "Jane",
    son: "Michael",
    daughter: "Emily"
};

console.log("Keys of the family object:");
for (const key in family) {
    console.log(key);
}

console.log("\nValues of the family object:");
for (const key in family) {
    console.log(family[key]);
}

// 6)

const details = {
    my: 'name',
    is: 'Rudolf',
    the: 'raindeer'
  }

let sentence = '';

for (const key in details) {
    sentence += key === 'my' ? 'my ' + details[key] + ' ' : key + ' ' + details[key] + ' ';
  }

console.log(sentence.trim());

// 7)

const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

const societyName = names
  .map(name => name[0]) 
  .sort()               
  .join(''); 

console.log("Secret Society's Name:", societyName);