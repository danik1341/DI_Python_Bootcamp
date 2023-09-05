import express, { Request, Response } from "express";
import dotenv from "dotenv";
import { fetchPosts } from "./data/dataService";

const app = express();
dotenv.config();
const port = process.env.PORT;

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.listen(port, () => {
  console.log(`Server running on ${port}`);
});

app.get("/api/posts", async (req: Request, res: Response) => {
  try {
    const posts = await fetchPosts();
    console.log("Posts fetched successfully", posts);
    res.json(posts);
  } catch (err) {
    console.error("Error fetching posts", err);
    res.status(500).json({ error: `Error fetching posts: ${err}` });
  }
});
