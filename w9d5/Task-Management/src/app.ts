import express from "express";
import dotenv from "dotenv";
import tasksRouter from "./routes/tasksRoutes";

const app = express();
dotenv.config();
const port = process.env.PORT;

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.use("/api", tasksRouter);

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
