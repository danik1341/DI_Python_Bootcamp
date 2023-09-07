"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.loginRouter = void 0;
const express_1 = __importDefault(require("express"));
const loginController_1 = require("../controllers/loginController");
exports.loginRouter = express_1.default.Router();
exports.loginRouter.post("/login", loginController_1.loginUser);
