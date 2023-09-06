import express, { Request, Response } from "express";

interface Book {
  id: number;
  title: string;
  author: string;
}

export const booksRouter = express.Router();

const books: Book[] = [];

booksRouter.get("/", (req: Request, res: Response) => {
  res.json(books);
});

booksRouter.post("/", (req: Request, res: Response) => {
  const { title, author }: { title: string; author: string } = req.body;
  const newBook = { id: books.length + 1, title, author };
  books.push(newBook);
  res.status(201).json(newBook);
});

booksRouter.put("/:id", (req: Request, res: Response) => {
  const { id } = req.params;
  const { title, author }: { title: string; author: string } = req.body;
  const book = books.find((item) => item.id === parseInt(id));
  if (!book) {
    return res.status(404).json({ message: "Book not found" });
  }
  book.title = title;
  book.author = author;
  res.json(book);
});

booksRouter.delete("/:id", (req: Request, res: Response) => {
  const { id } = req.params;
  const index = books.findIndex((item) => item.id === parseInt(id));
  if (index === -1) return res.status(404).json({ message: "Book not found" });
  books.splice(index, 1);
  res.json({ message: "Book deleted" });
});
