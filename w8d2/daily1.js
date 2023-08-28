// Daily: Play with words

// 1)

const makeAllCaps = (arr) => {
  return new Promise((resolve, reject) => {
    if (arr.every((word) => typeof word === "string")) {
      const uppercaseArr = arr.map((word) => word.toUpperCase());
      resolve(uppercaseArr);
    } else {
      reject("All elements in the array must be strings.");
    }
  });
};

const sortWords = (uppercasedArr) => {
  return new Promise((resolve, reject) => {
    if (uppercasedArr.length > 4) {
      const sortedArr = uppercasedArr.sort();
      resolve(sortedArr);
    } else {
      reject("Array length must be bigger than 4.");
    }
  });
};

// Test cases

makeAllCaps([1, "pear", "banana"])
  .then((arr) => sortWords(arr))
  .then((result) => console.log(result))
  .catch((error) => console.log(error)); // Output: "All elements in the array must be strings."

makeAllCaps(["apple", "pear", "banana"])
  .then((arr) => sortWords(arr))
  .then((result) => console.log(result))
  .catch((error) => console.log(error)); // Output: "Array length must be bigger than 4."

makeAllCaps(["apple", "pear", "banana", "melon", "kiwi"])
  .then((arr) => sortWords(arr))
  .then((result) => console.log(result))
  .catch((error) => console.log(error)); // Output: ["APPLE","BANANA", "KIWI", "MELON", "PEAR"]

// 2)
var prompt = require("prompt-sync")();

const morse = `{
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
  }`;

const toJs = () => {
  return new Promise((resolve, reject) => {
    try {
      const morseObject = JSON.parse(morse);
      if (Object.keys(morseObject).length === 0) {
        reject("Morse object is empty.");
      } else {
        resolve(morseObject);
      }
    } catch (err) {
      reject(err);
    }
  });
};

const toMorse = (morseJS) => {
  return new Promise((resolve, reject) => {
    const userInput = prompt("Enter a word or sentence:");
    const words = userInput.toLocaleLowerCase().split(" ");

    const morseTranslation = words.map((word) => {
      const chars = [...word];
      const morseChars = chars.map((char) => morseJS[char] || "");
      if (morseChars.includes("")) {
        reject(`Character not found: ${char}`);
      }
      return morseChars.join(" ");
    });
    resolve(morseTranslation);
  });
};

const joinWords = (morseTranslation) => {
  const joinedMorse = morseTranslation.join("\n");
  console.log(joinedMorse);
};

toJs()
  .then((morseJS) => toMorse(morseJS))
  .then((morseTranslation) => joinWords(morseTranslation))
  .catch((error) => console.log(error));
