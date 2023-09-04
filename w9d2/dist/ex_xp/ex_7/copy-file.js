"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const fs_1 = __importDefault(require("fs"));
const sourceFilePath = "ex_xp/ex_7/source.txt";
const destinationFilePath = "ex_xp/ex_7/destination.txt";
fs_1.default.readFile(sourceFilePath, "utf8", (err, data) => {
    if (err) {
        console.error("Error reading source file:", err);
        return;
    }
    fs_1.default.writeFile(destinationFilePath, data, "utf8", (err) => {
        if (err) {
            console.error("Error writing to destination file:", err);
            return;
        }
        console.log("Content copied from source.txt to destination.txt.");
    });
});
