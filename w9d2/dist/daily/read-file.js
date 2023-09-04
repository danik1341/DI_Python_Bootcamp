"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.readFile = void 0;
const fs_1 = __importDefault(require("fs"));
const readData = "daily/files/file-data.txt";
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
const readFile = (filePath) => {
    return new Promise((res, rej) => {
        fs_1.default.readFile(filePath, "utf-8", (err, data) => {
            if (err) {
                rej(err);
            }
            else {
                res(data);
            }
        });
    });
};
exports.readFile = readFile;
