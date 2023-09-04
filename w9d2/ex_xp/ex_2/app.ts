import { people } from "./data";

function calculateAverageAge(
  peopleArray: Array<{ name: string; age: number; location: string }>
): number {
  const totalAge = peopleArray.reduce((sum, person) => sum + person.age, 0);
  const averageAge = totalAge / peopleArray.length;
  return averageAge;
}

const averageAge = calculateAverageAge(people);
console.log(`Average Age: ${averageAge.toFixed(2)}`);
