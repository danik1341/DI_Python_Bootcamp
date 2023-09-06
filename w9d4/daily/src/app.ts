import express from "express";
import dotenv from "dotenv";
import { quizRouter } from "./routes/quiz";

dotenv.config();
const app = express();
const port = process.env.PORT;

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.use("/api", quizRouter);

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
