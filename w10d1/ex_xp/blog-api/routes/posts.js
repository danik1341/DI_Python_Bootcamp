import express from "express";
import { pool } from "../config/db";

const postsRouter = express.Router();

postsRouter.get("/posts", (req, res) => {
  pool.query("SELECT * FROM posts", (err, result) => {
    if (err) {
      console.error(err);
      res.status(500).json({ error: "Server error" });
    } else {
      res.json(result.rows);
    }
  });
});

postsRouter.get("/posts/:id", (req, res) => {
  const postId = req.params.id;
  pool.query("SELECT * FROM posts WHERE id = $1", [postId], (err, result) => {
    if (err) {
      console.error(err);
      res.status(500).json({ error: "Server error" });
    } else if (result.rows.length === 0) {
      res.status(404).json({ error: "Post not found" });
    } else {
      res.json(result.rows[0]);
    }
  });
});

postsRouter.post("/posts", (req, res) => {
  const { title, content } = req.body;
  pool.query(
    "INSERT INTO posts (title, content) VALUES ($1, $2)",
    [title, content],
    (err) => {
      if (err) {
        console.error(err);
        res.status(500).json({ error: "Server error" });
      } else {
        res.status(201).json({ message: "Post created successfully" });
      }
    }
  );
});

postsRouter.put("/posts/:id", (req, res) => {
  const postId = req.params.id;
  const { title, content } = req.body;
  pool.query(
    "UPDATE posts SET title = $1, content = $2 WHERE id = $3",
    [title, content, postId],
    (err, result) => {
      if (err) {
        console.error(err);
        res.status(500).json({ error: "Server error" });
      } else if (result.rowCount === 0) {
        res.status(404).json({ error: "Post not found" });
      } else {
        res.json({ message: "Post updated successfully" });
      }
    }
  );
});

postsRouter.delete("/posts/:id", (req, res) => {
  const postId = req.params.id;
  pool.query("DELETE FROM posts WHERE id = $1", [postId], (err, result) => {
    if (err) {
      console.error(err);
      res.status(500).json({ error: "Server error" });
    } else if (result.rowCount === 0) {
      res.status(404).json({ error: "Post not found" });
    } else {
      res.json({ message: "Post deleted successfully" });
    }
  });
});

export default postsRouter;
