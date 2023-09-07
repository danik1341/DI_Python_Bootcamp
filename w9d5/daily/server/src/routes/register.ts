import express from "express";
import { registerUser } from "../controllers/registerController";

export const registerRouter = express.Router();

registerRouter.post("/register", registerUser);
