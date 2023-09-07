import fs from "fs";
import { Request, Response } from "express";

interface User {
  username: string;
  password: string;
}

export const loginUser = async (req: Request, res: Response) => {
  const { username, password }: { username: string; password: string } =
    req.body;

  try {
    const users: User[] = JSON.parse(
      await fs.promises.readFile("data/users.json", "utf-8")
    );
    const user = users.find((user) => user.username === username);

    if (!user || user.password !== password) {
      res.status(401).json({ message: "Invalid credentials" });
    } else {
      res.json({ message: "Login successful" });
    }
  } catch (err) {
    console.error("Error reading user data:", err);
    res.status(500).json({ message: `Internal Server Error: ${err}` });
  }
};
