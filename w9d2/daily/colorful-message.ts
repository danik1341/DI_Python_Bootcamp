import chalk from "chalk";

export function createColorfulMessage() {
  const colorfulMessage = chalk.bold
    .rgb(255, 0, 0)
    .bgWhite("Hello, colorful world!");
  return colorfulMessage;
}
