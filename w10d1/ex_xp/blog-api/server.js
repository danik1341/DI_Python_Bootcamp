import express from "express";
import dotenv from "dotenv";
import bodyParser from "body-parser";
import postsRouter from "./routes/posts.js";
import errorHandler from "./config/errorHandler";

const app = express();
dotenv.config();
const port = process.env.PORT;

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.use("/", postsRouter);

app.use(errorHandler);

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
