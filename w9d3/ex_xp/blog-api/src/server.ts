import express, { Request, Response } from "express";
import dotenv from "dotenv";

const app = express();
dotenv.config();

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

const data = [
  {
    id: 1,
    title: "First Post",
    content: "This is the content of the first post",
  },
  {
    id: 2,
    title: "Second Post",
    content: "This is the content of the second post",
  },
];

type Post = {
  id: number;
  title: string;
  content: string;
};

app.listen(process.env.PORT, () => {
  console.log(`Server is running on ${process.env.PORT}`);
});

app.get("/api/posts", (req: Request, res: Response) => {
  let html = "<html><head><title>Blog Posts</title></head><body>";
  data.forEach((post) => {
    html += `<h1>${post.title}</h1><p>${post.content}</p><hr>`;
  });
  html += "</body></html>";
  res.send(html);
});

app.get("/api/posts/:id", (req: Request, res: Response) => {
  const postId = parseInt(req.params.id, 10);
  const post = data.find((post) => post.id === postId);

  if (!post) {
    res.status(404).json({ error: "Post not found" });
  } else {
    res.send(`
    <html>
      <head>
        <title>${post.title}</title>
      </head>
      <body>
        <h1>${post.title}</h1>
        <p>${post.content}</p>
      </body>
    </html>
  `);
  }
});

app.post("/api/posts", (req: Request, res: Response) => {
  const newPost: Post = req.body;

  const postId = Math.max(...data.map((post) => post.id), 0) + 1;

  const post = {
    id: postId,
    title: newPost.title,
    content: newPost.content,
  };

  data.push(post);

  res.status(201).json(post);
});

app.put("/api/posts/:id", (req: Request, res: Response) => {
  const postId = parseInt(req.params.id, 10);
  const postIndex = data.findIndex((post) => post.id === postId);

  if (postIndex === -1) {
    res.status(404).json({ error: "Post not found" });
    return;
  }

  const updatedPost: Post = req.body;

  data[postIndex] = {
    id: postId,
    title: updatedPost.title,
    content: updatedPost.content,
  };

  res.json(data[postIndex]);
});

app.delete("/api/posts/:id", (req: Request, res: Response) => {
  const postId = parseInt(req.params.id, 10);
  const postIndex = data.findIndex((post) => post.id === postId);

  if (postIndex === -1) {
    res.status(404).json({ error: "Post not found" });
    return;
  }

  data.splice(postIndex, 1);

  res.status(204).send();
});
