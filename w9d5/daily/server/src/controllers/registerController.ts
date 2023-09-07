import fs from "fs";
import { Request, Response } from "express";

interface User {
  username: string;
  password: string;
}

export const registerUser = async (req: Request, res: Response) => {
  const userData: User = req.body;

  try {
    const users: User[] = JSON.parse(
      await fs.promises.readFile("data/users.json", "utf-8")
    );
    const existingUser = users.find(
      (user) => user.username === userData.username
    );

    if (existingUser) {
      res.status(400).json({ message: "Username already in use" });
    } else {
      users.push(userData);
      await fs.promises.writeFile(
        "data/users.json",
        JSON.stringify(users, null, 2),
        "utf-8"
      );
      res.json({ message: "User registration successful" });
    }
  } catch (err) {
    console.error("Failed to register user:", err);
    res.json({ message: `Internal Server Error: ${err}` });
  }
};
