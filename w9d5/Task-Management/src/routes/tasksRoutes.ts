import express from "express";
import {
  createTask,
  deleteTask,
  getTaskById,
  getTasks,
  updateTask,
} from "../controllers/taskController";

const tasksRouter = express.Router();

tasksRouter.get("/tasks", getTasks);
tasksRouter.get("/tasks/:id", getTaskById);
tasksRouter.get("/tasks", createTask);
tasksRouter.get("/tasks/:id", updateTask);
tasksRouter.get("/tasks/:id", deleteTask);

export default tasksRouter;
