"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const data_1 = require("./data");
function calculateAverageAge(peopleArray) {
    const totalAge = peopleArray.reduce((sum, person) => sum + person.age, 0);
    const averageAge = totalAge / peopleArray.length;
    return averageAge;
}
const averageAge = calculateAverageAge(data_1.people);
console.log(`Average Age: ${averageAge.toFixed(2)}`);
