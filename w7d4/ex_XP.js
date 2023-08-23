// EX XP

// 1)

const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];

colors.forEach((color, index) => {
  console.log(`${index + 1} choice is ${color}.`);
});

colors.includes("Violet") ? console.log("Yeah") : console.log("No.....");

// 2)

const ordinal = ["th", "st", "nd", "rd"];

colors.forEach((color, index) => {
  const ordinalIndex = index + 1 > 3 ? 0 : index + 1;
  const ordinalSuffix = ordinal[ordinalIndex];
  console.log(`${index + 1}${ordinalSuffix} choice is ${color}.`);
});

// 3)

// ------1------
// const fruits = ["apple", "orange"];
// const vegetables = ["carrot", "potato"];

// const result = ["bread", ...vegetables, "chicken", ...fruits];
// console.log(result); [ 'bread', 'carrot', 'potato', 'chicken', 'apple', 'orange' ]
// because of the speard operator

// ------2------
// const country = "USA";
// console.log([...country]); [ 'U', 'S', 'A' ]
// because of the speard operator, the string is counted as an array of chars

// ------Bonus------
// let newArray = [...[, ,]];
// console.log(newArray); [ undefined, undefined ]
// the spread operator spreads nothing as there is nothing to spread and then there an array with two undifined values

// 4)

const users = [
  { firstName: "Bradley", lastName: "Bouley", role: "Full Stack Resident" },
  { firstName: "Chloe", lastName: "Alnaji", role: "Full Stack Resident" },
  { firstName: "Jonathan", lastName: "Baughn", role: "Enterprise Instructor" },
  { firstName: "Michael", lastName: "Herman", role: "Lead Instructor" },
  { firstName: "Robert", lastName: "Hajek", role: "Full Stack Resident" },
  { firstName: "Wes", lastName: "Reid", role: "Instructor" },
  { firstName: "Zach", lastName: "Klabunde", role: "Instructor" },
];

const welcomeStudents = users.map((user) => `Hello ${user.firstName}`);
console.log(welcomeStudents);

const fullStackResident = users.filter(
  (user) => user.role === "Full Stack Resident"
);

console.log(fullStackResident);

const fullStackResidentsLastNames = users
  .filter((user) => user.role === "Full Stack Resident")
  .map((user) => user.lastName);

console.log(fullStackResidentsLastNames);

// 5)

const epic = ["a", "long", "time", "ago", "in a", "galaxy", "far far", "away"];
const combinedString = epic.reduce(
  (accumulator, currentValue) => accumulator + " " + currentValue
);

console.log(combinedString);

// 6)

const students = [
  { name: "Ray", course: "Computer Science", isPassed: true },
  { name: "Liam", course: "Computer Science", isPassed: false },
  { name: "Jenner", course: "Information Technology", isPassed: true },
  { name: "Marco", course: "Robotics", isPassed: true },
  { name: "Kimberly", course: "Artificial Intelligence", isPassed: false },
  { name: "Jamie", course: "Big Data", isPassed: false },
];

const passed = students.filter((student) => student.isPassed);
console.log(passed);

const mazalTov = passed.forEach((student) => {
  console.log(
    `Good job ${student.name}!, you passed the course in ${student.course}`
  );
});
