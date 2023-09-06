import express from "express";
import dotenv from "dotenv";
import { todosRouter } from "./routes/todo";

dotenv.config();
const app = express();
const port = process.env.PORT;

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.use("/todos", todosRouter);

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
