import express, { Request, Response } from "express";

interface Todo {
  id: number;
  text: string;
}

export const todosRouter = express.Router();

const todos: Todo[] = [];

todosRouter.get("/", (req: Request, res: Response) => {
  res.json(todos);
});

todosRouter.post("/", (req: Request, res: Response) => {
  const { text } = req.body;
  const newTodo: Todo = { id: todos.length + 1, text };
  todos.push(newTodo);
  res.status(201).json(newTodo);
});

todosRouter.put("/:id", (req: Request, res: Response) => {
  const { id } = req.body;
  const { text } = req.body;
  const todo = todos.find((item) => item.id === parseInt(id));

  if (!todo) {
    return res.status(404).json({ message: "Todo not found" });
  }
  todo.text = text;
  res.json(todo);
});

todosRouter.delete("/:id", (req: Request, res: Response) => {
  const { id } = req.params;
  const index = todos.findIndex((item) => item.id === parseInt(id));
  if (index === -1) {
    return res.status(404).json({ message: "Todo not found" });
  }
  todos.splice(index, 1);
  res.json({ message: "Todo deleted" });
});
