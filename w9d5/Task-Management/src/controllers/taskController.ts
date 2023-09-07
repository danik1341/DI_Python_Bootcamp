import { Request, Response } from "express";
import fs from "fs";
import { Task } from "../models/task";

const dataFilePath = "data/tasks.json";

export const getTasks = (req: Request, res: Response) => {
  try {
    const data = JSON.parse(fs.readFileSync(dataFilePath, "utf-8"));
    res.json(data);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Internal server error" });
  }
};

export const getTaskById = (req: Request, res: Response) => {
  const taskId = parseInt(req.params.id);
  if (isNaN(taskId)) {
    res.status(400).json({ error: "Invalid task ID" });
    return;
  }

  try {
    const data = JSON.parse(fs.readFileSync(dataFilePath, "utf-8"));
    const task = data.find((t: Task) => t.id === taskId);
    if (task) {
      res.json(task);
    } else {
      res.status(404).json({ error: "Task not found" });
    }
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: "Internal server error" });
  }
};

export const createTask = (req: Request, res: Response) => {
  const { title, description }: { title: string; description: string } =
    req.body;

  if (!title || !description) {
    res.status(400).json({ error: "Title and description are required" });
    return;
  }

  try {
    const data = JSON.parse(fs.readFileSync(dataFilePath, "utf-8"));
    const lastTask = data[data.length - 1];
    const newTaskId = lastTask ? lastTask.id + 1 : 1;
    const newTask: Task = {
      id: newTaskId,
      title,
      description,
    };

    data.push(newTask);
    fs.writeFileSync(dataFilePath, JSON.stringify(data, null, 2));
    res.status(201).json(newTask);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Internal server error" });
  }
};

export const updateTask = (req: Request, res: Response) => {
  const taskId = parseInt(req.params.id);
  if (isNaN(taskId)) {
    res.status(400).json({ error: "Invalid task ID" });
    return;
  }

  const { title, description }: { title: string; description: string } =
    req.body;

  if (!title || !description) {
    res.status(400).json({ error: "Title and description are required" });
    return;
  }

  try {
    const data = JSON.parse(fs.readFileSync(dataFilePath, "utf-8"));
    const taskIndex = data.findIndex((t: Task) => t.id === taskId);

    if (taskIndex !== -1) {
      const updateTask: Task = {
        id: taskId,
        title,
        description,
      };
      data[taskIndex] = updateTask;
      fs.writeFileSync(dataFilePath, JSON.stringify(data, null, 2));
      res.json(updateTask);
    } else {
      res.status(404).json({ error: "Task not found" });
    }
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Internal server error" });
  }
};

export const deleteTask = (req: Request, res: Response) => {
  const taskId = parseInt(req.params.id);
  if (isNaN(taskId)) {
    res.status(400).json({ error: "Invalid task ID" });
    return;
  }

  try {
    const data = JSON.parse(fs.readFileSync(dataFilePath, "utf-8"));
    const taskIndex = data.findIndex((t: Task) => t.id === taskId);

    if (taskIndex !== -1) {
      const deleteTask = data.splice(taskIndex, 1)[0];
      fs.writeFileSync(dataFilePath, JSON.stringify(data, null, 2));
      res.json(deleteTask);
    } else {
      res.status(404).json({ error: "Task not found" });
    }
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Internal server error" });
  }
};
