import fs from "fs";

// export const readFile = fs.readFile(readData, (err, data) => {
//   if (err) {
//     console.error("Error reading source file:", err);
//     return;
//   }
//   console.log("====================================");
//   console.log("File Data:");
//   console.log("====================================");
//   console.log(data);
// });

export const readFile = (filePath: string): Promise<string> => {
  return new Promise((res, rej) => {
    fs.readFile(filePath, "utf-8", (err, data) => {
      if (err) {
        rej(err);
      } else {
        res(data);
      }
    });
  });
};
