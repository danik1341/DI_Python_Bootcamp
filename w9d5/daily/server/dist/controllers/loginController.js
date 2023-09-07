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
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.loginUser = void 0;
const fs_1 = __importDefault(require("fs"));
const loginUser = (req, res) => __awaiter(void 0, void 0, void 0, function* () {
    const { username, password } = req.body;
    try {
        const users = JSON.parse(yield fs_1.default.promises.readFile("users.json", "utf-8"));
        const user = users.find((user) => user.username === username);
        if (!user || user.password !== password) {
            res.status(401).json({ message: "Invalid credentials" });
        }
        else {
            res.json({ message: "Login successful" });
        }
    }
    catch (err) {
        console.error("Error reading user data:", err);
        res.status(500).json({ message: `Internal Server Error: ${err}` });
    }
});
exports.loginUser = loginUser;
