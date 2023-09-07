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
exports.registerUser = void 0;
const fs_1 = __importDefault(require("fs"));
const registerUser = (req, res) => __awaiter(void 0, void 0, void 0, function* () {
    const userData = req.body;
    try {
        const users = JSON.parse(yield fs_1.default.promises.readFile("users.json", "utf-8"));
        const existingUser = users.find((user) => user.username === userData.username);
        if (existingUser) {
            res.status(400).json({ message: "Username already in use" });
        }
        else {
            users.push(userData);
            yield fs_1.default.promises.writeFile("users.json", JSON.stringify(users, null, 2), "utf-8");
            res.json({ message: "User registration successful" });
        }
    }
    catch (err) {
        console.error("Failed to register user:", err);
        res.json({ message: `Internal Server Error: ${err}` });
    }
});
exports.registerUser = registerUser;
