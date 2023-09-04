import * as fs from "fs";

export const readFile = (filePath: string): Promise<string> => {
  return new Promise((res, rej) => {
    fs.readFile(filePath, "utf8", (err, data) => {
      if (err) {
        rej(err);
      } else {
        res(data);
      }
    });
  });
};

export const writeFile = (filePath: string, content: string): Promise<void> => {
  return new Promise((res, rej) => {
    fs.writeFile(filePath, content, "utf8", (err) => {
      if (err) {
        rej(err);
      } else {
        res();
      }
    });
  });
};
