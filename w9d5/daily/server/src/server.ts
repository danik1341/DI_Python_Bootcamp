import express from "express";
import dotenv from "dotenv";
import { loginRouter } from "./routes/login";
import { registerRouter } from "./routes/register";

const app = express();
dotenv.config();
const port = process.env.PORT;

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.use("/api/", loginRouter);
app.use("/api/", registerRouter);

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
