import fs from "fs";

const sourceFilePath = "ex_xp/ex_7/source.txt";
const destinationFilePath = "ex_xp/ex_7/destination.txt";

fs.readFile(sourceFilePath, "utf8", (err, data) => {
  if (err) {
    console.error("Error reading source file:", err);
    return;
  }

  fs.writeFile(destinationFilePath, data, "utf8", (err) => {
    if (err) {
      console.error("Error writing to destination file:", err);
      return;
    }

    console.log("Content copied from source.txt to destination.txt.");
  });
});
