// Daily Challenge: Not Bad

const sentence = "The movie is not that bad, I like it";
console.log(sentence);

const wordNot = sentence.indexOf("not");
console.log("Position of 'not':", wordNot);

const wordBad = sentence.indexOf("bad");
console.log("Position of 'bad':", wordBad);

if (wordNot !== -1 && wordBad !== -1 && wordBad > wordNot) {
    const modifiedSentence = sentence.slice(0, wordNot) + "good" + sentence.slice(wordBad + 3);
    console.log("Modified sentence:", modifiedSentence);
  } else {
    console.log("No modification needed:", sentence);
  }

const sentence1 = 'This dinner is not that bad ! You cook well';
const sentence2 = 'This movie is not so bad !';
const sentence3 = 'This dinner is bad !';

function replaceNotBadWithGood(inputSentence) {
    const wordNot = inputSentence.indexOf("not");
    const wordBad = inputSentence.indexOf("bad");
  
    if (wordNot !== -1 && wordBad !== -1 && wordBad > wordNot) {
      const modifiedSentence = inputSentence.slice(0, wordNot) + "good" + inputSentence.slice(wordBad + 3);
      return modifiedSentence;
    } else {
      return inputSentence;
    }
}

console.log("Original sentence:", sentence1);
console.log("Modified sentence:", replaceNotBadWithGood(sentence1));
console.log("");

console.log("Original sentence:", sentence2);
console.log("Modified sentence:", replaceNotBadWithGood(sentence2));
console.log("");

console.log("Original sentence:", sentence3);
console.log("Modified sentence:", replaceNotBadWithGood(sentence3));