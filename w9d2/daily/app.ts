import { greet } from "./greeting";
import { createColorfulMessage } from "./colorful-message";
import { readFile } from "./read-file";

const userName = "Daniel";

const greetingMsg = greet(userName);
console.log(greetingMsg);

const colorfulMessage = createColorfulMessage();
console.log(colorfulMessage);

const readText = async () => {
  try {
    const filePath = "daily/files/file-data.txt";
    const fileData = await readFile(filePath);
    console.log("====================================");
    console.log("File Data:");
    console.log("====================================");
    console.log(fileData);
  } catch (err) {
    console.error("Error reading the file:", err);
  }
};

readText();
