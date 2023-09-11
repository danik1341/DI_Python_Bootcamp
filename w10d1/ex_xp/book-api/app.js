import express from "express";

const app = express();
const port = 5000;

const books = [
  { id: 1, title: "Book 1", author: "Author 1", publishedYear: 2021 },
  { id: 2, title: "Book 2", author: "Author 2", publishedYear: 2022 },
];

app.use(express.json());

app.get("/api/books", (req, res) => {
  res.json(books);
});

app.get("/api/books/:bookId", (req, res) => {
  const bookId = parseInt(req.params.bookId);
  const book = books.find((b) => b.id === bookId);

  if (!book) {
    res.status(404).json({ error: "Book not found" });
  } else {
    res.json(book);
  }
});

app.post("/api/books", (req, res) => {
  const { title, author, publishedYear } = req.body;

  // Generate a new unique ID for the book
  const newBookId = books.length + 1;

  const newBook = {
    id: newBookId,
    title,
    author,
    publishedYear,
  };

  books.push(newBook);

  res.status(201).json(newBook);
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
