import express, { Request, Response } from "express";
import dotenv from "dotenv";

const app = express();
dotenv.config();
const port = process.env.PORT;

type Book = {
  title: string;
  author: string;
  publishedYear: number;
};

const books = [
  {
    id: 1,
    title: "The Stormlight Archive: The Way of Kings",
    author: "Brandon Sanderson",
    publishedYear: 2010,
  },
  {
    id: 2,
    title: "The Stormlight Archive: Words of Radiance",
    author: "Brandon Sanderson",
    publishedYear: 2014,
  },
  {
    id: 3,
    title: "The Stormlight Archive: Oathbringer",
    author: "Brandon Sanderson",
    publishedYear: 2017,
  },
  {
    id: 4,
    title: "The Stormlight Archive: Rhythm of War",
    author: "Brandon Sanderson",
    publishedYear: 2020,
  },
];

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

app.get("/api/books", (req: Request, res: Response) => {
  res.json(books);
});

app.get("/api/books/:bookId", (req: Request, res: Response) => {
  const bookId = parseInt(req.params.bookId, 10);
  const book = books.find((book) => book.id === bookId);

  if (!book) {
    res.status(404).json({ error: "Book not found" });
  } else {
    res.json(book);
  }
});

app.post("/api/books", (req: Request, res: Response) => {
  const newBook: Book = req.body;

  const newId = Math.max(...books.map((book) => book.id), 0) + 1;

  const book = {
    id: newId,
    ...newBook,
  };

  books.push(book);

  res.status(201).json(book);
});
