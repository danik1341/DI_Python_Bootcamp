"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.registerRouter = void 0;
const express_1 = __importDefault(require("express"));
const registerController_1 = require("../controllers/registerController");
exports.registerRouter = express_1.default.Router();
exports.registerRouter.post("/register", registerController_1.registerUser);
