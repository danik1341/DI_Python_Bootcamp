"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.createColorfulMessage = void 0;
const chalk_1 = __importDefault(require("chalk"));
function createColorfulMessage() {
    const colorfulMessage = chalk_1.default.bold
        .rgb(255, 0, 0)
        .bgWhite("Hello, colorful world!");
    return colorfulMessage;
}
exports.createColorfulMessage = createColorfulMessage;
