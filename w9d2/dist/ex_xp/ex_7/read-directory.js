"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const fs_1 = __importDefault(require("fs"));
const directoryPath = "./";
fs_1.default.readdir(directoryPath, (err, files) => {
    if (err) {
        console.error("Error reading directory:", err);
        return;
    }
    console.log("List of files in the directory:");
    files.forEach((file) => {
        console.log(file);
    });
});
