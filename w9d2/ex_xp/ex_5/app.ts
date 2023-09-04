import { math } from "./math";
import _ from "lodash";

const num1 = 5;
const num2 = 3;

const sum = math.add(num1, num2);
const mult = math.multiplication(num1, num2);

console.log(`Number 1: ${num1}`);
console.log(`Number 2: ${num2}`);
console.log(`Sum: ${sum}`);
console.log(`Mult: ${mult}`);

const num3 = _.random(1, 10);
const num4 = _.random(1, 10);

const sumRand = math.add(num3, num4);
const multRand = math.multiplication(num3, num4);

console.log(`Random Number 1: ${num3}`);
console.log(`Random Number 2: ${num4}`);
console.log(`Sum Random: ${sumRand}`);
console.log(`Mult Random: ${multRand}`);
