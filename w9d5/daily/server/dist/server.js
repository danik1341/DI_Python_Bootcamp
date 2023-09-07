"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = __importDefault(require("express"));
const dotenv_1 = __importDefault(require("dotenv"));
const login_1 = require("./routes/login");
const register_1 = require("./routes/register");
const app = (0, express_1.default)();
dotenv_1.default.config();
const port = process.env.PORT;
app.use(express_1.default.urlencoded({ extended: true }));
app.use(express_1.default.json());
app.use("/api/", login_1.loginRouter);
app.use("/api/", register_1.registerRouter);
app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
