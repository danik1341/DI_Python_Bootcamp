import express from "express";
import dotenv from "dotenv";
import { booksRouter } from "./routes/books";

dotenv.config();
const app = express();
const port = process.env.PORT;

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.use("/books", booksRouter);

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
