"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", { value: true });
const greeting_1 = require("./greeting");
const colorful_message_1 = require("./colorful-message");
const read_file_1 = require("./read-file");
const userName = "Daniel";
const greetingMsg = (0, greeting_1.greet)(userName);
console.log(greetingMsg);
const colorfulMessage = (0, colorful_message_1.createColorfulMessage)();
console.log(colorfulMessage);
const readText = () => __awaiter(void 0, void 0, void 0, function* () {
    try {
        const filePath = "daily/files/file-data.txt";
        const fileData = yield (0, read_file_1.readFile)(filePath);
        console.log("====================================");
        console.log("File Data:");
        console.log("====================================");
        console.log(fileData);
    }
    catch (err) {
        console.error("Error reading the file:", err);
    }
});
readText();
